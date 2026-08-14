"""Utilities for building 2D self-attention masks for conditioning items.

Ported from ltx-core/src/ltx_core/conditioning/mask_utils.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import mlx.core as mx

if TYPE_CHECKING:
    from ltx_core_mlx.conditioning.types.latent_cond import LatentState


def resolve_cross_mask(
    attention_mask: float | int | mx.array,
    num_new_tokens: int,
    batch_size: int,
) -> mx.array:
    """Convert an attention_mask (scalar or array) to a (B, M) cross_mask.

    Args:
        attention_mask: Scalar, 1D (M,), or 2D (B, M) array.
        num_new_tokens: Number of new conditioning tokens M.
        batch_size: Batch size B.

    Returns:
        Cross-mask of shape (B, M).
    """
    if isinstance(attention_mask, int | float):
        return mx.full((batch_size, num_new_tokens), attention_mask)

    mask = attention_mask
    if mask.ndim == 0:
        return mx.full((batch_size, num_new_tokens), float(mask.item()))

    if mask.ndim == 1:
        if mask.shape[0] != num_new_tokens:
            raise ValueError(
                f"1-D attention_mask length must equal num_new_tokens ({num_new_tokens}), got shape {tuple(mask.shape)}"
            )
        return mx.broadcast_to(mask[None, :], (batch_size, num_new_tokens))

    if mask.ndim == 2:
        _b, m = mask.shape
        if m != num_new_tokens:
            raise ValueError(
                f"2-D attention_mask dim-1 must equal num_new_tokens ({num_new_tokens}), got shape {tuple(mask.shape)}"
            )
        return mx.broadcast_to(mask, (batch_size, num_new_tokens))

    raise ValueError(f"attention_mask must be 0-D, 1-D, or 2-D, got {mask.ndim}-D")


def build_attention_mask(
    existing_mask: mx.array | None,
    num_noisy_tokens: int,
    num_new_tokens: int,
    num_existing_tokens: int,
    cross_mask: mx.array,
) -> mx.array:
    """Build or expand a (B, N+M, N+M) self-attention mask.

    Block structure:
                 noisy      prev_ref    new_ref
               (N_noisy)   (N-N_noisy)    (M)
             +───────────+───────────+───────────+
    noisy    |  existing |  existing |   cross   |
             +───────────+───────────+───────────+
    prev_ref |  existing |  existing |     0     |
             +───────────+───────────+───────────+
    new_ref  |   cross   |     0     |     1     |
             +───────────+───────────+───────────+

    Args:
        existing_mask: Current mask (B, N, N) or None.
        num_noisy_tokens: Original noisy token count.
        num_new_tokens: New conditioning tokens M.
        num_existing_tokens: Current total tokens N.
        cross_mask: Per-token attention weight (B, M), values in [0, 1].

    Returns:
        Attention mask (B, N+M, N+M).
    """
    batch_size = cross_mask.shape[0]
    num_previous_reference_tokens = num_existing_tokens - num_noisy_tokens

    if existing_mask is None:
        existing_mask = mx.ones((batch_size, num_existing_tokens, num_existing_tokens))

    # Build the four blocks directly. Chaining lazy ``array.at[...].add``
    # updates can overwrite an earlier disjoint slice on MLX 0.31.2, which is
    # the minimum runtime required by the Gemma 4 backend.
    noisy_to_new = mx.broadcast_to(cross_mask[:, None, :], (batch_size, num_noisy_tokens, num_new_tokens))
    previous_to_new = mx.zeros((batch_size, num_previous_reference_tokens, num_new_tokens))
    top_right = mx.concatenate([noisy_to_new, previous_to_new], axis=1)
    top = mx.concatenate([existing_mask, top_right], axis=2)

    new_to_noisy = mx.broadcast_to(cross_mask[:, :, None], (batch_size, num_new_tokens, num_noisy_tokens))
    new_to_previous = mx.zeros((batch_size, num_new_tokens, num_previous_reference_tokens))
    bottom_left = mx.concatenate([new_to_noisy, new_to_previous], axis=2)
    new_to_new = mx.ones((batch_size, num_new_tokens, num_new_tokens))
    bottom = mx.concatenate([bottom_left, new_to_new], axis=2)

    return mx.concatenate([top, bottom], axis=1)


def update_attention_mask(
    latent_state: LatentState,
    attention_mask: float | mx.array | None,
    num_noisy_tokens: int,
    num_new_tokens: int,
    batch_size: int,
) -> mx.array | None:
    """Build or update the self-attention mask for newly appended conditioning tokens.

    If attention_mask is None and no existing mask is present, returns None.
    If attention_mask is None but an existing mask is present, the mask is
    expanded with full attention (1s) for the new tokens.

    Args:
        latent_state: Current latent state.
        attention_mask: Per-token attention weight (scalar, 1D, 2D, or None).
        num_noisy_tokens: Original noisy token count.
        num_new_tokens: New conditioning tokens being appended.
        batch_size: Batch size.

    Returns:
        Updated mask (B, N+M, N+M) or None.
    """
    if attention_mask is None:
        if latent_state.attention_mask is None:
            return None
        cross_mask = mx.ones((batch_size, num_new_tokens))
        return build_attention_mask(
            existing_mask=latent_state.attention_mask,
            num_noisy_tokens=num_noisy_tokens,
            num_new_tokens=num_new_tokens,
            num_existing_tokens=latent_state.latent.shape[1],
            cross_mask=cross_mask,
        )

    cross_mask = resolve_cross_mask(attention_mask, num_new_tokens, batch_size)
    return build_attention_mask(
        existing_mask=latent_state.attention_mask,
        num_noisy_tokens=num_noisy_tokens,
        num_new_tokens=num_new_tokens,
        num_existing_tokens=latent_state.latent.shape[1],
        cross_mask=cross_mask,
    )

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_github_token_release_fallback_relocks_and_dispatches_ci() -> None:
    workflow = (REPO_ROOT / ".github/workflows/release-please.yml").read_text()

    assert "id: release" in workflow
    assert "steps.release.outputs.prs_created == 'true'" in workflow
    assert "headBranchName" in workflow
    assert "fallback-relock:" in workflow
    assert "fallback-push:" in workflow
    assert "actions/upload-artifact@" in workflow
    assert "actions/download-artifact@" in workflow
    assert "duplicate workspace packages" in workflow
    assert "changes data beyond the four workspace versions" in workflow
    assert 'gh workflow run ci.yml --ref "$HEAD_REF"' in workflow


def test_fallback_ci_can_be_dispatched_and_release_tokens_are_limited() -> None:
    ci_workflow = (REPO_ROOT / ".github/workflows/ci.yml").read_text()
    release_workflow = (REPO_ROOT / ".github/workflows/release-please.yml").read_text()
    relock_workflow = (REPO_ROOT / ".github/workflows/relock-on-release.yml").read_text()

    assert "workflow_dispatch:" in ci_workflow
    assert "permission-contents: write" in release_workflow
    assert "permission-pull-requests: write" in release_workflow
    assert "enable-cache: false" in release_workflow
    assert "permission-contents: write" in relock_workflow
    assert "needs: relock" in relock_workflow
    assert 'if [[ "$APP_CONFIGURED" != "true" ]]' in relock_workflow

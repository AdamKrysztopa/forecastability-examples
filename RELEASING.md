# Release Dance (EX-REL-01)

This document records the two-repo release sequence for coordinated `dependence-forecastability` + `forecastability-examples` releases.

## Prerequisites

- Core repo has a passing CI on the release branch.
- Sibling notebooks CI is green against the current core dev build.

## Two-repo release sequence

### Step 1 — Core RC1

1. In core: `git tag v0.4.0rc1 && git push origin v0.4.0rc1`
2. Core RC1 publishes to TestPyPI via the Trusted Publishing flow.

### Step 2 — Sibling pre-flight (EX-REL-02)

Run the sibling notebook matrix against the TestPyPI or `git+` source:

```bash
# TestPyPI source
uv sync --all-extras --override-dependencies \
  "dependence-forecastability==0.4.0rc1 --index https://test.pypi.org/simple/"

# git+ source (alternative)
uv sync --all-extras --override-dependencies \
  "dependence-forecastability @ git+https://github.com/AdamKrysztopa/dependence-forecastability.git@v0.4.0rc1"
```

Either green satisfies the acceptance gate; both green is preferred.

### Step 3 — Core final release

1. `git tag v0.4.0 && git push origin v0.4.0`
2. Core PyPI publish completes via Trusted Publishing.
3. Core release workflow emits `repository_dispatch` event `core_release` with `payload.version = "0.4.0"`.

### Step 4 — Sibling handshake fires (EX-CPL-01)

The sibling `.github/workflows/release.yml` triggers on `repository_dispatch`.
It runs the full notebook matrix against the new PyPI artifact and posts a
status comment on the core release page.

### Step 5 — Sibling pin bump and release

1. Update `pyproject.toml` in sibling if needed to pin `dependence-forecastability==0.4.0,<0.5`.
2. `git tag v0.4.0 && git push origin v0.4.0`
3. Sibling release publishes executed notebooks as release assets.

### Cross-repo PR linking

Each core PR that has a sibling counterpart should link both in the PR description.
Shared milestone: `v0.4.0 across both repos` in the GitHub Project (EX-CPL-02).

# Release Dance (EX-REL-01)

This document records the two-repo release sequence for coordinated
`dependence-forecastability` (core) + `forecastability-examples` (sibling) releases.

## Prerequisites

Before starting the dance, confirm:

- [ ] All Batch items for the target version are marked **Implemented** in the plan file.
- [ ] Core branch CI is green on the release branch (`chore/0-4-0-repos-split` or `main`).
- [ ] Sibling notebooks CI (`notebooks.yml`) is green on `main` against the current pinned source.
- [ ] Core `pyproject.toml`, `src/forecastability/__init__.py`, `CITATION.cff`, and `CHANGELOG.md` all agree on the target version.
- [ ] Core `docs/releases/v<VERSION>.md` release notes file exists and is non-empty.
- [ ] Sibling `pyproject.toml` and `uv.lock` agree. The final `dependence-forecastability>=<VERSION>,<next-minor>` pin bump happens after the core package is live on PyPI in Step 6.

## Notebook commit policy

**Commit notebooks with executed outputs** (with data). Before committing:

```bash
# Execute all notebooks in place (run from the repo root)
uv run jupyter nbconvert \
  --to notebook \
  --execute \
  --inplace \
  --ExecutePreprocessor.timeout=600 \
  walkthroughs/*.ipynb \
  triage_walkthroughs/*.ipynb \
  recipes/**/*.ipynb
```

Do not strip outputs before committing. CI re-executes notebooks on every push
and uploads executed versions as artifacts; having outputs in the repo makes the
notebooks immediately usable on GitHub without a local execution step.

---

## Two-repo release sequence

### Step 1 — Merge release branch to core `main`

1. Open a PR from `chore/0-4-0-repos-split` → `main` in the core repo.
2. Confirm all CI checks are green.
3. Merge (do not squash — preserve granular commit history).

### Step 2 — Core pre-flight ref

Do **not** push a release-candidate tag unless the core publish workflow has been explicitly changed for TestPyPI. The current core `publish-pypi.yml` workflow publishes `v*` tags to production PyPI.

Use a core branch or tag candidate as a `git+` source in the sibling pre-flight workflow. Use `source=testpypi` only when a maintainer has manually published a TestPyPI artifact for the same version.

### Step 3 — Sibling pre-flight (EX-REL-02)

Run the pre-flight matrix in the sibling repo against a `git+` ref before the final core release. If a TestPyPI artifact exists, the same workflow can also test that source.

**Via GitHub Actions UI:**

1. Go to **Actions → Pre-flight Matrix (EX-REL-02)** in the sibling repo.
2. Click **Run workflow**.
3. Set `core_version` to the RC version string or branch name and `source` to `testpypi` or `git`.

**Via CLI:**

```bash
# git+ source — use core release branch or candidate tag
gh workflow run preflight.yml \
  --repo AdamKrysztopa/forecastability-examples \
  -f core_version=<core-release-branch-or-tag> \
  -f source=git
```

**Acceptance gate:** the `git` matrix must be green before Step 4. If a TestPyPI artifact exists, run that matrix too; it is additional evidence, not a substitute for the git pre-flight.

### Step 4 — Core final tag and PyPI publish

1. In core: `git tag v<VERSION> && git push origin v<VERSION>`
2. `publish-pypi.yml` triggers:
   - Builds, lints, type-checks, tests, and publishes to PyPI via Trusted Publishing.
   - After successful publish, the `notify-sibling` job fires a `repository_dispatch`
     (`event_type = core_release`, with `client_payload.version`, `client_payload.tag`, and `client_payload.pypi_url`) to this repo.
   - **Requires secret:** `EXAMPLES_DISPATCH_TOKEN` — a PAT with `contents:write` scope on
     `AdamKrysztopa/forecastability-examples`, stored as a repository secret in the core repo.
3. `release.yml` triggers in core: creates the GitHub release from `docs/releases/v<VERSION>.md`.

### Step 5 — Sibling handshake fires (EX-CPL-01)

After Step 4, the sibling `.github/workflows/release.yml` auto-triggers on `repository_dispatch`.
It runs the full notebook matrix against the new PyPI artifact and uploads executed notebooks
as workflow artifacts named `release-notebooks-py<VER>-v<VERSION>`.

Monitor at: <https://github.com/AdamKrysztopa/forecastability-examples/actions/workflows/release.yml>

**Manual fallback** (if the dispatch fails or EXAMPLES_DISPATCH_TOKEN is not set):

```bash
gh workflow run release.yml \
  --repo AdamKrysztopa/forecastability-examples \
  -f core_version=<VERSION>
```

### Step 6 — Sibling pin bump and release

> **Important:** The pin bump must happen **after** the core package is live on PyPI (Step 4),
> not before. Bumping the pin before publish will break the sibling CI because `uv sync` resolves
> against PyPI and the new version won't be found.

1. Bump `pyproject.toml` pin: `dependence-forecastability>=<VERSION>,<next-minor>`.
2. Regenerate the lockfile: `uv lock`.
3. Execute all notebooks and commit everything (lockfile + pyproject + notebooks) with outputs —
   see the notebook commit policy above.
4. `git tag v<VERSION> && git push origin v<VERSION>`
5. The sibling release tag triggers the release handshake workflow and uploads executed notebooks as workflow artifacts.

---

## Setting up EXAMPLES_DISPATCH_TOKEN

This secret is required for the automatic cross-repo handshake (Step 4/5).

1. Create a **fine-grained PAT** at <https://github.com/settings/personal-access-tokens/new>:
   - Repository access: `AdamKrysztopa/forecastability-examples`
   - Permissions: **Contents** → Read and write
2. Copy the token value.
3. In the **core repo** (`dependence-forecastability`) → Settings → Secrets and variables → Actions:
   - Create a new repository secret named `EXAMPLES_DISPATCH_TOKEN`.
   - Paste the token value.

---

## Cross-repo PR linking

Each core PR that has a sibling counterpart should link both in the PR description.
Shared milestone: `v<VERSION> across both repos` in the GitHub Project (EX-CPL-02).

## Rollback

If PyPI publish succeeds but the sibling matrix fails:
1. Do **not** yank the PyPI release unless the published artifact is broken.
2. File an issue in the sibling repo, fix the notebook, re-run the handshake manually (Step 5 fallback).
3. If the artifact itself is broken: use `uv pip install dependence-forecastability==<PREVIOUS_VERSION>` to roll back sibling CI, then coordinate with core to yank and re-release.


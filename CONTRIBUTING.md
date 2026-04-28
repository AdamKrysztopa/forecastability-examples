# Contributing to forecastability-examples

## Repository relationship

This repository contains tutorials, walkthroughs, and integration notebooks for the
[`dependence-forecastability`](https://github.com/AdamKrysztopa/dependence-forecastability) toolkit.

- **Bugs in triage logic / public API** → file issues at the [core repo](https://github.com/AdamKrysztopa/dependence-forecastability/issues)
- **Bugs in notebooks or framework wiring** → file issues here

## Development setup

```bash
git clone https://github.com/AdamKrysztopa/forecastability-examples.git
cd forecastability-examples
uv sync --all-extras
uv run jupyter lab
```

## Notebook authoring policy (EX-NB-EXEC-01)

**Commit notebooks with cleared outputs.** Never commit executed cell outputs.

Rationale: executed outputs create large diffs and stale HTML; CI re-executes every notebook
and uploads executed versions as build artifacts on each push.

Before committing:

```bash
uv run jupyter nbconvert --to notebook --clear-output --inplace walkthroughs/*.ipynb
```

CI runs:

```bash
uv run jupyter nbconvert --to notebook --execute --inplace walkthroughs/*.ipynb triage_walkthroughs/*.ipynb
```

Executed notebooks are uploaded as GitHub Actions artifacts on each successful run.
On releases, they are published as release assets.

## Import surface constraint

Notebooks may only import from the public `forecastability` API:

```python
from forecastability import ...
from forecastability.triage import ...
```

**Never** import from internal namespaces:

- `forecastability.services`
- `forecastability.use_cases`
- `forecastability.utils`
- `forecastability.adapters`
- `forecastability.diagnostics`

CI enforces this with a grep lint step.

## Framework dependencies

Framework deps (`darts`, `mlforecast`, etc.) are optional extras. Install what you need:

```bash
uv sync --extra darts
uv sync --extra mlforecast
uv sync --all-extras  # everything
```

## Local development against a core branch

See `docs/development/local_workspace.md` in the core repo for the full local two-repo
workflow (arriving in EX-LOCAL-01 / Batch 1b).

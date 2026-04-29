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

**Commit notebooks with executed outputs** (with data). Execute all notebooks before committing:

```bash
uv run jupyter nbconvert \
  --to notebook \
  --execute \
  --inplace \
  --ExecutePreprocessor.timeout=600 \
  walkthroughs/*.ipynb \
  triage_walkthroughs/*.ipynb \
  recipes/**/*.ipynb
```

Having outputs in the repo makes notebooks immediately usable on GitHub without a local
execution step. CI also re-executes notebooks on every push and uploads executed versions as
build artifacts.

Before opening a PR, verify notebooks execute cleanly on a fresh `uv sync --all-extras`
environment and re-commit the executed outputs.

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

See [`docs/development/local_workspace.md`](https://github.com/AdamKrysztopa/dependence-forecastability/blob/main/docs/development/local_workspace.md)
in the core repo for the full local two-repo workflow.

**Quick start:**

```bash
# From the core repo root
export FORECASTABILITY_LOCAL_DEV=1
bash scripts/bootstrap_local_workspace.sh
```

This clones the sibling (if absent), creates the multi-root VS Code workspace,
and installs the core in editable mode into the sibling's venv so your local
core changes are immediately visible.

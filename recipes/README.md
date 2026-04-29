# Recipes

Short, focused integration snippets showing how to wire `forecastability` outputs to downstream forecasting frameworks.

## Available recipes

| Notebook | Description |
| --- | --- |
| [contract_roundtrip.ipynb](contract_roundtrip.ipynb) | `ForecastPrepContract` round-trip — `model_dump_json()` → disk → `model_validate_json()` without re-importing `forecastability` |

## Cross-repo links

- **Core text recipe** (framework-agnostic): [`docs/recipes/forecast_prep_to_external_frameworks.md`](https://github.com/AdamKrysztopa/dependence-forecastability/blob/main/docs/recipes/forecast_prep_to_external_frameworks.md)
- Core examples index (all notebooks): [`docs/examples_index.md`](https://github.com/AdamKrysztopa/dependence-forecastability/blob/main/docs/examples_index.md)
- **Executed notebooks** (release assets): [forecastability-examples releases](https://github.com/AdamKrysztopa/forecastability-examples/releases) — each release ships fully executed notebooks (including `contract_roundtrip.ipynb`) as downloadable artifacts

## Framework support

| Framework | Optional extra | Install |
| --- | --- | --- |
| Darts | `darts` | `pip install "dependence-forecastability[darts]"` from the sibling |
| MLForecast | `mlforecast` | `pip install "dependence-forecastability[mlforecast]"` from the sibling |
| statsforecast | `statsforecast` | `pip install "dependence-forecastability[statsforecast]"` from the sibling |

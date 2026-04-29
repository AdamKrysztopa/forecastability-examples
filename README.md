# forecastability-examples

Tutorials, walkthroughs, and integrations for the [`dependence-forecastability`](https://github.com/AdamKrysztopa/dependence-forecastability) toolkit

[![Notebooks](https://github.com/AdamKrysztopa/forecastability-examples/actions/workflows/notebooks.yml/badge.svg)](https://github.com/AdamKrysztopa/forecastability-examples/actions/workflows/notebooks.yml)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)

---

## Installation

Install the core toolkit with any optional framework extras you need:

```bash
pip install "dependence-forecastability[darts,mlforecast]"
```

Or with `uv`:

```bash
uv add dependence-forecastability
```

For the full examples environment (all extras + dev tooling):

```bash
uv sync --all-extras
```

---

## Quick links

| Directory | Contents |
| --- | --- |
| [`walkthroughs/`](walkthroughs/) | Step-by-step forecastability walkthroughs |
| [`triage_walkthroughs/`](triage_walkthroughs/) | Focused single-capability triage notebooks |
| [`recipes/`](recipes/) | Short framework-integration snippets |

---

## Notebook index

### Walkthroughs

| Notebook | Description | Dataset |
| --- | --- | --- |
| [`walkthroughs/00_air_passengers_showcase.ipynb`](walkthroughs/00_air_passengers_showcase.ipynb) | Canonical forecastability triage on the Air Passengers series | Air Passengers (Box & Jenkins) |
| [`walkthroughs/01_canonical_forecastability.ipynb`](walkthroughs/01_canonical_forecastability.ipynb) | End-to-end forecastability triage walkthrough | Synthetic |
| [`walkthroughs/01_covariant_informative_showcase.ipynb`](walkthroughs/01_covariant_informative_showcase.ipynb) | Covariant informative analysis showcase | Synthetic |
| [`walkthroughs/02_exogenous_analysis.ipynb`](walkthroughs/02_exogenous_analysis.ipynb) | Exogenous driver analysis with CrossAMI / pCrossAMI | Synthetic |
| [`walkthroughs/02_forecastability_fingerprint_showcase.ipynb`](walkthroughs/02_forecastability_fingerprint_showcase.ipynb) | Geometry-backed forecastability fingerprinting | Synthetic |
| [`walkthroughs/03_lagged_exogenous_triage_showcase.ipynb`](walkthroughs/03_lagged_exogenous_triage_showcase.ipynb) | Lagged exogenous triage with sparse lag selection | Synthetic |
| [`walkthroughs/03_triage_end_to_end.ipynb`](walkthroughs/03_triage_end_to_end.ipynb) | Full triage-to-contract pipeline | Synthetic |
| [`walkthroughs/04_routing_validation_showcase.ipynb`](walkthroughs/04_routing_validation_showcase.ipynb) | Routing validation and audit outcomes | Synthetic |
| [`walkthroughs/04_screening_end_to_end.ipynb`](walkthroughs/04_screening_end_to_end.ipynb) | Exogenous screening workbench end-to-end | Synthetic |
| [`walkthroughs/05_forecast_prep_to_models.ipynb`](walkthroughs/05_forecast_prep_to_models.ipynb) | Triage → `ForecastPrepContract` → Darts / MLForecast / sklearn | Air Passengers |
| [`walkthroughs/06_triage_driven_vs_naive_on_m4.ipynb`](walkthroughs/06_triage_driven_vs_naive_on_m4.ipynb) | Triage-driven model selection vs SeasonalNaive on M4 monthly | M4 monthly (≤ 200 series) |
| [`walkthroughs/07_causal_rivers_lag_and_feature_selection.ipynb`](walkthroughs/07_causal_rivers_lag_and_feature_selection.ipynb) | Deterministic lag & feature selection on CausalRivers benchmark | CausalRivers (East Germany) |

### Triage walkthroughs

| Notebook | Description |
| --- | --- |
| [`triage_walkthroughs/01_forecastability_profile_walkthrough.ipynb`](triage_walkthroughs/01_forecastability_profile_walkthrough.ipynb) | F1 — Forecastability profile and informative horizons |
| [`triage_walkthroughs/02_information_limits_and_compression.ipynb`](triage_walkthroughs/02_information_limits_and_compression.ipynb) | F2 — Information-theoretic limit diagnostics |
| [`triage_walkthroughs/03_predictive_information_learning_curves.ipynb`](triage_walkthroughs/03_predictive_information_learning_curves.ipynb) | F3 — Predictive information learning curves |
| [`triage_walkthroughs/04_spectral_and_entropy_diagnostics.ipynb`](triage_walkthroughs/04_spectral_and_entropy_diagnostics.ipynb) | F4/F6 — Spectral predictability and entropy diagnostics |
| [`triage_walkthroughs/05_batch_and_exogenous_workbench.ipynb`](triage_walkthroughs/05_batch_and_exogenous_workbench.ipynb) | F7/F8 — Batch multi-signal ranking and enhanced exogenous screening |
| [`triage_walkthroughs/06_agent_ready_triage_interpretation.ipynb`](triage_walkthroughs/06_agent_ready_triage_interpretation.ipynb) | Agent-ready triage interpretation and narration |

### Recipes

| Notebook | Description |
| --- | --- |
| [`recipes/contract_roundtrip.ipynb`](recipes/contract_roundtrip.ipynb) | `ForecastPrepContract` JSON roundtrip — serialize, deserialize, re-validate |

---

## Where to file issues

| Issue type | Where |
| --- | --- |
| Bugs in triage logic or the public API | [dependence-forecastability issues](https://github.com/AdamKrysztopa/dependence-forecastability/issues) |
| Bugs in notebooks or framework wiring | [forecastability-examples issues](https://github.com/AdamKrysztopa/forecastability-examples/issues) |

---

## Development

```bash
git clone https://github.com/AdamKrysztopa/forecastability-examples.git
cd forecastability-examples
uv sync --all-extras
uv run jupyter lab
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT — see [LICENSE](LICENSE).

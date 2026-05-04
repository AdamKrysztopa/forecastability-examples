# Walkthroughs

Step-by-step forecastability walkthroughs using the `dependence-forecastability` toolkit.

The extended fingerprint walkthroughs remain AMI-first: additive diagnostics explain structure around lag geometry rather than replacing it, and they stop before downstream model fitting.

| Notebook | Description |
| --- | --- |
| [00_air_passengers_showcase.ipynb](00_air_passengers_showcase.ipynb) | All forecastability methods demonstrated on the Air Passengers series |
| [01_canonical_forecastability.ipynb](01_canonical_forecastability.ipynb) | AMI vs pAMI forecastability triage on canonical synthetic cases; full report output |
| [01_covariant_informative_showcase.ipynb](01_covariant_informative_showcase.ipynb) | Covariate informativeness triage — when does an exogenous driver improve forecastability? |
| [02_exogenous_analysis.ipynb](02_exogenous_analysis.ipynb) | CrossAMI and pCrossAMI exogenous screening on bike-sharing, AAPL/SPY, and BTC/ETH series |
| [02_forecastability_fingerprint_showcase.ipynb](02_forecastability_fingerprint_showcase.ipynb) | Forecastability fingerprint — compact four-field profile and routing recommendation |
| [03_lagged_exogenous_triage_showcase.ipynb](03_lagged_exogenous_triage_showcase.ipynb) | Lagged-exogenous triage — driver lag roles, sparse selection, and tensor-ready lag maps |
| [03_triage_end_to_end.ipynb](03_triage_end_to_end.ipynb) | End-to-end agentic triage walkthrough; the consumer surface for automated triage pipelines |
| [04_routing_validation_showcase.ipynb](04_routing_validation_showcase.ipynb) | Routing validation — auditing deterministic routing against synthetic archetypes |
| [04_screening_end_to_end.ipynb](04_screening_end_to_end.ipynb) | Agentic feature screening — which exogenous drivers matter for forecastability? |
| [05_forecast_prep_to_models.ipynb](05_forecast_prep_to_models.ipynb) | Triage → `ForecastPrepContract` → hand-off to Darts, MLForecast, and sklearn Ridge; demonstrates the v0.3.4 sprint |
| [06_triage_driven_vs_naive_on_m4.ipynb](06_triage_driven_vs_naive_on_m4.ipynb) | Triage-driven model-family selection vs SeasonalNaive on M4 monthly subset (≤ 200 series) |
| [07_causal_rivers_lag_and_feature_selection.ipynb](07_causal_rivers_lag_and_feature_selection.ipynb) | Capability demo on the CausalRivers benchmark — self-lag and exogenous lag selection recovering graph-verified positives and rejecting negative controls |
| [08_extended_forecastability_showcase.ipynb](08_extended_forecastability_showcase.ipynb) | AMI-first extended forecastability showcase across the deterministic seven-series panel; writes sibling-repo figures and tables when run locally |

See also the [triage walkthroughs](../triage_walkthroughs/) and [recipes](../recipes/).

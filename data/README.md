# Data

This directory contains small vendored datasets and serves as the output location for datasets fetched at CI time.

## Data origin table

| Notebook | Dataset | Origin | License | Shipped where |
| --- | --- | --- | --- | --- |
| `walkthroughs/00_air_passengers_showcase.ipynb` | Air Passengers (monthly, 1949–1960) | Box & Jenkins | Public domain | Vendored CSV in `data/air_passengers.csv` |
| `walkthroughs/01_canonical_forecastability.ipynb` | Synthetic AR(1) + Lorenz | Generated in-notebook | n/a | None |
| `walkthroughs/02_exogenous_analysis.ipynb` | Bike-sharing hourly (UCI), AAPL/SPY log-returns, BTC/ETH log-returns | UCI ML repo + Yahoo Finance + CoinGecko snapshots | UCI: CC BY 4.0; financial snapshots: vendored aggregates only | Vendored aggregates in `data/exogenous_demos/` |
| `walkthroughs/03_etth1_subset.ipynb` | ETTh1 OHT subset | [Informer/ETT release](https://github.com/zhouhaoyi/ETDataset) | CC BY 4.0 | Vendored CSV in `data/etth1_oht_subset.csv` |
| `walkthroughs/04_routing_validation_showcase.ipynb` and `04_screening_end_to_end.ipynb` | M4 monthly subset (≤ 200 series) | [M4 competition](https://github.com/Mcompetitions/M4-methods) | CC BY 4.0 | Fetched + cached via ported `download_data.py` |
| `walkthroughs/05_forecast_prep_to_models.ipynb` | Synthetic via `forecastability.generate_ar1` | n/a | n/a | None |
| `walkthroughs/06_triage_driven_vs_naive_on_m4.ipynb` | M4 monthly subset | as above | CC BY 4.0 | Same cached fetch as row above |
| `walkthroughs/07_causal_rivers_lag_and_feature_selection.ipynb` | CausalRivers East Germany subset (8 stations, 6h-resampled) | [CausalRivers benchmark](https://github.com/CausalRivers/causalrivers) | dl-de/by-2-0 | Fetched + cached via `scripts/download_causal_rivers.py` into `data/causal_rivers/east_germany_8stations_6h.parquet` |
| `recipes/contract_roundtrip.ipynb` | Synthetic via `forecastability.generate_ar1` | n/a | n/a | None |

## Fetching data at CI time

Notebooks that require fetching use a `_FETCHED` marker file pattern. The CI workflow caches fetched data via `actions/cache@v4`.

For the CausalRivers data, see `scripts/download_causal_rivers.py` (arriving in EX-NB-DATA-02).

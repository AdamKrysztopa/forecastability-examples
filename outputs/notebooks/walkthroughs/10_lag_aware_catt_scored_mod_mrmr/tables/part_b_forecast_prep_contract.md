# Forecast Prep Contract

## Metadata

- source_goal: lagged_exogenous
- blocked: False
- readiness_status: clear
- confidence_label: medium
- target_frequency: 6h
- horizon: 4
- contract_version: 0.3.4

## Target Lags

**recommended_target_lags:**
- 1

**recommended_seasonal_lags:**
(none)

**excluded_target_lags:**
(none)

**lag_rationale:**
- lag 1 is the strongest non-seasonal lag
- lag 2 is secondary under current confidence
- lag 3 is secondary under current confidence
- lag 4 is secondary under current confidence
- lag 5 is secondary under current confidence

## Model Families

**recommended_families:**
(none)

**baseline_families:**
- naive
- seasonal_naive

## Covariates

**past_covariates:**
- station_1095
- station_313
- station_490
- station_67
- station_71
- station_758
- station_99

**selected_covariate_lags:**
| axis | kind | driver | selected_lags | feature_names |
| --- | --- | --- | --- | --- |
| past | measured | station_1095 | 4 | x_station_1095_lag4 |
| past | measured | station_313 | 4 | x_station_313_lag4 |
| past | measured | station_490 | 4 | x_station_490_lag4 |
| past | measured | station_67 | 5 | x_station_67_lag5 |
| past | measured | station_71 | 4, 6, 8 | x_station_71_lag4, x_station_71_lag6, x_station_71_lag8 |
| past | measured | station_758 | 4, 5, 8, 12 | x_station_758_lag4, x_station_758_lag5, x_station_758_lag8, x_station_758_lag12 |
| past | measured | station_99 | 11 | x_station_99_lag11 |

**covariate_notes:**
- past covariate station_1095: lags [4]
- past covariate station_313: lags [4]
- past covariate station_490: lags [4]
- past covariate station_67: lags [5]
- past covariate station_71: lags [4, 6, 8]
- past covariate station_758: lags [4, 5, 8, 12]
- past covariate station_99: lags [11]

**future_covariates:**
(none)

**calendar_features:**
(none)

**calendar_locale:** None

**rejected_covariates:**
(none)

**target_history_context:**
- enabled: True
- target_lags: [4, 5]
- scorer_name: catt_knn_mi
- normalization_strategy: rank_percentile
- penalized_selected_features: 12
- max_selected_redundancy: 0.8263888888888888
- notes:
- target-history novelty scored with catt_knn_mi over target lags [4, 5]
- 12 selected feature(s) carried non-zero target-history redundancy

## Notes

**caution_flags:**
(none)

**downstream_notes:**
(none)

**transformation_hints:**
(none)

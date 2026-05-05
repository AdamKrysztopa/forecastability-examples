# Forecast Prep Contract

## Metadata

- source_goal: lagged_exogenous
- blocked: False
- readiness_status: clear
- confidence_label: medium
- target_frequency: D
- horizon: 2
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

## Model Families

**recommended_families:**
(none)

**baseline_families:**
- naive
- seasonal_naive

## Covariates

**past_covariates:**
- noise_sensor
- promo_index

**selected_covariate_lags:**
| axis | kind | driver | selected_lags | feature_names |
| --- | --- | --- | --- | --- |
| future | known_future:calendar | calendar_flag | 4 | x_calendar_flag_lag4 |
| past | measured | noise_sensor | 2, 3 | x_noise_sensor_lag2, x_noise_sensor_lag3 |
| past | measured | promo_index | 3 | x_promo_index_lag3 |

**covariate_notes:**
- future covariate calendar_flag: lags [4]
- past covariate noise_sensor: lags [2, 3]
- past covariate promo_index: lags [3]

**future_covariates:**
- calendar_flag

**calendar_features:**
(none)

**calendar_locale:** None

**rejected_covariates:**
(none)

**target_history_context:**
- enabled: True
- target_lags: [2, 4]
- scorer_name: spearman_abs
- normalization_strategy: rank_percentile
- penalized_selected_features: 4
- max_selected_redundancy: 0.7058823529411765
- notes:
- target-history novelty scored with spearman_abs over target lags [2, 4]
- 4 selected feature(s) carried non-zero target-history redundancy

## Notes

**caution_flags:**
(none)

**downstream_notes:**
(none)

**transformation_hints:**
(none)

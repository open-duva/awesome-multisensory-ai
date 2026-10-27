# Benchmarks and evaluation design

[Home](../README.md) · [Datasets](datasets.md) · [Core evaluation papers](../topics/datasets-and-benchmarks.md) · [Research Map](../atlas/dist/index.html)

Twelve selected evaluation suites/resources below measure different abilities. They are not one leaderboard. Results are author-reported; this collection has not rerun the experiments.

| Evaluation resource | Ability and reference | Essential comparison / boundary |
| --- | --- | --- |
| [PaPaGei suite](https://github.com/Nokia-Bell-Labs/papagei-foundation-model) | PPG classification/regression with task-specific measurements/labels and subject-level splits. | Compare generic SSL, pretrained models, and statistical features; device/placement transfer is a separate test. |
| [ECG-FM public task](https://github.com/bowang-lab/ECG-FM) | Public ECG interpretation-related label prediction and data-scaling protocols. | Separate public tasks from private institutional and linked ejection-fraction evaluations. Audit clinical versus machine-generated labels. |
| [TacBench](https://github.com/facebookresearch/sparsh) | Force, slip, pose, tactile properties, and manipulation-related tests. | Use calibrated units where provided; compare frozen encoders, scratch training, and adaptation. Better traversal is not full task completion. |
| [FoTa / T3](https://github.com/alanzjl/t3) | Heterogeneous sensor/task representation and held-out pair evaluation. | Inspect every task/sensor split. Joint training can hurt some combinations; average improvement hides negative transfer. |
| [SensorQA](https://github.com/benjamin-reichman/SensorQA) | Long-duration activity/context QA with human-authored references. | Oracle graphs, predicted graphs, embeddings, and raw sensor inputs are different conditions. Add numeric/time scoring to language overlap. |
| [PHIA queries](https://github.com/yahskapar/personal-health-insights-agent) | Objective wearable calculations and human-rated open-ended answers. | Include deterministic and single-step code baselines; separate synthetic/real users and answer quality from health outcomes. |
| [SensorBench](https://github.com/nesl/LLM_sensor_processing) | Executed filtering, spectral, timing, reconstruction, and feature-extraction tasks. | Numeric/engineering references expose fluent-but-wrong outputs. Findings are tied to tested models and task parameters. |
| [EEG-FM-Compass](https://github.com/Dingkun0817/EEG-FM-Benchmark) | Common downstream regimes for open EEG models and supervised specialists. | Separate leave-one-person-out, within-person calibration, full fine-tuning, and frozen-head tests; audit pretraining overlap. |
| [PPG-Bench](https://github.com/mannas-ai/ppg-bench) | Subject-disjoint nested evaluation, native preprocessing, and simple physiological controls. | A recent independent benchmark with useful negative results; not a timeless verdict on every PPG model or endpoint. |
| [MM-Fi protocols](https://github.com/ybhbingo/MMFi_dataset) | Pose/action tests across synchronized physical modalities with explicit split variants. | Compare random, cross-person, and cross-environment results. Visual pose references are estimates; missing/weak modalities matter. |
| [SenseFi](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) | WiFi CSI model zoo and reproducible task comparisons. | Library breadth is not universal cross-device/site transfer. Keep preprocessing and source-dataset protocols fixed. |
| [SenTSR-Bench](https://github.com/amazon-science/SenTSR-Bench) | Expert industrial diagnostic QA on hourly standardized sensor streams. | Labels for likely causes and fixes do not identify causal mechanisms or prove maintenance benefit. Three questions may share one stream. |

## What the deeper review changes

Model comparisons belong next to model papers. The research map separately records twelve evaluation relations, such as PPG-Bench evaluating PaPaGei and EEG-FM-Compass evaluating LaBraM. These are **evaluations/comparisons, not architecture inheritance or necessarily independent replications**.

[Further reading](watchlist.md) includes OpenSLA's retrospective action tests, physiological/EMG benchmarks, and fault-stress tests. General numerical evaluation such as TSRBench and TimesX can inform controls without becoming a claim about raw physical-sensor intelligence.

## General-encoding protocol comparison

The [forecasting-feature study](../resources/encoder-comparison.md#forecasting-encoders-for-classification) directly tests frozen forecasting representations for classification. It complements the physical suites above and is counted as a background evaluation paper, not a thirteenth physical-sensing benchmark. Its fitted target classifiers, extraction layers, memory fallbacks and author involvement remain explicit.

## Match the claim to its test

| Claimed capability | Minimum useful controls | What the score cannot establish by itself |
| --- | --- | --- |
| Reusable representation | Person/session-disjoint evaluation; specialist and scratch baselines; source-mix ablations | Transfer across a new sensor family |
| Sensor-language alignment | Sensor shuffling; text-only controls; held-out caption templates and labels | Independent physical interpretation beyond the captions |
| Physical state estimation | Independent reference, timing/error units, calibration and device shift | Causal mechanisms or intervention benefit |
| Temporal reasoning | Explicit time/unit scoring; deterministic query baseline; missingness controls | Correct upstream activity/physiology estimates |
| Future prediction | No future-input leakage; specified horizon; matched no-sensor model | Better planning or control |
| Recorded-action prediction | Pre-decision inputs; cohort overlap, policy shift, confounders and prevalence | That a predicted action should be taken |
| Action utility | Executed outcomes; sensor ablations; latency controls; disturbance/failure tests | Reliability across arbitrary platforms or environments |

## Coverage limits

No selected suite establishes universal transfer across PPG, EEG, IMU, touch, and RF with shared metadata, unseen devices, calibrated uncertainty, and action outcomes. Interpret each benchmark within its documented modalities, tasks, and evaluation protocol.

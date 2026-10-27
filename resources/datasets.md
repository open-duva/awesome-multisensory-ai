# Datasets

[Home](../README.md) · [Benchmarks](benchmarks.md) · [Tools](tools.md)

Sixteen physical source datasets, collections, or corpus families, plus one synthetic pretraining control, selected for sensor-aware model research. A dataset's existence does not make it a standardized benchmark: choose a target, independent reference, and leakage-controlled split. Access information was checked on **2026-10-25**; verify the upstream terms before obtaining or redistributing data.

## Health and human sensing

| Dataset | Measurement and reference | Useful capability tests | Access and limitations |
| --- | --- | --- | --- |
| [PPG-DaLiA](https://archive.ics.uci.edu/dataset/495/ppg+dalia) | Wrist PPG and acceleration, with chest ECG for heart-rate reference during everyday activities; other recorded channels are described upstream. | Motion-robust PPG representation, ECG-referenced rate estimation, subject transfer. | Public; UCI lists CC BY 4.0. Small participant cohort and wrist placement do not validate in-ear use. Preserve synchronization and subject boundaries. |
| [WESAD](https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection) | Chest and wrist physiology, including ECG, PPG/BVP, EDA, EMG, respiration, temperature, and motion; experimental conditions and questionnaires. | Multisensor fusion, missing modalities, participant transfer, confounding by activity or protocol. | UCI points to the original dataset for licensing; do not assume the entire UCI catalog has one license. Laboratory stress conditions and self-report are not clinical diagnoses. |
| [PTB-XL v1.0.3](https://physionet.org/content/ptb-xl/1.0.3/) | Clinical 12-lead ECG waveforms with diagnostic, rhythm, and form annotations. | ECG representation, multilabel prediction, reduced-lead adaptation, calibration. | Open access; CC BY 4.0. Use recommended patient-aware folds and document label aggregation. ECG statements are not direct causal labels. |
| [MIMIC-IV-ECG v1.0](https://physionet.org/content/mimic-iv-ecg/1.0/) | Diagnostic ECG waveforms and machine-generated measurements, linkable to a separate clinical database. | Large-scale waveform pretraining, ECG-FM evaluation, clinical-context integration when separately authorized. | This ECG release is open access under ODbL 1.0. Linked clinical data have separate access requirements. Do not confuse open waveforms with unrestricted access to clinical records or reports. |
| [TUH EEG corpus family](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/) | Clinical scalp EEG; TUEG provides the broad corpus, with related TUAB/TUEV resources for abnormality and event labels. | EEG pretraining, event/abnormality classification, channel configuration and cohort transfer. | Registration/access process required; consult each corpus release. Related corpora can overlap: audit participants and recordings across pretraining and evaluation. Counted here as one corpus family. |
| [ExtraSensory](http://extrasensory.ucsd.edu/) | Smartphone/watch motion and contextual sensors; feature-level data and additional raw-measurement resources, with participant activity/context labels. | Sensor-language alignment, activity QA, missingness and placement robustness. | Public research resources under upstream noncommercial terms. Availability differs by sensor and participant; annotations are self-reported context, not independently observed physiology. Source data for SensorQA/SensorChat. |

## Physical interaction

| Dataset | Measurement and reference | Useful capability tests | Access and limitations |
| --- | --- | --- | --- |
| [Ego4D](https://ego4d-data.org/) | Egocentric video with IMU available for a subset, plus other modality-dependent metadata and annotations. | Image/IMU alignment, activity representation, synchronized cross-modal transfer. | License acceptance is required. Inspect modality availability rather than assuming every clip contains IMU. Split participants and recording sessions. |
| [Touch and Go](https://touch-and-go.github.io/) | Egocentric scene video and optical tactile video, timestamps, material labels, and touch onsets. | Visuo-tactile contrastive learning, correspondence, tactile-frame prediction. | Official dataset page provides downloads and CC BY 4.0 notice. Keep object/scene identity from becoming a shortcut. Human exploration is not robot-policy supervision. |
| [ObjectFolder-Real](https://objectfolder.stanford.edu/objectfolder-real-download.html) | Physical recordings of 100 household objects: visual assets, impact sound, and tactile contact videos; impact recordings include force profiles. | Cross-modal object/property representation and transfer between vision, sound, and touch. | Official download instructions verified. Check the project/data terms before redistribution. Object identity, material, striking location, and contact geometry can be confounded; this is the real collection, not its synthetic counterpart. |

## Additional resources from the deeper search

Additional datasets and reusable annotation/evaluation resources are listed below, with their signals, uses, and access conditions.

| Resource | Measurement and annotation source | Useful tests | Access / release boundary |
| --- | --- | --- | --- |
| [TVL](https://huggingface.co/datasets/mlfu7/Touch-Vision-Language-Dataset) | Paired tactile/RGB observations; human labels for part of the data and the test set, many training captions generated by GPT-4V. | Touch-language alignment and description, with human versus generated labels separated. | [Official code](https://github.com/Max-Fu/tvl) recommends [TVL-revise](https://huggingface.co/datasets/yoorhim/TVL-revise) to fix swapped directories. No explicit dataset license found; Apache-2.0 code terms are separate. Released checkpoint statistics differ from the paper. |
| [FoTa / T3](https://huggingface.co/datasets/alanz-mit/FoundationTactile) | Aggregated optical tactile datasets with original object/property/pose labels, plus author-collected robot/force observations. | Sensor/task sharing, held-out sensor-task pairs, negative transfer. | Data card declares MIT; split ZIP and model files are listed. Constituent licenses were not independently reconciled. A viewer error for split archives is not an integrity test. |
| [PhysiCLeAR / Octopi](https://github.com/clear-nus/octopi/tree/master/dataset) | Tactile videos with human ordinal hardness/roughness/bumpiness labels and generated QA templates. | Property-grounded tactile-language tasks; preserve object splits. | Videos and annotation code are visible. No explicit repository/data license located. Present file count differs from the paper's corpus, so pin the revision and split logic. |
| [MM-Fi](https://github.com/ybhbingo/MMFi_dataset) | CSI, radar/LiDAR point clouds, RGB/depth; visual triangulation/optimization for pose, scripted actions and annotated time segments. | Random, cross-person, and cross-environment pose/action evaluations. | Dataset CC BY-NC 4.0. Original RGB access calls for an application; current anonymized-RGB links differ. Follow the terms of the specific release. Pose references contain estimation error; not raw RF IQ. |
| [Sparsh-X data](https://huggingface.co/datasets/facebook/sparsh-x-dataset) | Optical contact images, audio, motion/IMU, and pressure measurements used by the associated encoder. | Complementarity and missing-channel tests across contact evidence. | Official card metadata declares CC BY-NC 4.0; archive inventory visible. Code/model/data terms and completeness remain separate. |
| [Sparsh-skin data](https://huggingface.co/datasets/facebook/sparsh-skin-dataset) | Magnetic tactile skin and kinematic inputs with pretraining and downstream resources. | Full-hand representation, calibrated state/force tasks, downstream policy use. | Public directories verified. No explicit dataset-card license located; do not infer it from the code's CC BY-NC terms. |
| [SenTSR-Bench data](https://huggingface.co/datasets/ZLHe0/SenTSR-Bench) | Hourly standardized industrial acceleration/velocity/temperature readings; expert anomaly/cause/fix questions. | Diagnostic QA and domain-knowledge integration. | Dataset CC BY-NC 4.0; code Apache-2.0. Public 330-row evaluation resource, not the original candidate-stream collection. Plausible causes/fixes are annotations, not tested interventions. |

## Synthetic pretraining control

| Resource | Data source | Useful test | Access / boundary |
| --- | --- | --- | --- |
| [CauKer2M](https://huggingface.co/datasets/paris-noah/CauKer2M) | Two million synthetic sequences generated from kernel/graph compositions; no measured participants or sensor calibration. | Compare synthetic-only pretraining with potentially overlapping real benchmark mixtures. | Official card declares Apache-2.0 and exposes a train split. Full downloads/integrity were not tested. Synthetic causal structure is not validation of a real physical mechanism. See [CauKer](../topics/background.md#cauker). |

## Pairing and measurement checklist

For a useful multisensory experiment, record:

- Sensor model and measurement mechanism; units, channel identity, coordinate frame, placement, and calibration.
- Original sample rates, timestamp source, synchronization error, resampling, filtering, normalization, and missing-data treatment.
- Whether inputs are raw samples, processed waveforms, derived features, event records, or aggregates; report effective temporal bandwidth after preprocessing.
- Who or what supplies the target: a reference instrument, clinician, annotator, self-report, algorithm, or synthetic caption pipeline.
- Split units and overlap: person, session, device, object, environment, and source corpus; include repeated recordings and overlapping windows.
- Consent/access conditions, redistribution terms, and any required citation or data-use agreement.

## Dataset release boundaries

SensorFM and SensorLM's large private wearable cohorts are not listed as downloadable datasets. OpenSLA combines data sources with differing access conditions; follow its [watchlist note](watchlist.md#opensla) rather than treating a model download as a clinical-data release. New tactile papers may depend on external corpora that require additional release and preprocessing checks.

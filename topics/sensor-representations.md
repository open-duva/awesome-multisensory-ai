# Sensor representation and pretraining

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Reusable encoders, calibrated input assumptions, and the boundary between within-family transfer and universal sensor representations.

20 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:limu-bert -->

### LIMU-BERT

**[LIMU-BERT: Unleashing the Potential of Unlabeled Data for IMU Sensing Applications](https://doi.org/10.1145/3485730.3485937)**

Huatao Xu et al. · SenSys 2021. [Status source](https://doi.org/10.1145/3485730.3485937) · [Official implementation](https://github.com/dapowan/LIMU-BERT-Public)

- **Contribution:** Early, compact, reproducible physical-signal pretraining baseline.
- **Measurements and method:** Sample-level IMU; resampled to 20 Hz. Lightweight shared-parameter transformer reconstructs masked spans.
- **Supervision:** Unlabelled signal pretraining; small labelled classifier sets.
- **Demonstrated capability:** Label efficiency, cross-dataset transfer, and mobile inference.
- **Reference / ground truth:** Activity and placement labels from four public datasets.
- **Generalization tested:** Cross-dataset tests; primary split is random nonoverlapping windows (80/10/10), not subject-disjoint.
- **Baselines:** DCNN, DeepSense, transformation-prediction network, raw-input GRU.
- **Boundary:** Classification evidence does not establish odometry or language reasoning; 20 Hz limits bandwidth.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3.3–3.4; 4.1; 4.4; Table 5](https://tanrui.github.io/pub/LIMU_BERT.pdf) · [README; saved/](https://github.com/dapowan/LIMU-BERT-Public)

<!-- paper:oxwearables-ssl -->

### Oxford wearable SSL

**[Self-supervised learning for human activity recognition using 700,000 person-days of wearable data](https://www.nature.com/articles/s41746-024-01062-3)**

Hang Yuan et al. · npj Digital Medicine 7, 91 (2024). [Status source](https://www.nature.com/articles/s41746-024-01062-3) · [Official implementation](https://github.com/OxWearables/ssl-wearables)

- **Contribution:** A practical wearable encoder whose benefit is measured after transfer to external activity datasets.
- **Measurements and method:** Raw wrist acceleration, resampled to 30 Hz in 10-second windows.. 1D ResNet learns time reversal, permutation and time-warp detection with motion-weighted sampling.
- **Supervision:** Unlabeled UK Biobank pretraining; labeled downstream adaptation.
- **Demonstrated capability:** Journal version evaluates eight external datasets, including Parkinsonian motor impairment.
- **Reference / ground truth:** Dataset activity annotations; no clinical diagnostic claim.
- **Generalization tested:** Five device brands, four placement configurations and different populations; subject-wise CV.
- **Baselines:** Same architecture from scratch, engineered-feature random forest, supervised pretraining, SSL ablations.
- **Boundary:** UK pretraining demographics are narrow; labels are still required downstream. Small-dataset classes were filtered; some failed runs select among seeds.
- **Access:** Code, Torch Hub feature extractors and checkpoints provided under an academic-use license; UK Biobank data require application.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2206.02909) · [Methods: Datasets; Evaluation; Discussion; Data availability](https://www.nature.com/articles/s41746-024-01062-3) · [Datasets; Evaluation; Discussion](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11015005/fullTextXML) · [Pretrained models; License](https://github.com/OxWearables/ssl-wearables)

<!-- paper:biot -->

### BIOT

**[BIOT: Biosignal Transformer for Cross-data Learning in the Wild](https://arxiv.org/abs/2305.10351)**

Chaoqi Yang et al. · NeurIPS 2023. [Status source](https://proceedings.neurips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf) · [Official implementation](https://github.com/ycq091044/BIOT)

- **Contribution:** An early reusable solution to heterogeneous sensor formats, with public code and checkpoints; do not imply a single universal multimodal checkpoint.
- **Measurements and method:** waveform transformed into spectral channel patches. Channel-wise spectral tokens plus channel/relative-position embeddings and a linear Transformer.
- **Supervision:** Self-supervised contrastive pretraining; separate supervised and transfer settings.
- **Demonstrated capability:** EEG clinical classification, ECG phenotyping and HAR architecture tests; simulated missing channels/segments.
- **Reference / ground truth:** Clinical EEG and ECG labels; annotated human activities.
- **Generalization tested:** Transfer between datasets with different channel counts and lengths within a signal family.
- **Baselines:** SPaRCNet, ContraWR, CNN-Transformer, FFCL, ST-Transformer; training from scratch.
- **Boundary:** EEG and ECG checkpoints are pretrained separately; the ECG-pretrained models are explicitly not applied to HAR. PREST is proprietary.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Sections 2, 3.1, 3.3-3.6; Table 3 note](https://arxiv.org/html/2305.10351v1) · [Title and proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf) · [README](https://github.com/ycq091044/BIOT) · [Author metadata](https://arxiv.org/abs/2305.10351)

<!-- paper:labram -->

### LaBraM

**[Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://arxiv.org/abs/2405.18765)**

Jiang, Wei-Bang et al. · ICLR 2024. [Status source](https://arxiv.org/abs/2405.18765) · [Official implementation](https://github.com/935963004/LaBraM)

- **Contribution:** Channel-patch tokenization supports transferable EEG representations across recording configurations.
- **Measurements and method:** raw EEG channel patches. Spectrum-prediction VQ tokenizer and masked neural-code prediction.
- **Supervision:** See original manuscript; not independently reproduced.
- **Demonstrated capability:** Abnormality/event/emotion/gait tasks; downstream datasets excluded from pretraining.
- **Reference / ground truth:** Dataset-specific abnormality, EEG-event, emotion-protocol, and gait targets; no single universal physical-state label.
- **Generalization tested:** See demonstrated capability; no untested cross-device or clinical claim inferred.
- **Baselines:** EEG-specialist models and BIOT-style published evaluation protocols; downstream datasets excluded from pretraining.
- **Boundary:** Independent EEG benchmarks show variable gains versus supervised specialists.
- **Access:** official code, preprocessing instructions, and pretrained-model links. Some source EEG corpora require registration or separate agreements.

**Evidence locations:** [History and journal reference](https://arxiv.org/abs/2405.18765) · [Section 3 Model Architecture](https://arxiv.org/html/2504.19596v1) · [Benchmark results](https://doi.org/10.1093/nsr/nwag466)

<!-- paper:siamquality -->

### SiamQuality

**[SiamQuality: a ConvNet-based foundation model for photoplethysmography signals](https://pmc.ncbi.nlm.nih.gov/articles/PMC11334241/)**

Cheng Ding et al. · Physiological Measurement 45(8):085004 (2024). [Status source](https://doi.org/10.1088/1361-6579/ad6747) · [Official implementation](https://github.com/chengding0713/SiamQuality)

- **Contribution:** Uses real signal degradation as a learning signal and reports where artifact-robust learning still fails.
- **Measurements and method:** 30-second waveform segments at 40 Hz; quality scores guide pretraining pairs.. SimSiam-style shared CNN aligns nearby clean/noisy segments; curriculum increases quality difference.
- **Supervision:** Unlabeled waveform consistency with pretrained quality-model guidance; supervised downstream tuning.
- **Demonstrated capability:** Six external datasets across HR, BP, respiratory rate and AF; artifact-tolerance curves.
- **Reference / ground truth:** Dataset physiological references and AF labels; quality labels are model-derived.
- **Generalization tested:** Private ICU pretraining transferred to public clinical/wearable datasets; requires task tuning.
- **Baselines:** Matched SSL backbones/objectives; temporal-pairing and quality/curriculum ablations.
- **Boundary:** Physiology may change within the five-minute pairing window. PVC failure reported at F1 0.52; filtered-test comparisons are not equivalent.
- **Access:** Official source code visible; no published weight file or reuse license found in inspected tree. Pretraining data require author request.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2404.17667) · [Sections 2.3, 3.1–3.5, limitations and reproducibility](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11334241/fullTextXML) · [Publication metadata and data availability](https://pmc.ncbi.nlm.nih.gov/articles/PMC11334241/) · [Repository tree](https://github.com/chengding0713/SiamQuality)

<!-- paper:t3 -->

### T3

**[Transferable Tactile Transformers for Representation Learning Across Diverse Sensors and Tasks](https://arxiv.org/abs/2406.13640)**

Zhao, Jialiang et al. · CoRL 2024; PMLR proceedings 2025. [Status source](https://proceedings.mlr.press/v270/zhao25c.html) · [Official implementation](https://github.com/alanzjl/t3)

- **Contribution:** Important heterogeneous-training architecture and reusable FoTa benchmark, with unusually explicit negative transfer results.
- **Measurements and method:** Sensor-specific tactile images. Sensor encoders and task decoders share a transformer trunk; FoTa aggregates over three million samples.
- **Supervision:** Masked reconstruction followed by supervised task learning.
- **Demonstrated capability:** Held-out sensor-task pairings and three physical insertion parts.
- **Reference / ground truth:** Dataset task labels and insertion within a 30-step limit.
- **Generalization tested:** Unseen pairings of known sensors/tasks; small-data adaptation.
- **Baselines:** Scratch/pretraining ablations, vision-only and scratch tactile policies.
- **Boundary:** Zero-shot classification barely exceeds random guessing; two sensors dominate the corpus; per-image encoder.
- **Access:** Official FoTa card lists split archives and models and declares MIT. Viewer inability to open split ZIP files is not proof that the archive is corrupt. Complete download/integrity not tested.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2406.13640) · [Sections 3–6; Appendix A](https://arxiv.org/html/2406.13640v2) · [Publication/project record](https://t3.alanz.info/) · [README / linked implementation](https://github.com/alanzjl/t3)

<!-- paper:ecg-fm -->

### ECG-FM

**[ECG-FM: an open electrocardiogram foundation model](https://arxiv.org/abs/2408.05178)**

McKeen, Kaden et al. · JAMIA Open 2025. [Status source](https://academic.oup.com/jamiaopen/article/8/5/ooaf122/8287827) · [Official implementation](https://github.com/bowang-lab/ECG-FM)

- **Contribution:** Open ECG representations with checkpoints, a public task, and explicit label-efficiency comparisons.
- **Measurements and method:** raw 12-lead ECG windows. WCR: wav2vec 2.0 signal masking, CLOCS-derived CMSC and random lead masking, adopted through fairseq-signals.
- **Supervision:** See original manuscript; not independently reproduced.
- **Demonstrated capability:** Low-label ECG labels and reduced-LVEF prediction; public MIMIC benchmark and institutional transfer.
- **Reference / ground truth:** Clinical/machine-generated ECG interpretation labels and linked ejection-fraction measurements; public and private task cohorts differ.
- **Generalization tested:** See demonstrated capability; no untested cross-device or clinical claim inferred.
- **Baselines:** Supervised ResNet-based and SE-WRN ECG models, with fixed validation/test sets under label scaling.
- **Boundary:** Report-derived labels and whole-record labels applied to segments; private cohort not fully reproducible.
- **Access:** official preprocessing, configurations, public checkpoint links, and a MIMIC-IV-ECG benchmark. Use the revised manuscript when checking cohort sizes; early abstracts differ.

**Evidence locations:** [Publication history; Discussion](https://academic.oup.com/jamiaopen/article/8/5/ooaf122/8287827) · [Section 2.4](https://arxiv.org/html/2408.05178v2) · [Model; Quick start](https://github.com/bowang-lab/ECG-FM)

<!-- paper:gluformer -->

### GluFormer

**[A foundation model for continuous glucose monitoring data](https://www.nature.com/articles/s41586-025-09925-9)**

Guy Lutsker et al. · Nature 2026. [Status source](https://www.nature.com/articles/s41586-025-09925-9) · [Official implementation](https://github.com/Guylu/GluFormer)

- **Contribution:** Adds a chemical sensor modality and unusually broad cohort/device transfer, with explicit reference measurements.
- **Measurements and method:** direct glucose concentration series; optional meal records. Glucose-value discretization and autoregressive Transformer; frozen embeddings feed ridge predictors; optional dietary tokens.
- **Supervision:** Self-supervised next-token prediction, with downstream clinical targets.
- **Demonstrated capability:** Clinical-measure prediction, longitudinal risk ranking, glucose generation and meal-response prediction.
- **Reference / ground truth:** Measured HbA1c and other clinical variables, incident diagnoses and mortality; recorded glucose trajectories.
- **Generalization tested:** 19 external cohorts spanning five countries and eight CGM devices; downstream supervised probes should not be called zero-shot clinical diagnosis.
- **Baselines:** HbA1c, GMI and other CGM summaries; matched non-pretrained Transformer/CNN ablations in preprint.
- **Boundary:** Predominantly non-diabetic pretraining and observational risk analyses. Trial-outcome prediction is not validated treatment selection. Public code does not establish unrestricted pretrained-weight access.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [History](https://arxiv.org/abs/2408.11876) · [Methods pp.29-41](https://arxiv.org/pdf/2408.11876v2) · [Abstract and publication metadata](https://www.nature.com/articles/s41586-025-09925-9) · [README; repository structure](https://github.com/Guylu/GluFormer) · [Author metadata](https://api.crossref.org/works/10.1038%2Fs41586-025-09925-9)

<!-- paper:ecgfounder -->

### ECGFounder

**[An Electrocardiogram Foundation Model Built on over 10 Million Recordings](https://doi.org/10.1056/AIoa2401033)**

Jun Li et al. · NEJM AI 2(7), AIoa2401033 (2025). [Status source](https://doi.org/10.1056/AIoa2401033) · [Official implementation](https://github.com/PKUDigitalHealth/ECGFounder)

- **Contribution:** A clinical-label-pretrained ECG encoder that transfers across lead settings and provides the frozen teacher for AnyPPG.
- **Measurements and method:** Filtered, per-segment standardized cardiac waveforms; separate 12-lead and single-lead models.. Net1D/RegNet backbone with multilabel positive-unlabeled loss and limb-lead augmentation.
- **Supervision:** Parsed clinical ECG diagnoses; downstream labels for probing/fine-tuning.
- **Demonstrated capability:** External ECG diagnosis on CODE-test/PTB-XL and AliveCor recordings; MIMIC clinical tasks and PPG AF adaptation.
- **Reference / ground truth:** Clinical/expert diagnostic labels, linked clinical measurements and downstream rhythm labels.
- **Generalization tested:** Geographic/database shift and one portable-device corpus; MIMIC/PPG results include target-data adaptation.
- **Baselines:** S12L-ECG, CTN, ECG-SE-ResNet, ECG-SimCLR and task-specific comparisons; training corpora differ.
- **Boundary:** U.S.-heavy development; small expert-review subset; continuous-target systematic bias. Cloud execution is not on-device deployment; no prospective clinical-benefit test.
- **Access:** MIT code and MIT-tagged public Hugging Face 1-lead/12-lead checkpoints verified by metadata/file listing. Exact preprocessing required; full training-data access and model execution not verified.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2410.04133) · [Front matter; Methods; Results Tables 2–4; Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC12327759/) · [Publication record](https://pubmed.ncbi.nlm.nih.gov/40771651/) · [README; LICENSE; dataset.py](https://github.com/PKUDigitalHealth/ECGFounder) · [Model card and file listing](https://huggingface.co/PKUDigitalHealth/ECGFounder) · [private/gated/cardData/siblings](https://huggingface.co/api/models/PKUDigitalHealth/ECGFounder) · [Section 4.3; Figure 2](https://arxiv.org/html/2511.01747v4)

<!-- paper:papagei -->

### PaPaGei

**[PaPaGei: Open Foundation Models for Optical Physiological Signals](https://arxiv.org/abs/2410.20542)**

Pillai, Arvind et al. · ICLR 2025. [Status source](https://arxiv.org/abs/2410.20542) · [Official implementation](https://github.com/Nokia-Bell-Labs/papagei-foundation-model)

- **Contribution:** Morphology-aware PPG representations, public weights, and evaluation across distinct datasets.
- **Measurements and method:** preprocessed raw PPG. Morphology-aware contrastive learning with ResNet variants.
- **Supervision:** See original manuscript; not independently reproduced.
- **Demonstrated capability:** 20 tasks in ten datasets, including cross-dataset transfer and skin-tone analysis.
- **Reference / ground truth:** Task-specific physiological reference measurements and source-dataset condition labels; validity differs by endpoint.
- **Generalization tested:** See demonstrated capability; no untested cross-device or clinical claim inferred.
- **Baselines:** Statistical features; SimCLR, BYOL and TF-C; REGLE, Chronos and MOMENT.
- **Boundary:** Clinical/motion-poor pretraining limits field transfer; independent PPG-Bench questions consistent gains. Archived repository remains usable, not actively maintained.
- **Access:** official code and linked model weights; upstream datasets retain separate terms. The official repository is archived as of this review.

**Evidence locations:** [Abstract; history](https://arxiv.org/abs/2410.20542) · [Updates; header; weights](https://github.com/Nokia-Bell-Labs/papagei-foundation-model) · [Results](https://arxiv.org/html/2610.13435v1)

<!-- paper:sparsh -->

### Sparsh

**[Sparsh: Self-supervised touch representations for vision-based tactile sensing](https://arxiv.org/abs/2410.24090)**

Higuera, Carolina et al. · CoRL 2024; proceedings published 2025. [Status source](https://proceedings.mlr.press/v270/higuera25a.html) · [Official implementation](https://github.com/facebookresearch/sparsh)

- **Contribution:** Reusable optical-touch encoders evaluated against physical references and task-specific training.
- **Measurements and method:** Tactile images or short stacked frames. Masked reconstruction, self-distillation and JEPA family.
- **Supervision:** Unlabeled pretraining; supervised probes.
- **Demonstrated capability:** Six tactile tasks; planning experiment includes failures.
- **Reference / ground truth:** Instrumented three-axis force and task-specific slip, pose, textile, grasp, and traversal references.
- **Generalization tested:** Multiple optical sensors and downstream tasks.
- **Baselines:** Task-specific end-to-end learning, alternate SSL objectives, and low-label adaptation.
- **Boundary:** Optical-only; broad numerical averages hide task differences; bead-maze manipulation remains weak.
- **Access:** official code, checkpoints, and benchmark-data instructions. The original repository is archived; review its license and the constituent datasets separately.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2410.24090) · [Sections 3–8; Appendix D](https://arxiv.org/html/2410.24090v1)

<!-- paper:cbramod -->

### CBraMod

**[CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding](https://arxiv.org/abs/2412.07236)**

Jiquan Wang et al. · ICLR 2025. [Status source](https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html) · [Official implementation](https://github.com/wjq-learning/CBraMod)

- **Contribution:** A compact EEG alternative with explicit spatial/temporal structure and external benchmark support.
- **Measurements and method:** Filtered EEG patches with time/frequency features; common-channel pretraining at 200 Hz.. Separate spatial/temporal criss-cross attention and conditional positional encoding reconstruct masked patches.
- **Supervision:** Unlabeled cleaned TUEG; labeled downstream fine-tuning.
- **Demonstrated capability:** Twelve datasets across ten BCI tasks; independent EEG-FM-Compass comparison.
- **Reference / ground truth:** Dataset task labels, clinical annotations and vigilance references.
- **Generalization tested:** Variable montages and tasks; dataset-specific adaptation/splits, plus independent LOSO/few-shot protocols.
- **Baselines:** BIOT/LaBraM and scratch specialists; architecture, data-quality and pretraining controls.
- **Boundary:** Filtering substantially reduces the raw archive. Independent benchmark ranks it strongly among FMs while specialists remain competitive.
- **Access:** MIT code and a Hugging Face pretrained weight entry verified; underlying EEG datasets have separate access conditions.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2412.07236) · [Sections 2–3; Appendices D/E/G/Q/S](https://arxiv.org/html/2412.07236v3) · [Benchmark results; specialist comparison; Figure 6](https://doi.org/10.1093/nsr/nwag466) · [Pretrain; Fine-tune; License](https://github.com/wjq-learning/CBraMod) · [File listing](https://huggingface.co/weighting666/CBraMod/tree/main) · [Abstract, comments and history](https://arxiv.org/abs/2412.07236) · [Benchmark results](https://doi.org/10.1093/nsr/nwag466)

<!-- paper:pulse-ppg -->

### Pulse-PPG

**[Pulse-PPG: An Open-Source Field-Trained PPG Foundation Model for Wearable Applications Across Lab and Field Settings](https://arxiv.org/abs/2502.01108)**

Mithun Saha et al. · ACM IMWUT / UbiComp 2025. [Status source](https://dl.acm.org/doi/10.1145/3749494) · [Official implementation](https://github.com/maxxu05/pulseppg)

- **Contribution:** Complements clean-clinical PPG pretraining with a reusable field-trained encoder and informative failure analysis.
- **Measurements and method:** raw wearable PPG with field artifacts. Contrastive representation learning using a learned motif-similarity distance on uncurated field recordings.
- **Supervision:** Self-supervised field pretraining; frozen supervised probes.
- **Demonstrated capability:** Wearable and clinical tasks, including activity, stress, heart rate and blood-pressure endpoints; field-versus-clinical pretraining ablations.
- **Reference / ground truth:** Dataset-specific activity, self-report and physiological reference labels; field stress has model-assisted sampling caveats.
- **Generalization tested:** Held-out users and several clinical/lab/field datasets; parameter/window-matched lightweight ablation.
- **Baselines:** PaPaGei-S, Chronos, MOMENT and supervised models.
- **Boundary:** Sleep-disorder task is weaker than PaPaGei; no sleep during field pretraining. Skin-tone metadata absent. Author-controlled evaluation does not establish universal superiority.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Sections 3, 6-8; Appendix A.2](https://arxiv.org/html/2502.01108v2) · [README; License](https://github.com/maxxu05/pulseppg) · [Author metadata](https://api.crossref.org/works/10.1145%2F3749494)

<!-- paper:sleepfm-clinical -->

### SleepFM clinical

**[A multimodal sleep foundation model for disease prediction](https://www.nature.com/articles/s41591-025-04133-4)**

Rahul Thapa et al. · Nature Medicine 2026. [Status source](https://www.nature.com/articles/s41591-025-04133-4) · [Official implementation](https://github.com/zou-group/sleepfm-clinical)

- **Contribution:** Strong multimodal waveform example with independent clinical references, external transfer and released checkpoints/data access instructions.
- **Measurements and method:** preprocessed raw PSG waveforms. 5-second waveform tokens, channel-agnostic attention pooling, temporal Transformer and leave-one-out contrastive alignment.
- **Supervision:** Self-supervised paired modalities; downstream sleep labels and EHR outcomes.
- **Demonstrated capability:** Sleep staging, apnea, age/sex and longitudinal disease-risk ranking across clinical cohorts.
- **Reference / ground truth:** Expert sleep/apnea annotations; EHR diagnoses and follow-up outcomes.
- **Generalization tested:** Temporal SSC test and external SHHS, which is excluded from pretraining but receives downstream fine-tuning.
- **Baselines:** Demographics; same-architecture supervised PSG model; U-Sleep/YASA and other staging specialists.
- **Boundary:** Referral-clinic selection and EHR ascertainment limit population claims. SHHS is transfer learning, not zero-shot clinical validation; prospective intervention benefit untested.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Methods; Table 1; Discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC12920147/) · [News & Updates; Usage](https://github.com/zou-group/sleepfm-clinical) · [Preprint record](https://pubmed.ncbi.nlm.nih.gov/39974074/) · [Author metadata](https://pmc.ncbi.nlm.nih.gov/articles/PMC12920147/)

<!-- paper:sparsh-skin -->

### Sparsh-skin

**[Self-supervised perception for tactile skin covered dexterous hands](https://arxiv.org/abs/2505.11420)**

Sharma, Akash et al. · CoRL 2025. [Status source](https://github.com/facebookresearch/sparsh-multisensory-touch) · [Official implementation](https://github.com/facebookresearch/sparsh-multisensory-touch)

- **Contribution:** Fills the non-optical full-hand gap with raw signal learning, measured references and usable released assets.
- **Measurements and method:** 100 ms raw magnetic-flux windows plus kinematics-derived taxel coordinates. Spatiotemporal tokenization of 368 taxels and positions; masked self-distillation.
- **Supervision:** About four hours of play; supervised downstream probes and imitation learning.
- **Demonstrated capability:** Force, joystick, object pose and real plug insertion.
- **Reference / ground truth:** F/T probe, joystick state, ArUco pose, physical completion.
- **Generalization tested:** Label-budget transfer on one Allegro/Xela setup; not arbitrary-hand transfer.
- **Baselines:** Same-capacity end-to-end, BYOL, MAE, HiSS on applicable task.
- **Boundary:** Shear estimates are less accurate than normal force; insertion failures include grip loss; hand/sensor transfer untested.
- **Access:** Official code and public pretraining/downstream data directories. The data card lacks an explicit license; the code license should not be assumed to license the data.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2505.11420) · [Sections 3–4; Appendix B](https://arxiv.org/html/2505.11420v1) · [Publication/project record](https://github.com/facebookresearch/sparsh-multisensory-touch) · [README / linked implementation](https://github.com/facebookresearch/sparsh-multisensory-touch)

<!-- paper:sparsh-x -->

### Sparsh-X

**[Tactile Beyond Pixels: Multisensory Touch Representations for Robot Manipulation](https://arxiv.org/abs/2506.14754)**

Higuera, Carolina et al. · CoRL 2025 (oral). [Status source](https://akashsharma02.github.io/sparsh-x-ssl/) · [Official implementation](https://github.com/facebookresearch/sparsh-multisensory-touch)

- **Contribution:** A reusable encoder combines optical touch, contact audio, motion, and pressure.
- **Measurements and method:** Tactile images, log-mel audio and sampled numeric time series. Teacher-student masked self-distillation with bottleneck fusion of four physical channels.
- **Supervision:** Unlabeled contact interactions; task-specific supervised heads and policies.
- **Demonstrated capability:** Plug insertion and in-hand rotation, plus material/quantity and normal-force tests.
- **Reference / ground truth:** Force probe, property labels, robot task outcomes; not all are calibrated continuous properties.
- **Generalization tested:** Task/data-budget transfer within Digit 360 hardware.
- **Baselines:** Modality ablations; end-to-end image-only and multisensory models.
- **Boundary:** Normal-force experiment uses one probe geometry; no shear-force evaluation. Limited optical device diversity.
- **Access:** Official training/evaluation code, weight links and a public dataset directory; the Hugging Face dataset metadata declares CC BY-NC 4.0. Large archives were not downloaded.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2506.14754) · [Sections 3–5; Limitations; Appendices A–C](https://arxiv.org/html/2506.14754v1) · [Publication/project record](https://akashsharma02.github.io/sparsh-x-ssl/) · [README / linked implementation](https://github.com/facebookresearch/sparsh-multisensory-touch)

<!-- paper:tinymyo -->

### TinyMyo

**[TinyMyo: a Tiny Foundation Model for Flexible EMG Signal Processing at the Edge](https://arxiv.org/abs/2512.15729)**

Matteo Fasulo et al. · IEEE Transactions on Biomedical Engineering 2026 (early access). [Status source](https://doi.org/10.1109/TBME.2026.3736157) · [Official implementation](https://github.com/pulp-bio/BioFoundation)

- **Contribution:** Rare combination of multimodal-adjacent biosignal transfer and concrete embedded measurements, with public implementation and model card.
- **Measurements and method:** raw surface-EMG waveforms. Channel-independent patches, rotary Transformer and masked reconstruction; small task heads and integer deployment.
- **Supervision:** Self-supervised public-data pretraining, supervised task adaptation.
- **Demonstrated capability:** Gesture classification, kinematic regression, silent-speech production/recognition; GAP9 hardware latency and energy measured.
- **Reference / ground truth:** Gesture labels, motion references and speech targets; hardware timing/power measurements.
- **Generalization tested:** Multiple acquisition configurations and tasks; UCI subject-disjoint split. NinaPro uses repetitions within subjects, not unseen-subject validation.
- **Baselines:** MOMENT, OTIS, PhysioWave, WaveFormer and task-specific systems.
- **Boundary:** Main 3.6M variant takes 0.785 s per inference; this alone is not low-latency closed-loop control. Published metrics differ from arXiv v2; avoid mixing them.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [III-A/III-B; IV; Table II](https://arxiv.org/html/2512.15729v2) · [Publication and abstract](https://pubmed.ncbi.nlm.nih.gov/42785278/) · [Model table](https://github.com/pulp-bio/BioFoundation) · [Author metadata](https://api.crossref.org/works/10.1109%2FTBME.2026.3736157)

<!-- paper:osf -->

### OSF

**[OSF: On Pre-training and Scaling of Sleep Foundation Models](https://proceedings.mlr.press/v306/shuai26a.html)**

Zitao Shuai et al. · ICML 2026. [Status source](https://proceedings.mlr.press/v306/shuai26a.html) · [Official implementation](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM)

- **Contribution:** Channel-invariant pretraining is tested under missing sensors and external-cohort adaptation.
- **Measurements and method:** Standardized 12-channel PSG, 30-second epochs at 64 Hz; missing channels zero-padded.. DINO-style self-distillation with channel/time masking; controlled objective and scaling comparisons.
- **Supervision:** Unlabeled pretraining; labeled probes and fine-tuning.
- **Demonstrated capability:** Sleep staging/events, missing-channel tests, disease-label classification and regression.
- **Reference / ground truth:** Cohort sleep annotations; disease histories/medications; heart-rate reference for regression.
- **Generalization tested:** Four cohorts excluded from pretraining; target probes still train on target labels.
- **Baselines:** Matched-backbone SleepFM, SimCLR, DINO, MAE, VQ-VAE, AR and supervised ViT.
- **Boundary:** Not uniformly best: reconstruction objectives improve heart-rate regression. Channel removal tests and retrospective disease labels do not establish deployment benefit.
- **Access:** MIT code and OSF-Base weight entry verified. Source datasets require access; preprocessing remains promised.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2603.00190) · [Publication record](https://proceedings.mlr.press/v306/shuai26a.html) · [Sections 2–6; Appendix B.1–B.3; Table 33](https://arxiv.org/html/2603.00190v2) · [News; Weights; SleepBench; License](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM) · [File listing](https://huggingface.co/yang-ai-lab/OSF-Base/tree/main) · [Submission history](https://arxiv.org/abs/2603.00190) · [2–4; Appendix B.1–B.3; Table 33](https://arxiv.org/html/2603.00190v2) · [News; Pretrained Weights; SleepBench; License](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM) · [News](https://yang-ai-lab.github.io/osf/) · [Appendix C.1; reference 31](https://arxiv.org/html/2610.08244)

<!-- paper:anytouch2 -->

### AnyTouch 2

**[AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception](https://arxiv.org/abs/2602.09617)**

Feng, Ruoxuan et al. · ICLR 2026. [Status source](https://arxiv.org/abs/2602.09617) · [Official implementation](https://github.com/GeWu-Lab/AnyTouch2)

- **Contribution:** Connects semantic tactile pretraining to measured dynamics, with data/model releases and controlled physical-supervision ablations.
- **Measurements and method:** Background-subtracted tactile sequences; measured forces during training. Frame and frame-difference reconstruction, multimodal/cross-sensor matching, force and delta-force heads.
- **Supervision:** Mixed self-supervision, alignment and measured-force supervision on ToucHD plus prior datasets.
- **Demonstrated capability:** Offline physical probes and four real manipulation tasks, including USB insertion and chip movement.
- **Reference / ground truth:** Wrist force sensor, task/property labels and robot task outcomes.
- **Generalization tested:** Several optical sensors; unseen indenters and gel replacement tests.
- **Baselines:** UniTouch, T3, Sparsh variants and AnyTouch; data-matched MAE included.
- **Boundary:** Force collection uses simplified indenter interactions; some collected sensors are unused. Alignment removal improves some force metrics.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2602.09617) · [Sections 3–5; Appendices 15–19](https://arxiv.org/html/2602.09617v1) · [README / linked implementation](https://github.com/GeWu-Lab/AnyTouch2) · [Comments / acceptance status](https://arxiv.org/abs/2602.09617)

<!-- paper:csfm -->

### CSFM

**[Cardiac health assessment across scenarios and devices using a multimodal foundation model pretrained on data from 1.7 million individuals](https://www.nature.com/articles/s42256-026-01180-5)**

Xiao Gu et al. · Nature Machine Intelligence 2026. [Status source](https://www.nature.com/articles/s42256-026-01180-5) · [Official implementation](https://github.com/guxiao0822/Cardiac-Sensing-FM)

- **Contribution:** Strong complementary ECG/PPG integration with heterogeneous-input evaluation and independent BP reference; disclose access restrictions prominently.
- **Measurements and method:** waveform and clinical/machine-generated report embeddings. Masked channel/time modeling across heterogeneous cardiac recordings with text representations; dense heads for waveform outputs.
- **Supervision:** Self-supervised masked pretraining plus supervised downstream tasks.
- **Demonstrated capability:** Reduced-lead diagnosis, vital-sign estimation, mortality/alarm prediction, ECG QA and cross-signal reconstruction.
- **Reference / ground truth:** ECG annotations, arterial BP traces, clinical outcomes and benchmark QA labels.
- **Generalization tested:** Cross-dataset/device/input configurations; subject-wise splits; reduced-lead adaptation.
- **Baselines:** Domain features (NeuroKit2/pyPPG), supervised models and open foundation models.
- **Boundary:** Private CODE data limit full reproduction. Weights require a signed Academic Access Agreement. Synthesized waveforms are estimates, not replacement measurements.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Results; Methods; Discussion](https://www.nature.com/articles/s42256-026-01180-5) · [Download the Pretrained Model Weights](https://github.com/guxiao0822/Cardiac-Sensing-FM) · [Author metadata](https://api.crossref.org/works/10.1038%2Fs42256-026-01180-5)

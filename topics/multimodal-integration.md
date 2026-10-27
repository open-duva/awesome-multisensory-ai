# Multimodal alignment and integration

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Ways to connect physical measurements to language and other modalities. Shared embeddings and fluent output do not by themselves establish physical-state accuracy.

15 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:imu2clip -->

### IMU2CLIP

**[IMU2CLIP: Language-grounded Motion Sensor Translation with Multimodal Contrastive Learning](https://aclanthology.org/2023.findings-emnlp.883/)**

Seungwhan Moon et al. · Findings of EMNLP 2023. [Status source](https://aclanthology.org/2023.findings-emnlp.883/) · [Official implementation](https://github.com/facebookresearch/imu2clip)

- **Contribution:** Clear early IMU-to-language bridge with controlled pretraining comparison.
- **Measurements and method:** Six-axis sampled IMU; egocentric video and narrations. CNN/GRU IMU encoder contrastively aligned to frozen CLIP space.
- **Supervision:** Paired recordings and narrations; downstream activity labels.
- **Demonstrated capability:** Retrieval and probing/fine-tuning gains against the same randomly initialized encoder.
- **Reference / ground truth:** Paired windows and activity labels in Ego4D and Aria.
- **Generalization tested:** Video-ID splits; new device/domain transfer explicitly unanswered.
- **Baselines:** Same architecture without pretraining; CLIP video retrieval; alignment variants.
- **Boundary:** Sensor-log question answering is qualitative only; code archived July 17, 2025.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3–4; 6 Limitations](https://aclanthology.org/2023.findings-emnlp.883.pdf) · [README and archive banner](https://github.com/facebookresearch/imu2clip)

<!-- paper:touch-and-go -->

### Touch and Go

**[Touch and Go: Learning from Human-Collected Vision and Touch](https://arxiv.org/abs/2211.12498)**

Yang, Fengyu et al. · NeurIPS 2022 Datasets and Benchmarks. [Status source](https://papers.nips.cc/paper_files/paper/2022/file/354892587fe39b17c2b727af02abff4a-Paper-Datasets_and_Benchmarks.pdf) · [Official implementation](https://github.com/fredfyyang/Touch-and-Go)

- **Contribution:** A paired in-the-wild vision/touch resource that enables subsequent representation studies.
- **Measurements and method:** Synchronized RGB and GelSight videos. Human-collected probing with cross-modal representation and prediction baselines.
- **Supervision:** Paired streams and material labels.
- **Demonstrated capability:** Representation, stylization and tactile future prediction.
- **Reference / ground truth:** Observed tactile frames and annotated materials.
- **Generalization tested:** Varied natural scenes; video-level splits matter.
- **Baselines:** Task-specific unimodal/multimodal comparisons.
- **Boundary:** Split by recording video to avoid adjacent-frame leakage; inferred material labels can be noisy.
- **Access:** official code and [dataset project](https://touch-and-go.github.io/). This paper also appears in the dataset index; it is counted once in the bibliography.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2211.12498) · [Datasheet Q12–Q20](https://papers.neurips.cc/paper_files/paper/2022/file/354892587fe39b17c2b727af02abff4a-Supplemental-Datasets_and_Benchmarks.pdf)

<!-- paper:imagebind -->

### ImageBind

**[ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665)**

Girdhar, Rohit et al. · CVPR 2023. [Status source](https://arxiv.org/abs/2305.05665) · [Official implementation](https://github.com/facebookresearch/ImageBind)

- **Contribution:** An image-paired bridge connects IMU to other modalities without every modality pair being observed.
- **Measurements and method:** Not inspected. Modality-specific encoders are aligned through image-paired contrastive learning. A shared image space connects text, audio, depth, thermal and IMU without training every modality pair.
- **Supervision:** Naturally paired observations plus pretrained image-text representations; the added sensor modalities do not require direct text pairing for every task.
- **Demonstrated capability:** Zero-shot recognition, cross-modal retrieval, few-shot adaptation and compositional embedding applications; IMU evaluation includes Ego4D scenario classification.
- **Reference / ground truth:** Benchmark category labels and paired retrieval targets; these are semantic references rather than calibrated acceleration or latent physical-state measurements.
- **Generalization tested:** Emergent cross-modal combinations and held-out benchmark tasks/examples. This does not establish arbitrary device transfer or calibrated physical inference.
- **Baselines:** Modality specialists and prior cross-modal models, with text-paired and supervised references where available; encoder-scale and training ablations.
- **Boundary:** Image-paired alignment inherits the coverage of its pairing data. Semantic recognition/retrieval does not establish physical-state calibration, causal understanding, or executed control.
- **Access:** official code and pretrained models; inspect the model license and each training dataset's access conditions.

**Evidence locations:** [Sections 3–4; Tables 1–3; modality and architecture details](https://arxiv.org/abs/2305.05665) · [Official implementation and models](https://github.com/facebookresearch/ImageBind)

<!-- paper:onellm -->

### OneLLM

**[OneLLM: One Framework to Align All Modalities with Language](https://arxiv.org/abs/2312.03700)**

Han, Jiaming et al. · CVPR 2024. [Status source](https://arxiv.org/abs/2312.03700) · [Official implementation](https://github.com/csuhan/OneLLM)

- **Contribution:** Reusable unified architecture spanning IMU and brain sensing.
- **Measurements and method:** Modality tokens; measured IMU/fMRI, alongside visual and derived depth inputs. Frozen CLIP vision transformer; modality tokenizers; routed projection experts; LLaMA2.
- **Supervision:** Paired captions followed by multimodal instruction tuning.
- **Demonstrated capability:** Broad QA/captioning benchmarks; scarce-modality joint-training ablations.
- **Reference / ground truth:** Ego4D narrations and NSD stimulus captions for sensor branches.
- **Generalization tested:** Held-out benchmark examples; sensor experiments primarily captioning.
- **Baselines:** Specialist MLLMs; joint versus separate alignment and encoder ablations.
- **Boundary:** Twenty-five benchmarks do not mean twenty-five physical-sensor validations; depth/normal training maps are generated.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3; 4; Appendix C–D](https://arxiv.org/html/2312.03700v2) · [README](https://github.com/csuhan/OneLLM)

<!-- paper:unitouch -->

### UniTouch

**[Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://arxiv.org/abs/2401.18084)**

Yang, Fengyu et al. · CVPR 2024. [Status source](https://arxiv.org/abs/2401.18084) · [Official implementation](https://github.com/cfeng16/UniTouch)

- **Contribution:** An image-bridged representation connects optical touch with language and other modalities.
- **Measurements and method:** Tactile images aligned to frozen multimodal features. Sensor-specific tokens and image-pivot contrastive alignment to ImageBind.
- **Supervision:** Paired visual/tactile data; pretrained multimodal supervision.
- **Demonstrated capability:** Recognition, retrieval and generation/LLM applications.
- **Reference / ground truth:** Dataset labels and matched sensory pairs.
- **Generalization tested:** Several optical sensors; cross-modal transfer through image pivot.
- **Baselines:** Single-sensor training and prior tactile representations.
- **Boundary:** Grasp-stability prediction is offline outcome prediction, not executed grasp control; generated touch need not be calibrated.
- **Access:** official implementation and [project page](https://cfeng16.github.io/UniTouch/), with model-use instructions. Verify repository and checkpoint permissions directly; a public GitHub repository alone does not grant a reuse license.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2401.18084) · [Sections 3–5; Appendix A](https://arxiv.org/html/2401.18084v1)

<!-- paper:tvl -->

### TVL

**[A Touch, Vision, and Language Dataset for Multimodal Alignment](https://arxiv.org/abs/2402.13232)**

Fu, Letian et al. · ICML 2024. [Status source](https://tactile-vlm.github.io/) · [Official implementation](https://github.com/Max-Fu/tvl)

- **Contribution:** Foundational open tri-modal dataset and reproducible alignment baseline with explicit annotation provenance.
- **Measurements and method:** DIGIT images and RGB; human/pseudo text labels. CLIP-aligned tactile encoder; tactile-conditioned LLaMA adapter.
- **Supervision:** About 44k contact pairs; mostly visual GPT-4V pseudo-labels.
- **Demonstrated capability:** Cross-modal retrieval/classification and tactile-description scoring.
- **Reference / ground truth:** 402 human-labeled test triplets; synonym-aware retrieval and GPT-4 judged text.
- **Generalization tested:** Lab versus in-the-wild data; no physical-control evaluation.
- **Baselines:** GPT-4V, open VLMs, SSVTP-LLaMA, alignment ablations.
- **Boundary:** Descriptions are semantic labels, not measured material constants; pseudo-label and evaluator biases remain.
- **Access:** Official code plus original and corrected Hugging Face data. Official README recommends TVL-revise to fix swapped image/tactile directories. An explicit dataset license was not found; Apache-2.0 code terms do not settle data reuse.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2402.13232) · [Sections 3–5; Appendix B](https://arxiv.org/html/2402.13232v1) · [Publication/project record](https://tactile-vlm.github.io/) · [README / linked implementation](https://github.com/Max-Fu/tvl)

<!-- paper:merl -->

### MERL

**[Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement](https://arxiv.org/abs/2403.06659)**

Che Liu et al. · ICML 2024. [Status source](https://proceedings.mlr.press/v235/liu24bg.html) · [Official implementation](https://github.com/cheliu-computation/MERL)

- **Contribution:** Reusable waveform-language bridge with official code and clearly separable alignment/probe tests.
- **Measurements and method:** raw ECG paired with clinical report text. ECG-report contrastive alignment, latent-dropout unimodal alignment, medically grounded prompt enrichment.
- **Supervision:** Report supervision, self-supervised signal alignment; frozen zero-shot inference or linear probes.
- **Demonstrated capability:** Zero-shot cardiac-label recognition and low-label probes on external ECG corpora.
- **Reference / ground truth:** Dataset ECG diagnosis annotations; paired reports supply pretraining semantics.
- **Generalization tested:** External datasets and cross-dataset label mapping; PTB-XL uses official splits.
- **Baselines:** eSSL encoders, prompt variants and unimodal/cross-modal ablations.
- **Boundary:** Six reported benchmark settings include four PTB-XL label subsets, rather than six independent cohorts. Report-derived semantics and label merging bound open-ended reasoning claims.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Sections 3, 4.1-4.5; Appendix A](https://arxiv.org/html/2403.06659v2) · [Proceedings record](https://proceedings.mlr.press/v235/liu24bg.html) · [Author metadata](https://proceedings.mlr.press/v235/liu24bg.html)

<!-- paper:octopi -->

### Octopi

**[Octopi: Object Property Reasoning with Large Tactile-Language Models](https://arxiv.org/abs/2405.02794)**

Yu, Samson et al. · RSS 2024. [Status source](https://octopi-tactile-lvlm.github.io/) · [Official implementation](https://github.com/clear-nus/octopi)

- **Contribution:** Reusable early tactile-language model with explicit property bottleneck, public data, and verified reuse by VLA-Touch.
- **Measurements and method:** GelSight video frames and text prompts. Fine-tuned CLIP encoder, projection and Vicuna; intermediate property descriptions.
- **Supervision:** Human property ratings on PhysiCLeAR; staged alignment and instruction tuning.
- **Demonstrated capability:** Held-out object questions, scenario questions and robot avocado-selection experiment.
- **Reference / ground truth:** Three annotators rate hardness/roughness/bumpiness; task answers and selection outcomes.
- **Generalization tested:** Unseen objects and scenarios; one tactile sensor family.
- **Baselines:** Random, fine-tuned CLIP classifiers, no-property-description and encoder-tuning ablations.
- **Boundary:** Small 74-object/408-video corpus; ordinal human properties are not calibrated mechanics; larger LLM is not uniformly better.
- **Access:** PhysiCLeAR videos are visible in the official repository. The current directory differs in file count from the paper, and no complete repository/data license was located; do not inherit MIT from upstream acknowledgments.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2405.02794) · [Sections III–VII; Appendix A](https://arxiv.org/html/2405.02794v1) · [Publication/project record](https://octopi-tactile-lvlm.github.io/) · [README / linked implementation](https://github.com/clear-nus/octopi)

<!-- paper:neurolm -->

### NeuroLM

**[NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals](https://arxiv.org/abs/2409.00101)**

Wei-Bang Jiang et al. · ICLR 2025. [Status source](https://proceedings.iclr.cc/paper_files/paper/2025/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf) · [Official implementation](https://github.com/935963004/NeuroLM)

- **Contribution:** Separates a useful multitask language interface from unsupported claims about rich EEG semantics.
- **Measurements and method:** EEG patches and task prompts; vocabulary embeddings provide coarse alignment targets.. LaBraM-derived VQ tokenizer, adversarial distribution alignment, GPT-2 multi-channel autoregression and joint instruction tuning.
- **Supervision:** Waveform reconstruction/autoregression plus labeled downstream instructions.
- **Demonstrated capability:** Six dataset tasks: abnormality, events, emotion, sleep stage, workload and slowing.
- **Reference / ground truth:** Dataset categories; not natural-language descriptions of mental contents.
- **Generalization tested:** HMC/workload subject splits; SEED trial split shares people. These are adapted tasks, not unseen-task zero-shot evidence.
- **Baselines:** LaBraM, BIOT and task-specific models; autoregression/robustness/instruction-data ablations.
- **Boundary:** Random GPT-2 vocabulary alignment is coarse, not paired semantic grounding; weaker than strong specialists and hyperparameter-sensitive.
- **Access:** MIT implementation, preprocessing scripts and four model/tokenizer checkpoint entries verified on Hugging Face.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2409.00101) · [Sections 2.1–2.3, 3.1–3.3; Appendices C/H](https://arxiv.org/html/2409.00101v2) · [Model Weights; pretraining; instruction tuning; LICENSE](https://github.com/935963004/NeuroLM) · [checkpoints/](https://huggingface.co/Weibang/NeuroLM/tree/main) · [Abstract and metadata](https://arxiv.org/abs/2409.00101)

<!-- paper:fm-fi -->

### FM-Fi

**[Large Model for Small Data: Foundation Model for Cross-Modal RF Human Activity Recognition](https://arxiv.org/abs/2410.19766)**

Weng, Yuxuan et al. · SenSys 2024. [Status source](https://doi.org/10.1145/3666025.3699349)

- **Contribution:** Strong controlled example of vision-language knowledge reaching nonvisual physical sensing.
- **Measurements and method:** Radar point clouds with coordinates, Doppler and intensity; not raw RF waveforms. CLIP knowledge distillation with contrastive alignment and physically motivated background removal.
- **Supervision:** Paired RGB/radar; few labelled support examples.
- **Demonstrated capability:** Matched RF-encoder, distillation and filtering ablations; zero/few-shot evaluations.
- **Reference / ground truth:** Collected activity labels and synchronized image-radar pairs.
- **Generalization tested:** Ten people and ten environments; leave-one-out 3-shot testing.
- **Baselines:** RF-Net, MetaSense, PointNet++, Point Transformer, same RF encoder without distillation.
- **Boundary:** Limited sensing hardware/task; no verified official code release found.
- **Access:** No usable official implementation verified in this review.

**Evidence locations:** [3.1–3.3; 4; 5.3–5.6](https://arxiv.org/html/2410.19766)

<!-- paper:sensorllm -->

### SensorLLM

**[SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://arxiv.org/abs/2410.10624)**

Li, Zechen et al. · EMNLP 2025. [Status source](https://aclanthology.org/2025.emnlp-main.19/) · [Official implementation](https://github.com/cruiseresearchgroup/SensorLLM)

- **Contribution:** A concrete sensor-encoder-to-LLM integration recipe with activity recognition and alignment experiments.
- **Measurements and method:** Not inspected. Chronos-based sensor embeddings feed an MLP projection into LLaMA3-8B, with channel-boundary tokens. Trend-description alignment precedes task-aware activity-classification tuning.
- **Supervision:** Automatically generated trend descriptions for alignment and dataset activity labels for downstream tuning; optional sensor-statistic text prompts.
- **Demonstrated capability:** Trend-description generation and HAR on five datasets, with five-run reporting. The paper tests alignment removal, text prompts and Chronos+MLP rather than attributing every gain to the backbone.
- **Reference / ground truth:** Generated trend references for alignment; source-dataset activity labels for HAR. The descriptions are not independent measurements of physical causes.
- **Generalization tested:** Subject-independent splits on four datasets and the fixed UCI-HAR split; transfer between alignment and downstream datasets is separately tested.
- **Baselines:** Chronos+MLP, task-only tuning without alignment, prompt ablations, general time-series models and HAR specialists including DeepConvLSTM and Attend.
- **Boundary:** Evidence is concentrated on trends and activity classification. It does not establish arbitrary physiological interpretation or open-ended physical reasoning; normalization can remove absolute scale relevant to other targets.
- **Access:** official code, training/evaluation instructions, and configurations. The original author repository redirects to the current research-group repository. Check backbone and dataset terms separately.

**Evidence locations:** [Final EMNLP paper, sections 3–5; Appendix A.6–A.7](https://aclanthology.org/2025.emnlp-main.19/) · [Revised manuscript v4; Table 3](https://arxiv.org/abs/2410.10624)

<!-- paper:holollm -->

### HoloLLM

**[HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning](https://arxiv.org/abs/2505.17645)**

Zhou, Chuhao et al. · NeurIPS 2025; camera-ready revised February 2026. [Status source](https://arxiv.org/abs/2505.17645) · [Official implementation](https://github.com/NTUMARS/HoloLLM)

- **Contribution:** Directly addresses underrepresented RF/environmental modalities and reports difficult shifts.
- **Measurements and method:** Measured CSI, radar/LiDAR point clouds and images; heterogeneous processed sensor products. CLIP-initialized tokens query fine-grained tailored sensor encoders through UMIP cross-attention.
- **Supervision:** Human/VLM-curated text on MM-Fi and XRF55.
- **Demonstrated capability:** Modality-specific gains with random, cross-subject and cross-environment evaluations.
- **Reference / ground truth:** Action labels and curated captions/QA, not measured causal states.
- **Generalization tested:** Substantial distribution-shift failures remain: MM-Fi WiFi roughly 9% cross-subject/environment.
- **Baselines:** OneLLM, ImageBind, Honeybee, Tokenpacker and projector/encoder ablations.
- **Boundary:** XRF55 RFID/WiFi cross-environment recognition is near chance; fusion exploration is preliminary. XRF55 RGB access requires author permission.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3; 4; Appendix C.1–C.4; Table 5](https://arxiv.org/html/2505.17645v2) · [README](https://github.com/NTUMARS/HoloLLM)

<!-- paper:sensorlm -->

### SensorLM

**[SensorLM: Learning the Language of Wearable Sensors](https://arxiv.org/abs/2506.09108)**

Zhang, Yuwei et al. · NeurIPS 2025. [Status source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42cd98f0e7520d4a63c34891ac1c972f-Abstract-Conference.html) · [Official implementation](https://github.com/Google-Health/consumer-health-research/tree/main/sensorlm)

- **Contribution:** Hierarchical captions connect minute-level wearable features with language.
- **Measurements and method:** 26 minute-level derived features across 24 hours. Hierarchical auto-captioning and contrastive/generative sensor-language learning.
- **Supervision:** See original manuscript; not independently reproduced.
- **Demonstrated capability:** Zero/few-shot recognition, retrieval and captioning on held-out users/concepts.
- **Reference / ground truth:** Activity/study labels for recognition; automatically generated captions for retrieval and captioning.
- **Generalization tested:** See demonstrated capability; no untested cross-device or clinical claim inferred.
- **Baselines:** Tabular-input LLMs for zero-shot/retrieval; matched-backbone SimCLR, DINO and MSN for supervised probes and few-shot evaluation.
- **Boundary:** Private source corpus and constructed captions limit independent inference claims; raw PPG encoding is not demonstrated.
- **Access:** official reference code and released examples/data resources. A public repository should not be interpreted as access to the complete private wearable pretraining cohort or every reported checkpoint.

**Evidence locations:** [Method and experiments](https://arxiv.org/html/2506.09108v1) · [Proceedings record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42cd98f0e7520d4a63c34891ac1c972f-Abstract-Conference.html)

<!-- paper:opentslm -->

### OpenTSLM

**[OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data](https://arxiv.org/abs/2510.02410)**

Langer, Patrick et al. · ICML 2026. [Status source](https://proceedings.mlr.press/v306/langer26a.html) · [Official implementation](https://github.com/OpenTSLM/OpenTSLM)

- **Contribution:** Open code/models/data and an explicit comparison of sensor-language interfaces.
- **Measurements and method:** Sample-level signals normalized with scale and timing supplied in text. Compare soft-prompt tokens with Flamingo-style cross-attention; optional Chronos-2 encoder.
- **Supervision:** Curriculum learning; GPT-4o rationales generated with correct labels.
- **Demonstrated capability:** HAR/sleep/ECG-QA performance, memory scaling, and cardiologist review.
- **Reference / ground truth:** Dataset labels; five cardiologists reviewed 84 ECG examples.
- **Generalization tested:** Reported 80/10/10 splits; inspected description does not establish subject-disjoint transfer.
- **Baselines:** Serialized values, fine-tuned text models, plots, GPT-4o; encoder variants.
- **Boundary:** Label-conditioned rationales are not independent causal explanations or prospective clinical validation.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3.1; 4.1–4.6; Appendix A.2, A.6](https://arxiv.org/html/2510.02410) · [Publication and abstract](https://proceedings.mlr.press/v306/langer26a.html) · [README](https://github.com/OpenTSLM/OpenTSLM)

<!-- paper:anyppg -->

### AnyPPG

**[AnyPPG: An ECG-Guided PPG Foundation Model Trained on Over 100,000 Hours of Recordings for Holistic Health Profiling](https://arxiv.org/abs/2511.01747)**

Guangkun Nie et al. · KDD 2026. [Status source](https://doi.org/10.1145/3770855.3818911) · [Official implementation](https://github.com/PKUDigitalHealth/AnyPPG)

- **Contribution:** Uses ECG only to shape a reusable PPG encoder; diagnostic associations remain bounded by cohort and split design.
- **Measurements and method:** Paired raw 10-second cardiac waveforms; downstream encoder uses PPG.. Frozen ECGFounder supervises a Net1D PPG encoder through symmetric contrastive alignment.
- **Supervision:** Paired-waveform alignment, followed by labeled linear probes or fine-tuning.
- **Demonstrated capability:** Fifteen dataset-task pairs plus held-out-patient MC-MED phenome analysis; independent PPG-Bench.
- **Reference / ground truth:** Dataset physiological/behavioral references and ICD-derived phenotype labels.
- **Generalization tested:** Eight downstream datasets; patient-exclusive phenome cohort within the same MC-MED source.
- **Baselines:** Data/architecture-matched SimCLR/BYOL; released PPG/time-series models; demographic controls.
- **Boundary:** Unknown subject IDs cause sample-level splits in some tasks. Phenome results are single-cohort associations; many benchmark tasks remain weak.
- **Access:** Code, preprocessing, supplementary PDF and PPG checkpoint entry visible. No repository license found; phenotype checkpoints/mappings remain promised.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2511.01747) · [Sections 3–6; Table 1; Section 4.3](https://arxiv.org/html/2511.01747v4) · [Sections 4–5; Table 1; subject-level evaluation](https://arxiv.org/html/2610.13435v1) · [README; load_anyppg; MC-MED note; tree](https://github.com/PKUDigitalHealth/AnyPPG) · [History](https://arxiv.org/abs/2511.01747) · [README and repository header](https://github.com/PKUDigitalHealth/AnyPPG) · [Results](https://arxiv.org/html/2610.13435v1)

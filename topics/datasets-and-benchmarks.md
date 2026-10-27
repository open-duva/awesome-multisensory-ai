# Datasets and evaluation contributions

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Reusable data and independent evaluations earn a place alongside models. Oracle labels, noisy reference instruments, and inferred states are different evidence levels.

6 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:sensefi -->

### SenseFi

**[SenseFi: A Library and Benchmark on Deep-Learning-Empowered WiFi Human Sensing](https://arxiv.org/abs/2207.07859)**

Yang, Jianfei et al. · Patterns 2023. [Status source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10028433/) · [Official implementation](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)

- **Contribution:** Practical benchmark foundation for checking whether a new RF model earns its complexity.
- **Measurements and method:** Channel state information and derived representations. Shared library compares deep architectures, transfer and unsupervised learning.
- **Supervision:** Task labels and self-supervised variants.
- **Demonstrated capability:** Recognition, model size, complexity and transfer comparisons across sensing datasets.
- **Reference / ground truth:** Public dataset activity/gesture annotations.
- **Generalization tested:** Dataset/platform transfer evaluated; not universal RF transfer.
- **Baselines:** Conventional and modern neural architectures under one library.
- **Boundary:** WiFi CSI is hardware/environment dependent; broad library coverage does not remove those shifts.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Results and discussion; methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC10028433/) · [README](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)

<!-- paper:mm-fi -->

### MM-Fi

**[MM-Fi: Multi-Modal Non-Intrusive 4D Human Dataset for Versatile Wireless Sensing](https://arxiv.org/abs/2305.10345)**

Yang, Jianfei et al. · NeurIPS 2023 Datasets and Benchmarks. [Status source](https://papers.nips.cc/paper_files/paper/2023/file/3baf7a39d07e9f4f1e258a412df94521-Paper-Datasets_and_Benchmarks.pdf) · [Official implementation](https://github.com/ybhbingo/MMFi_dataset)

- **Contribution:** Reusable synchronized physical modalities with documented acquisition and difficult splits.
- **Measurements and method:** Synchronized processed sensor streams; radar/LiDAR point clouds and CSI, not raw RF IQ. Shared acquisition platform and 10 Hz timestamp alignment.
- **Supervision:** Action annotations and optimized multi-camera pose estimates.
- **Demonstrated capability:** Over 320k frames, 40 subjects, 27 actions; single/fused sensing comparisons.
- **Reference / ground truth:** Triangulated, regularized 3D keypoints; human action/segment labels.
- **Generalization tested:** Random, 32/8-subject and 3/1-environment splits.
- **Baselines:** Single-modality pose models and linear result fusion.
- **Boundary:** Pose labels inherit visual estimation/occlusion errors; cross-environment performance deteriorates.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3.2; 4; 5](https://arxiv.org/html/2305.10345) · [README](https://github.com/ybhbingo/MMFi_dataset)

<!-- paper:objectfolder-benchmark -->

### ObjectFolder Benchmark

**[The ObjectFolder Benchmark: Multisensory Learning with Neural and Real Objects](https://arxiv.org/abs/2306.00956)**

Gao, Ruohan et al. · CVPR 2023. [Status source](https://objectfolder.stanford.edu/)

- **Contribution:** A reusable testbed spanning measurement, geometry and action; its data underpins later tactile encoders.
- **Measurements and method:** Real measurements plus simulated neural-object sensory queries. ObjectFolder Real adds aligned object-level measurements and recognition, reconstruction and manipulation tasks.
- **Supervision:** Task-specific labels, scanned geometry and measured/simulated sensory references.
- **Demonstrated capability:** Retrieval, localization, reconstruction, contact refinement, traversal and dynamic pushing.
- **Reference / ground truth:** Object identities, scans, recorded sensory signals and physical task endpoints.
- **Generalization tested:** Real and simulated objects; task-specific splits require separate inspection.
- **Baselines:** Unimodal versus multimodal task baselines, including multisensory MPC.
- **Boundary:** 100 real objects; not a universal dynamics benchmark. Simulated signals and real sensor measurements must remain distinct.
- **Access:** No usable official implementation verified in this review.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2306.00956) · [Sections 3–4; especially 4.8–4.10](https://openaccess.thecvf.com/content/CVPR2023/papers/Gao_The_ObjectFolder_Benchmark_Multisensory_Learning_With_Neural_and_Real_Objects_CVPR_2023_paper.pdf) · [Dataset/benchmark releases](https://objectfolder.stanford.edu/)

<!-- paper:sensorbench -->

### SensorBench

**[SensorBench: Benchmarking LLMs in Coding-Based Sensor Processing](https://arxiv.org/abs/2410.10741)**

Quan, Pengrui et al. · HotMobile 2025. [Status source](https://researchportal.hkust.edu.hk/en/publications/sensorbench-benchmarking-llms-in-coding-based-sensor-processing/) · [Official implementation](https://github.com/nesl/LLM_sensor_processing)

- **Contribution:** Tests quantitative work on physical measurements rather than fluent explanations.
- **Measurements and method:** Sample-level signals processed through generated executable code. Assess filtering, reconstruction, spectral analysis, timing and feature extraction.
- **Supervision:** Task prompts; optional DSP fine-tuning; numerical/reference outputs.
- **Demonstrated capability:** LLMs struggle with compositional/parameterized tasks; self-verification helps more than tested fine-tuning.
- **Reference / ground truth:** Known injected distortions, signal-processing references and engineering-expert outputs.
- **Generalization tested:** Multiple tasks/signals; not unrestricted tool-agent or deployment validation.
- **Baselines:** Human experts, direct prompting, CoT, ReAct, self-verification and fine-tuning.
- **Boundary:** Finite task suite and dated model versions; conclusions should not imply all future LLMs fail.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3–5; limitations](https://arxiv.org/html/2410.10741v3) · [README; API/; query/](https://github.com/nesl/LLM_sensor_processing)

<!-- paper:eeg-fm-compass -->

### EEG-FM-Compass

**[EEG-FM-Compass: Progress, Benchmarking, and Future Directions for EEG Foundation Models](https://arxiv.org/abs/2601.17883)**

Dingkun Liu et al. · National Science Review 2026. [Status source](https://doi.org/10.1093/nsr/nwag466) · [Official implementation](https://github.com/Dingkun0817/EEG-FM-Benchmark)

- **Contribution:** Independent EEG evaluation puts pretrained models and supervised specialists on common protocols.
- **Measurements and method:** preprocessed EEG with model-specific interfaces. Standardized full fine-tuning versus frozen probes and specialist controls.
- **Supervision:** Existing pretrained models; supervised downstream protocols.
- **Demonstrated capability:** 12 open FMs and specialist baselines across 13 datasets/nine paradigms; both LOSO and within-person few-shot.
- **Reference / ground truth:** Clinical, BCI task, sleep and experimental labels supplied by source datasets.
- **Generalization tested:** Explicit cross-subject and rapid-calibration regimes; model size is analyzed separately.
- **Baselines:** Traditional features/classifiers, EEGNet, ShallowConv, LMDA and other supervised specialists.
- **Boundary:** One benchmark configuration cannot settle all model rankings. Pretraining dataset overlap and preprocessing remain model-specific; larger size is not a guarantee.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Benchmark experiments; Results; Conclusion; publication history](https://doi.org/10.1093/nsr/nwag466) · [Benchmarking; Quick start; Models and Checkpoints](https://github.com/Dingkun0817/EEG-FM-Benchmark) · [Author metadata](https://api.crossref.org/works/10.1093%2Fnsr%2Fnwag466)

<!-- paper:sentsr-bench -->

### SenTSR-Bench

**[SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning](https://arxiv.org/abs/2602.19455)**

He, Zelin et al. · AISTATS 2026. [Status source](https://proceedings.mlr.press/v300/he26c.html) · [Official implementation](https://github.com/amazon-science/SenTSR-Bench)

- **Contribution:** Rare real industrial diagnostic labels beyond generic synthetic time-series puzzles.
- **Measurements and method:** Standardized hourly industrial acceleration/velocity/temperature readings; not raw high-frequency vibration waveforms.. Inject specialist traces into a general reasoning model; RL with verifiable rewards.
- **Supervision:** Synthetic training; human-curated real industrial diagnostic questions.
- **Demonstrated capability:** 110 streams and 330 questions spanning anomaly, cause and suggested fix.
- **Reference / ground truth:** Human diagnostic annotations; MCQ accuracy and RAGAS for generative answers.
- **Generalization tested:** Industrial evaluation and two public QA benchmarks.
- **Baselines:** Standalone specialists/reasoners; prompting, SFT and RL injection.
- **Boundary:** Selected anomalous cases; suggested fixes are answer labels, not tested intervention benefits or identified causal effects.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Dataset construction; experiments; Appendix D–E](https://arxiv.org/html/2602.19455) · [Benchmark; training; evaluation](https://github.com/amazon-science/SenTSR-Bench) · [Overview; Data Format; License](https://huggingface.co/datasets/ZLHe0/SenTSR-Bench)

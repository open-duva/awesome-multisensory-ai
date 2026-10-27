# Physical state understanding and reasoning

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Calibrated estimation, explicit sensor querying, and tool-based analysis. The reference measurement and the information available to the model matter as much as answer fluency.

5 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:phia -->

### PHIA

**[Transforming Wearable Data into Personal Health Insights using Large Language Model Agents](https://arxiv.org/abs/2406.06464)**

Merrill, Mike A. et al. · Nature Communications 2026. [Status source](https://www.nature.com/articles/s41467-025-67922-y) · [Official implementation](https://github.com/yahskapar/personal-health-insights-agent)

- **Contribution:** Tools and executable analysis turn derived wearable metrics into auditable answers.
- **Measurements and method:** derived behavioral/health metrics and tool outputs. Multistep agent with generated analysis code and information retrieval.
- **Supervision:** See original manuscript; not independently reproduced.
- **Demonstrated capability:** Objective numerical QA and human-rated open-ended insights.
- **Reference / ground truth:** Executable references for objective questions; separate human judgments for open-ended answers.
- **Generalization tested:** See demonstrated capability; no untested cross-device or clinical claim inferred.
- **Baselines:** Numerical reasoning, code generation, and agent/tool ablations.
- **Boundary:** Human helpfulness judgments and numerical answers are not new physiological measurements or prospective health benefits.
- **Access:** official code and evaluation resources. The linked repository uses noncommercial content terms; verify data and service dependencies before reuse. The citation below follows the revised paper's title, which differs from early releases.

**Evidence locations:** [Abstract; comments; history](https://arxiv.org/abs/2406.06464) · [Publisher record](https://www.nature.com/articles/s41467-025-67922-y)

<!-- paper:sensorqa -->

### SensorQA

**[SensorQA: A Question Answering Benchmark for Daily-Life Monitoring](https://arxiv.org/abs/2501.04974)**

Reichman, Benjamin et al. · SenSys 2025. [Status source](https://github.com/benjamin-reichman/SensorQA) · [Official implementation](https://github.com/benjamin-reichman/SensorQA)

- **Contribution:** A concrete long-duration sensor QA evaluation resource with human-authored questions.
- **Measurements and method:** ExtraSensory measurements/features with activity graphs and QA labels. Human-authored questions and answers over activity records.
- **Supervision:** Human QA; dataset activity annotations.
- **Demonstrated capability:** 5.6K questions and baseline/edge-efficiency evaluation.
- **Reference / ground truth:** Reference answers derived from activity records; oracle and predicted-activity settings.
- **Generalization tested:** Sixty users; dataset scope does not establish arbitrary device transfer.
- **Baselines:** Text-only, plots+text and sensor+text models.
- **Boundary:** Language-overlap scores can obscure numerical/time errors; oracle activity information must not be confused with raw-sensor inference.
- **Access:** official QA data and evaluation code; underlying ExtraSensory terms apply separately. This is Reichman et al.'s benchmark, distinct from similarly named QA resources used in other sensor papers.

**Evidence locations:** [3; 5](https://arxiv.org/html/2501.04974) · [README](https://github.com/benjamin-reichman/SensorQA)

<!-- paper:sensorchat -->

### SensorChat

**[SensorChat: Answering Qualitative and Quantitative Questions during Long-Term Multimodal Sensor Interactions](https://arxiv.org/abs/2502.02883)**

Yu, Xiaofan et al. · IMWUT 2025. [Status source](https://github.com/Orienfish/SensorChat) · [Official implementation](https://github.com/Orienfish/SensorChat)

- **Contribution:** An explicit query stage separates numerical operations from language answer generation.
- **Measurements and method:** Raw IMU plus derived acoustic/context features, queried through learned embeddings. Question decomposition, explicit sensor query, answer assembly.
- **Supervision:** Contrastive sensor/context alignment; QA fine-tuning.
- **Demonstrated capability:** SensorQA accuracy, edge deployment and eight-person user study.
- **Reference / ground truth:** SensorQA human answers/activity records; user ratings for qualitative answers.
- **Generalization tested:** Appendix I: answer assembly transfers; sensor querying degrades on unseen users.
- **Baselines:** OneLLM, IMU2CLIP+GPT-4o, LLMSense, DeepSQA and text/plot methods.
- **Boundary:** Main random QA split is not subject-disjoint. Query functions supply numerical precision; qualitative satisfaction is not physiological truth.
- **Access:** official implementation, data-processing instructions, and links to SensorQA. Compare like input conditions when reproducing benchmark results.

**Evidence locations:** [4; 6; Appendix I](https://arxiv.org/html/2502.02883) · [README](https://github.com/Orienfish/SensorChat)

<!-- paper:genforce -->

### GenForce

**[Training Tactile Sensors to Learn Force Sensing from Each Other](https://www.nature.com/articles/s41467-026-68753-1)**

Zhuo Chen et al. · Nature Communications 2026. [Status source](https://www.nature.com/articles/s41467-026-68753-1) · [Official implementation](https://github.com/Zhuochenn/GenForce_Code)

- **Contribution:** Calibrated force transfer connects tactile technologies through explicit mechanical information.
- **Measurements and method:** Image markers or numeric signals converted into marker displacement/size. Marker-to-marker diffusion translation, temporal force prediction and material compensation.
- **Supervision:** Synthetic deformations, source force labels and material characterization.
- **Demonstrated capability:** Homogeneous and heterogeneous transfer; grasp/slip compensation demonstrations.
- **Reference / ground truth:** ATI force/torque measurements.
- **Generalization tested:** GelSight, TacTip and uSkin variants; cross-material and marker-layout transfer.
- **Baselines:** Source-only transfer, target-trained reference and compensation ablations.
- **Boundary:** Not arbitrary sensor physics: representation assumes recoverable deformation markers. Material priors and normalization are still needed.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2503.01058) · [Results: marker translation, heterogeneous transfer; Methods; Code availability](https://www.nature.com/articles/s41467-026-68753-1) · [Publication/project record](https://www.nature.com/articles/s41467-026-68753-1) · [README / linked implementation](https://github.com/Zhuochenn/GenForce_Code)

<!-- paper:tartan-imu -->

### Tartan IMU

**[Tartan IMU: A Light Foundation Model for Inertial Positioning in Robotics](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.pdf)**

Shibo Zhao et al. · CVPR 2025. [Status source](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.pdf) · [Official implementation](https://github.com/superxslam/TartanIMU)

- **Contribution:** Moves beyond semantic labels to physically meaningful state estimation.
- **Measurements and method:** Six-axis IMU aligned to 200 Hz; original paper removes gravity using orientation and assumes known sensor biases.. Shared ResNet/LSTM and robot-specific heads; supervised velocity/covariance losses; LoRA; SLAM-teacher online adaptation with GMM-balanced replay.
- **Supervision:** Reference body velocities/trajectories; online adaptation additionally uses SLAM relative poses.
- **Demonstrated capability:** Four motion families; same-data specialist comparisons; mixed-versus-single-platform training; SubT-to-TartanDrive adaptation and forgetting experiments.
- **Reference / ground truth:** Source-dataset reference trajectories; SLAM teacher feedback for online adaptation.
- **Generalization tested:** Unseen sequences across trained platform families and SubT-to-TartanDrive shift; arbitrary new embodiments explicitly unsupported.
- **Baselines:** AI-IMU, RNIN-VIO, TLIO and IMO retrained on the same data; single/multi-platform training; full versus LoRA fine-tuning.
- **Boundary:** Needs orientation/bias preprocessing and platform heads; online learning uses SLAM. Paper has conflicting adapter counts and unconventional/inconsistent improvement percentages. The 2026 release has different preprocessing, sampling, data and metrics.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [3.2–3.3; experiments](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhao_Tartan_IMU_A_Light_Foundation_Model_for_Inertial_Positioning_in_CVPR_2025_paper.pdf) · [Overview; implementation note](https://github.com/superxslam/TartanIMU) · [Limitations](https://superodometry.com/tartanimu) · [Model card; v3/wdfix2 notes; intended use; evaluation metrics](https://huggingface.co/Tartan-IMU/TartanIMU)

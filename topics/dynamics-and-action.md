# Dynamics, world models and action

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Executed control, open-loop planning, and prediction remain distinct claims. The selected notes identify the actual measured outcome and sensor ablations. See also [LingBot-Touch](sensor-representations.md#lingbot-touch) in representations for frozen-encoder policy evaluations with staged task scoring.

7 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:vision-touch -->

### Making Sense of Vision and Touch

**[Making Sense of Vision and Touch: Self-Supervised Learning of Multimodal Representations for Contact-Rich Tasks](https://arxiv.org/abs/1810.10191)**

Lee, Michelle A. et al. · ICRA 2019. [Status source](https://arxiv.org/abs/1810.10191)

- **Contribution:** An early controlled connection from force/vision representation learning to robot control.
- **Measurements and method:** Images and numerical wrist/robot signals. Compact representation trained on concurrency/contact/flow, then policy learning.
- **Supervision:** Self-supervised prediction and reinforcement learning.
- **Demonstrated capability:** Simulated and real peg insertion.
- **Reference / ground truth:** Observed flow/contact, physical insertion success.
- **Generalization tested:** Geometry, clearance, start conditions and disturbances.
- **Baselines:** Modality/representation ablations.
- **Boundary:** Constrained insertion family; tactile here is wrist wrench, not optical touch.
- **Access:** the primary paper is verified; no implementation link is asserted here. We cite the ICRA paper (arXiv:1810.10191), not the later expanded manuscript with a similar title.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/1810.10191) · [Abstract; initial-repository section cross-check](https://arxiv.org/abs/1810.10191)

<!-- paper:see-hear-feel -->

### See, Hear, and Feel

**[See, Hear, and Feel: Smart Sensory Fusion for Robotic Manipulation](https://arxiv.org/abs/2212.03858)**

Li, Hao et al. · CoRL 2022; PMLR proceedings 2023. [Status source](https://proceedings.mlr.press/v205/li23c.html) · [Official implementation](https://github.com/JunzheJosephZhu/see_hear_feel)

- **Contribution:** A clear controlled demonstration of complementary physical information from three senses, not merely larger multimodal input.
- **Measurements and method:** RGB/tactile images and audio mel spectrogram histories. ResNet encoders and modality-temporal self-attention predict discrete expert actions.
- **Supervision:** Behavior cloning from human demonstrations.
- **Demonstrated capability:** Dense packing and bead pouring on a real robot.
- **Reference / ground truth:** Physical insertion success and poured-mass error.
- **Generalization tested:** Changed packing objects/initial positions; narrow task family.
- **Baselines:** All key modality subsets, direct concatenation and earlier fusion method.
- **Boundary:** Contact microphone is attached to the object; small trial counts; demonstrations and task-specific discrete actions.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2212.03858) · [Sections 3–5](https://arxiv.org/html/2212.03858v1) · [Publication/project record](https://proceedings.mlr.press/v205/li23c.html) · [README / linked implementation](https://github.com/JunzheJosephZhu/see_hear_feel)

<!-- paper:generic-neuromotor -->

### Generic neuromotor interface

**[A generic non-invasive neuromotor interface for human-computer interaction](https://www.nature.com/articles/s41586-025-09255-w)**

Patrick Kaifosh et al. · Nature 2025. [Status source](https://www.nature.com/articles/s41586-025-09255-w) · [Official implementation](https://github.com/facebookresearch/generic-neuromotor-interface)

- **Contribution:** Cross-user EMG decoding evaluated through actual human-computer interaction.
- **Measurements and method:** 16-channel wrist sEMG at 2 kHz. Large-population supervised neural decoders for wrist control, discrete gestures and handwriting.
- **Supervision:** Motion-capture, prompted gestures and text targets; supervised multi-person learning.
- **Demonstrated capability:** New users operate continuous cursor control, discrete navigation and text entry without individual calibration.
- **Reference / ground truth:** Motion capture wrist angles, prompted gestures/text and actual closed-loop target acquisition/text-entry performance.
- **Generalization tested:** Held-out users and band-position changes; personalization can further improve handwriting.
- **Baselines:** Trackpad, motion-capture wrist control, game controller and ordinary handwriting.
- **Boundary:** Conventional HCI baselines outperform the EMG decoders. Hardware-specific training and able-bodied participants do not establish disability-population or arbitrary-device transfer.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Scalable sEMG recording platform; Discussion; Comparison to HCI baselines](https://www.nature.com/articles/s41586-025-09255-w) · [History](https://www.biorxiv.org/content/10.1101/2024.02.23.581779v1) · [README](https://github.com/facebookresearch/generic-neuromotor-interface) · [Author metadata](https://pubmed.ncbi.nlm.nih.gov/40702190/)

<!-- paper:hpt -->

### HPT

**[Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers](https://arxiv.org/abs/2409.20537)**

Lirui Wang et al. · NeurIPS 2024 (spotlight). [Status source](https://liruiw.github.io/hpt/) · [Official implementation](https://github.com/liruiw/HPT)

- **Contribution:** A shared policy trunk learns across incompatible sensor and action spaces, with explicit proprioception ablations.
- **Measurements and method:** Robot states and camera observations; hand-pose surrogates for human-video data.. Embodiment-specific stems and heads surround a shared transformer trunk.
- **Supervision:** Supervised action prediction, then target-task adaptation.
- **Demonstrated capability:** Simulation benchmarks and four hardware tasks on two embodiments.
- **Reference / ground truth:** Demonstrated actions for training; executed task success for evaluation.
- **Generalization tested:** Unseen embodiments/tasks after approximately 100 demonstrations per hardware task.
- **Baselines:** Scratch/no-trunk, no-proprioception, vision encoders; generalist-policy and head comparisons.
- **Boundary:** 52 is a dataset mixture, not 52 real-robot domains. Short-horizon tests; pretraining loss does not establish reliable closed-loop control.
- **Access:** MIT code; Hugging Face checkpoint file listings verified. Published 1B-scale exploration exceeds currently linked checkpoint sizes; no training reproduced.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2409.20537) · [Sections 3–5; Appendix A.1; Appendix C/D](https://arxiv.org/html/2409.20537v1) · [Dataset Mixture; publication heading](https://liruiw.github.io/hpt/) · [Usage; Checkpoints; LICENSE](https://github.com/liruiw/HPT) · [File listing](https://huggingface.co/liruiw/hpt-base/tree/main)

<!-- paper:3d-vitac -->

### 3D-ViTac

**[3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing](https://arxiv.org/abs/2410.24091)**

Huang, Binghao et al. · CoRL 2024. [Status source](https://binghao-huang.github.io/3D-ViTac/) · [Official implementation](https://github.com/binghao-huang/3d-vitac-training-code)

- **Contribution:** Accessible non-optical hardware plus spatially grounded fusion with strong modality-ablation design.
- **Measurements and method:** Dense taxel readings and depth points, mapped through robot kinematics. Unifies tactile and visual points in a common 3D frame; diffusion policy predicts joint sequences.
- **Supervision:** Human robot demonstrations.
- **Demonstrated capability:** Fragile-object and in-hand manipulation, including egg handling and hex-key collection.
- **Reference / ground truth:** Physical subtask and complete-task success.
- **Generalization tested:** Object/initial-state variation and camera-occlusion tests.
- **Baselines:** Vision-only, tactile-only, RGB/tactile-image fusion, dense/continuous signal ablations.
- **Boundary:** Real-data collection cost and unmodeled sensor simulation; no broad embodiment transfer.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2410.24091) · [Sections 3–6; Appendix B](https://arxiv.org/html/2410.24091v2) · [Publication/project record](https://binghao-huang.github.io/3D-ViTac/) · [README / linked implementation](https://github.com/binghao-huang/3d-vitac-training-code)

<!-- paper:foar -->

### FoAR

**[FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2411.15753)**

He, Zihao et al. · IEEE RA-L 2025; IROS 2025 presentation. [Status source](https://ieeexplore.ieee.org/document/10964857/) · [Official implementation](https://github.com/Alan-Heoooh/FoAR)

- **Contribution:** Strong non-optical force-control baseline with controlled fusion comparisons and reproducible implementation.
- **Measurements and method:** Scene point cloud and 100 Hz wrench history. RISE-derived policy uses predicted contact to gate force fusion and refine position commands.
- **Supervision:** Haptic teleoperation and contact prediction.
- **Demonstrated capability:** Wiping, peeling and chopping with disturbance tests.
- **Reference / ground truth:** Action success plus erasure/peeled-length/chopped-segment quality.
- **Generalization tested:** Different board orientations/tool grasps; disturbances, not broad unseen-task transfer.
- **Baselines:** RISE, force-token/force-concat variants, predictor/control ablations.
- **Boundary:** Only 20 trials for wiping/peeling and 10 for chopping; action success is not task-quality score. Naive force addition can hurt.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2411.15753) · [Sections III–IV and Appendix](https://arxiv.org/html/2411.15753v2) · [Publication/project record](https://ieeexplore.ieee.org/document/10964857/) · [README / linked implementation](https://github.com/Alan-Heoooh/FoAR)

<!-- paper:fuse -->

### FuSe

**[Beyond Sight: Finetuning Generalist Robot Policies with Heterogeneous Sensors via Language Grounding](https://arxiv.org/abs/2501.04693)**

Jones, Joshua et al. · ICRA 2025. [Status source](https://fuse-model.github.io/) · [Official implementation](https://github.com/fuse-model/FuSe)

- **Contribution:** Reusable training recipe addresses modality ignoring and demonstrates incremental sensing value with released code/data/model links.
- **Measurements and method:** Images, audio windows, robot states and language. Adds contrastive and generative language grounding to sensor-augmented Octo or a PaliGemma-based VLA.
- **Supervision:** 26,866 teleoperation trajectories with templated instructions.
- **Demonstrated capability:** Tabletop/bag grasping, button pressing and compositional instructions on hardware.
- **Reference / ground truth:** Executed task completion.
- **Generalization tested:** Seen/unseen objects; two different policy backbones.
- **Baselines:** Vision-only finetuning, scratch multimodal models, individual-loss ablations.
- **Boundary:** Three task families and one robot; audio composition is a controlled button setting, not open-ended acoustic reasoning.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Submission history](https://arxiv.org/abs/2501.04693) · [Sections III–IV, especially IV-F/G](https://arxiv.org/html/2501.04693v1) · [Publication/project record](https://fuse-model.github.io/) · [README / linked implementation](https://github.com/fuse-model/FuSe)

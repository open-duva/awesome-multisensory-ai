# Background and technical context

[Home](../README.md) · [Research Map](../atlas/dist/index.html) · [Paper index](../resources/papers.md)

Methodological controls, general time-series encoders, and documented ancestors. These are not counted as core multisensory contributions. See the [encoder comparison](../resources/encoder-comparison.md) for reusable methods and shared checkpoints.

37 curated entries. Generated from the reviewed catalog; edit the source record and rebuild rather than changing this page alone.

<!-- paper:t-loss -->

### T-Loss / Franceschi et al.

**[Unsupervised Scalable Representation Learning for Multivariate Time Series](https://arxiv.org/abs/1901.10738)**

Jean-Yves Franceschi et al. · NeurIPS 2019. [Status source](https://papers.nips.cc/paper_files/paper/2019/hash/53c6de78244e9f528eb3e1cda69699bb-Abstract.html) · [Official implementation](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries)

- **Contribution:** A compact causal CNN maps variable-length sequences to one vector; the positive-pair assumption is part of the method.
- **Scope and evidence:** Causal dilated CNN, global max pooling and projection trained with subseries-positive/random-negative triplet-style loss. UCR/UEA classification, sparse-label experiments, electric-consumption clustering and FordA-source transfer.
- **Boundary:** Subseries-positive invariance may erase local events. Official preprocessing includes test values in normalization; authors document this post-publication caveat.
- **Access:** Official code; a CricketX checkpoint is present and an external pretrained-model index is linked. External index accessibility was not verified; these are dataset-specific artifacts.

**Evidence locations:** [3–5; S1–S2](https://arxiv.org/pdf/1901.10738) · [README Files; Pretrained Models](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries) · [Normalization post-publication note](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries/blob/master/ucr.py) · [Normalization post-publication note](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries/blob/master/uea.py)

<!-- paper:clocs -->

### CLOCS

**[CLOCS: Contrastive Learning of Cardiac Signals Across Space, Time, and Patients](https://arxiv.org/abs/2005.13249)**

Kiyasseh, Dani et al. · ICML 2021. [Status source](https://proceedings.mlr.press/v139/kiyasseh21a/kiyasseh21a.pdf) · [Official implementation](https://github.com/danikiyasseh/CLOCS)

- **Contribution:** Foundational sensor-specific contrastive objective explicitly reused by ECG-FM.
- **Scope and evidence:** Positive pairs exploit patient, temporal and lead relationships. Label-efficient ECG classification and representation transfer.
- **Boundary:** Invariance assumptions can fail with evolving disease or changing recording circumstances.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Section 4](https://proceedings.mlr.press/v139/kiyasseh21a/kiyasseh21a.pdf) · [History](https://arxiv.org/abs/2005.13249)

<!-- paper:wav2vec2 -->

### wav2vec 2.0

**[wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477)**

Baevski, Alexei et al. · NeurIPS 2020. [Status source](https://arxiv.org/abs/2006.11477) · [Official implementation](https://github.com/facebookresearch/fairseq)

- **Contribution:** Not deeply inspected
- **Scope and evidence:** Not deeply inspected Screening only
- **Boundary:** Scope explicitly bounded in decision reason; not all existing entries were fully re-read.
- **Access:** Official source linked; artifact completeness not independently reproduced.

**Evidence locations:** [Publication/official source](https://arxiv.org/abs/2006.11477) · [Abstract and submission history](https://arxiv.org/abs/2006.11477)

<!-- paper:tst -->

### TST / MVTS Transformer

**[A Transformer-based Framework for Multivariate Time Series Representation Learning](https://arxiv.org/abs/2010.02803)**

George Zerveas et al. · KDD 2021. [Status source](https://doi.org/10.1145/3447548.3467401) · [Official implementation](https://github.com/gzerveas/mvts_transformer)

- **Contribution:** A masked-value learning objective can help even when pretraining uses the same training examples as the supervised task.
- **Scope and evidence:** Joint channel projection, learned positional encodings and transformer encoder reconstruct contiguous masked values; downstream heads fine-tune representations. Final KDD paper: eleven classification and six regression datasets; static-versus-fine-tuned and masking/normalization controls.
- **Boundary:** Quadratic temporal attention, fixed channel projection and sequence-sized classification head. Paper uses held-out training validation, while README examples evaluate TEST periodically.
- **Access:** Official reusable framework, preprocessing and experiment scripts; no general pretrained model bank identified.

**Evidence locations:** [3; 4; Tables 1–5; section 5](https://health-nlp.com/files/pubs/kdd21.pdf) · [README Example commands](https://github.com/gzerveas/mvts_transformer) · [Pre-process features](https://github.com/gzerveas/mvts_transformer/blob/master/src/main.py) · [Normalizer](https://github.com/gzerveas/mvts_transformer/blob/master/src/datasets/data.py)

<!-- paper:tnc -->

### TNC

**[Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding](https://arxiv.org/abs/2106.00750)**

Sana Tonekaboni et al. · ICLR 2021. [Status source](https://openreview.net/forum?id=8qDwejCuCN) · [Official implementation](https://github.com/sanatonek/TNC_representation_learning)

- **Contribution:** Choose what counts as a stable local state before choosing a contrastive positive pair.
- **Scope and evidence:** Contrast neighboring windows against distant samples, estimating neighborhood extent by stationarity tests and correcting negative-sampling bias with positive-unlabelled weighting. Clustering and linear classification on simulated states, ECG rhythms and activity-feature sequences.
- **Boundary:** Assumes locally persistent states and meaningful time neighborhoods; window size remains domain-dependent. ADF needs fully observed series.
- **Access:** Official training, preprocessing and evaluation code. No reusable general pretrained checkpoint listed; README advises manual neighborhoods for missing values.

**Evidence locations:** [2; 3.1–3.3; 4; Appendix A.2–A.4](https://arxiv.org/pdf/2106.00750) · [README Note](https://github.com/sanatonek/TNC_representation_learning) · [generate_processed_db; _normalize](https://github.com/sanatonek/TNC_representation_learning/blob/master/data/afib_data.py) · [Input files and subject grouping](https://github.com/sanatonek/TNC_representation_learning/blob/master/data/HAR_data.py)

<!-- paper:bendr -->

### BENDR

**[BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data](https://arxiv.org/abs/2101.12037)**

Kostas, Demetres et al. · Frontiers in Human Neuroscience 2021. [Status source](https://doi.org/10.3389/fnhum.2021.653659) · [Official implementation](https://github.com/SPOClab-ca/BENDR)

- **Contribution:** Historical speech-to-biosignal bridge; useful for real method lineage.
- **Scope and evidence:** wav2vec-inspired compressed convolutional representations with masked contrastive Transformer learning. Cross-task/dataset adaptation of pretrained EEG representations.
- **Boundary:** Older fixed montage/representation assumptions; modern benchmarks are needed for comparative claims.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Methods and discussion](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.653659/full) · [History](https://arxiv.org/abs/2101.12037)

<!-- paper:ts2vec -->

### TS2Vec

**[TS2Vec: Towards Universal Representation of Time Series](https://arxiv.org/abs/2106.10466)**

Zhihan Yue et al. · AAAI 2022. [Status source](https://ojs.aaai.org/index.php/AAAI/article/view/20881) · [Official implementation](https://github.com/zhihanyue/ts2vec)

- **Contribution:** Train an encoder, then choose timestamp, window or whole-series features; transfer evidence exists but is narrower than universal physical semantics.
- **Scope and evidence:** Dilated residual CNN contrasts matching timestamps under overlapping contexts and latent masking, recursively max-pooling to contrast at several scales. Broad UCR/UEA classification, frozen-source transfer, missing-observation tests and masked/unmasked anomaly scoring.
- **Boundary:** A fixed input projection expects a fixed channel layout. Any missing channel masks the entire timestamp in official code; causal use requires restricted/sliding inference.
- **Access:** Official training/inference code and reproduction scripts. No general shared pretrained checkpoint is supplied by the inspected repository; training produces dataset-specific saved models.

**Evidence locations:** [2; 3; Appendix C.1, D; Table 11](https://arxiv.org/pdf/2106.10466) · [README Usage/Code Example](https://github.com/zhihanyue/ts2vec) · [load_UCR; load_UEA; forecasting loaders](https://github.com/zhihanyue/ts2vec/blob/main/datautils.py) · [TSEncoder.forward](https://github.com/zhihanyue/ts2vec/blob/main/models/encoder.py) · [Publication/official source](https://arxiv.org/abs/2106.10466) · [Abstract and submission history](https://arxiv.org/abs/2106.10466)

<!-- paper:ts-tcc -->

### TS-TCC

**[Time-Series Representation Learning via Temporal and Contextual Contrasting](https://arxiv.org/abs/2106.14112)**

Emadeldeen Eldele et al. · IJCAI 2021. [Status source](https://www.ijcai.org/proceedings/2021/324) · [Official implementation](https://github.com/emadeldeen24/TS-TCC)

- **Contribution:** Internal temporal features support an instance-level classifier; the transformer is a training context module, not a universal sensor tokenizer.
- **Scope and evidence:** Three-block CNN; weak/strong views drive cross-view future-latent prediction and a contextual contrastive loss. HAR, sleep and seizure classification; limited labels; twelve bearing-condition transfer scenarios.
- **Boundary:** Scaling, jitter and permutation can destroy task-relevant amplitude/order. Official epilepsy preprocessing fits MinMaxScaler before its split.
- **Access:** Official code, configurations and preprocessing; train self_supervised before linear/fine-tune modes. No broadly reusable released checkpoint identified.

**Evidence locations:** [3; 4.2; 5.1–5.3](https://www.ijcai.org/proceedings/2021/0324.pdf) · [README Training; datasets](https://github.com/emadeldeen24/TS-TCC) · [base_Model.forward](https://github.com/emadeldeen24/TS-TCC/blob/main/models/model.py) · [Scaler and train_test_split order](https://github.com/emadeldeen24/TS-TCC/blob/main/data_preprocessing/epilepsy/preprocess.py)

<!-- paper:rma -->

### RMA

**[RMA: Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)**

Ashish Kumar et al. · Robotics: Science and Systems 2021. [Status source](https://ashish-kmr.github.io/rma-legged-robots/) · [Author-linked successor code](https://github.com/antonilo/rl_locomotion)

- **Contribution:** Recent proprioceptive/contact history adapts behavior without identifying exact environment parameters.
- **Scope and evidence:** Privileged simulator factors train a base policy; a history encoder estimates their behavioral latent at deployment. Hardware terrain/payload changes and matched simulated perturbation tests.
- **Boundary:** Single robot; sparse hardware trials, with early termination for severe failure. Reactive latent inference is not a universal sensor foundation model.
- **Access:** Author project links a GPL-3.0 successor repository for Cross-Modal Supervision, explicitly built on RMA; not an exact frozen original release.

**Evidence locations:** [Submission history and author metadata](https://arxiv.org/abs/2107.04034) · [Sections III–V; Table II](https://arxiv.org/html/2107.04034v1) · [Paper; Code; RSS heading](https://ashish-kmr.github.io/rma-legged-robots/) · [README introduction](https://github.com/antonilo/rl_locomotion)

<!-- paper:objectfolder2 -->

### ObjectFolder 2.0

**[ObjectFolder 2.0: A Multisensory Object Dataset for Sim2Real Transfer](https://arxiv.org/abs/2204.02389)**

Gao, Ruohan et al. · CVPR 2022. [Status source](https://arxiv.org/abs/2204.02389) · [Official implementation](https://github.com/rhgao/ObjectFolder)

- **Contribution:** Faster visual/acoustic fields and deformation-conditioned TouchNet/Taxim.
- **Scope and evidence:** Faster visual/acoustic fields and deformation-conditioned TouchNet/Taxim. 1,000 objects; scale, contact localization and reconstruction transfer.
- **Boundary:** Approximately homogeneous materials and restricted touch orientations/depths.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2204.02389) · [Section 4.3; task evaluations](https://openaccess.thecvf.com/content/CVPR2022/papers/Gao_ObjectFolder_2.0_A_Multisensory_Object_Dataset_for_Sim2Real_Transfer_CVPR_2022_paper.pdf)

<!-- paper:tf-c -->

### TF-C

**[Self-Supervised Contrastive Pre-Training For Time Series via Time-Frequency Consistency](https://arxiv.org/abs/2206.08496)**

Xiang Zhang et al. · NeurIPS 2022. [Status source](https://proceedings.neurips.cc/paper_files/paper/2022/hash/194b8dac525581c346e30a2cebe9a369-Abstract-Conference.html) · [Official implementation](https://github.com/mims-harvard/TFC-pretraining)

- **Contribution:** Real cross-domain fine-tuning evidence; the available example weights have a much narrower scope than the paper’s umbrella claims.
- **Scope and evidence:** Separate time/frequency contrastive encoders plus projectors align local time and spectral views. Eight datasets; one-to-one and one-to-many transfer including EEG-source adaptation to EMG and machine faults.
- **Boundary:** Current example code truncates to the first channel and fixed length; paper describes shared single-channel encoders with concatenation for multivariate use. FFT magnitude omits phase.
- **Access:** Official code/data links and an example SleepEEG checkpoint. January 2023 release changes CNNs to transformers and uses only 1,280 source examples for debugging; it is not the original full-data model.

**Evidence locations:** [3–5; Appendix E–F](https://arxiv.org/pdf/2206.08496) · [README Updated Jan. 2023](https://github.com/mims-harvard/TFC-pretraining) · [Load_Dataset; data_generator](https://github.com/mims-harvard/TFC-pretraining/blob/main/code/TFC/dataloader.py)

<!-- paper:infots -->

### InfoTS

**[Time Series Contrastive Learning with Information-Aware Augmentations](https://arxiv.org/abs/2303.11911)**

Dongsheng Luo et al. · AAAI 2023. [Status source](https://ojs.aaai.org/index.php/AAAI/article/view/25575) · [Official implementation](https://github.com/chengw07/InfoTS)

- **Contribution:** Learn augmentation choices, but verify what a transformation is allowed to erase for the sensor task.
- **Scope and evidence:** A differentiable meta-learner balances label/instance-identity preservation and view diversity, combined with global/local contrastive objectives. Classification/forecasting and augmentation-selection ablations across UCR/UEA and forecasting benchmarks.
- **Boundary:** A finite candidate bank and batch pseudo-label surrogate do not guarantee physically valid invariances. Official linked repository currently contains only README.
- **Access:** Full primary paper and author-hosted HTML are accessible; linked official repository has no runnable implementation or model weights in its inspected public tree.

**Evidence locations:** [Information-aware Criteria; Meta-Contrastive Learning; Experimental Details](https://arxiv.org/pdf/2303.11911) · [Time Series Meta-Contrastive Learning](https://users.cs.fiu.edu/~dluo/papers/aaai23/main.html) · [Repository file tree; README](https://github.com/chengw07/InfoTS)

<!-- paper:nutime -->

### NuTime

**[NuTime: Numerically Multi-Scaled Embedding for Large-Scale Time-Series Pretraining](https://arxiv.org/abs/2310.07402v3)**

Chenguo Lin et al. · TMLR 2024; reviewed arXiv v3. [Status source](https://arxiv.org/abs/2310.07402) · [Official implementation](https://github.com/microsoft/NuTime)

- **Contribution:** Preserve shape and numerical scale; separate test holdout from unseen-domain transfer.
- **Scope and evidence:** BYOL-style pretraining of a Transformer with separate shape and multi-scale numerical-statistic embeddings. Univariate/multivariate classification, few-shot learning, clustering, and anomaly-detection evaluations.
- **Boundary:** Window/channel settings need adaptation; numerical-scale retention does not supply sensor units. No original-scale numerical decoder is established.
- **Access:** Official MIT code and checkpoint_bias9.pth are listed; downloading and running the checkpoint were not tested.

**Evidence locations:** [Sections 3–4; limitations](https://arxiv.org/html/2310.07402v3) · [README, encoders and checkpoint listing](https://github.com/microsoft/NuTime)

<!-- paper:timesfm -->

### TimesFM (original)

**[A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688)**

Abhimanyu Das et al. · ICML 2024. [Status source](https://proceedings.mlr.press/v235/das24c.html) · [Official implementation](https://github.com/google-research/timesfm)

- **Contribution:** A decoder architecture can supply useful hidden features, but the extraction and version must be specified.
- **Scope and evidence:** Patched decoder predicts future numerical patches after large real/synthetic pretraining. Original held-out forecast evaluation; versions 1/2 later tested as frozen classification features.
- **Boundary:** Current repository also serves later generations; do not apply old classification measurements to TimesFM 3.0.
- **Access:** Official code and historical Hugging Face checkpoints; v1 directory retains versions 1/2.

**Evidence locations:** [Sections 4-6](https://arxiv.org/html/2310.10688v4) · [Archived Model Versions](https://github.com/google-research/timesfm) · [Appendix B.2](https://arxiv.org/html/2510.26777v1)

<!-- paper:apple-biosignal-fm -->

### Apple biosignal FMs

**[Large-scale Training of Foundation Models for Wearable Biosignals](https://arxiv.org/abs/2312.05409)**

Salar Abbaspourazad et al. · ICLR 2024. [Status source](https://openreview.net/pdf?id=pC3WJHf51j)

- **Contribution:** Wearable-scale precursor for PaPaGei, Pulse-PPG and ECG-FM style encoders; participant-level positive pairs and private-corpus scaling are the reference point later open work compares against.
- **Scope and evidence:** Participant-level positive pairs, augmentations and regularized momentum contrastive learning. Separate PPG/ECG representations encode demographics and health conditions in AHMS.
- **Boundary:** Large private Apple Watch corpus and no verified public checkpoint; distinct unimodal FMs are not a joint multimodal decoder.
- **Access:** No usable official implementation verified in this review.

**Evidence locations:** [Abstract](https://arxiv.org/abs/2312.05409) · [Proceedings heading](https://openreview.net/pdf?id=pC3WJHf51j)

<!-- paper:timesurl -->

### TimesURL

**[TimesURL: Self-supervised Contrastive Learning for Universal Time Series Representation Learning](https://arxiv.org/abs/2312.15709)**

Jiexi Liu et al. · AAAI 2024. [Status source](https://ojs.aaai.org/index.php/AAAI/article/view/29299) · [Official implementation](https://github.com/Alrash/TimesURL)

- **Contribution:** Adds frequency mixing, harder negatives and reconstruction to the TS2Vec family; its transfer study remains a bounded ten-dataset test.
- **Scope and evidence:** TS2Vec-style encoder and hierarchy plus frequency mixing, synthetic hard negatives and masked time reconstruction. UCR/UEA classification and other tasks; frozen-encoder transfer matrix across ten UCR datasets.
- **Boundary:** Frequency mixing and synthetic negatives can alter meaningful sensor phenomena. Many baseline values are inherited from prior papers/reproductions rather than rerun in one environment.
- **Access:** Official implementation and eight-page appendix. No shared pretrained checkpoint identified in the repository.

**Evidence locations:** [Proposed Framework; Experimental Results](https://arxiv.org/pdf/2312.15709) · [Experimental Details; Transfer Learning; Table 3](https://github.com/Alrash/TimesURL/blob/main/AAAI24_appendix.pdf) · [README Codes](https://github.com/Alrash/TimesURL) · [load_UCR; load_UEA](https://github.com/Alrash/TimesURL/blob/main/src/datautils.py) · [normalize_with_mask](https://github.com/Alrash/TimesURL/blob/main/src/utils.py)

<!-- paper:ts-jepa -->

### TS-JEPA

**[Joint Embeddings Go Temporal](https://arxiv.org/abs/2509.25449)**

Sofiane Ennadir et al. · NeurIPS 2024 TSALM workshop; arXiv posted 2025-09-29. [Status source](https://arxiv.org/abs/2509.25449) · [Official implementation](https://github.com/Sennadir/TS_JEPA)

- **Contribution:** Masked patch embeddings are predicted against an EMA target encoder using latent L1 loss.
- **Scope and evidence:** Masked patch embeddings are predicted against an EMA target encoder using latent L1 loss. Classification and forecasting after dataset-level pretraining, including two related-dataset transfer pairs.
- **Boundary:** Performance is mixed, including weaker FaultDetectionB transfer; small-head evaluation should not automatically be called strict linear probing.
- **Access:** Official experimental source code verified; no broad cross-dataset pretrained checkpoint identified.

**Evidence locations:** [Sections 2-4; Appendix](https://arxiv.org/html/2509.25449v1) · [Repository; src/data_loaders/data_class.py](https://github.com/Sennadir/TS_JEPA) · [Workshop manuscript](https://openreview.net/pdf?id=FIdbozebmy)

<!-- paper:moirai -->

### Moirai (1.x)

**[Unified Training of Universal Time Series Forecasting Transformers](https://arxiv.org/abs/2402.02592)**

Gerald Woo et al. · ICML 2024. [Status source](https://github.com/SalesforceAIResearch/uni2ts) · [Official implementation](https://github.com/SalesforceAIResearch/uni2ts)

- **Contribution:** An any-variate encoder trained for forecasting, useful for testing what shared channel processing contributes.
- **Scope and evidence:** Masked forecast-horizon encoder with multi-patch projections, any-variate attention and mixture-distribution outputs. In/out-of-distribution forecasting; later Moirai 1.1 frozen classification features.
- **Boundary:** Architectural encoder status does not establish task-universal representations; later Moirai 2.0 architecture differs.
- **Access:** Official LOTSA/code and Salesforce/moirai-1.1-R-small/base/large weights; forecast API verified.

**Evidence locations:** [Sections 3-4](https://arxiv.org/html/2402.02592v2) · [Releases; Getting Started](https://github.com/SalesforceAIResearch/uni2ts) · [Appendix B.2](https://arxiv.org/html/2510.26777v1)

<!-- paper:moment -->

### MOMENT

**[MOMENT: A Family of Open Time-series Foundation Models](https://arxiv.org/abs/2402.03885)**

Mononito Goswami et al. · ICML 2024. [Status source](https://arxiv.org/abs/2402.03885) · [Official implementation](https://github.com/moment-timeseries-foundation-model/moment)

- **Contribution:** Restore a directly reusable shared numerical encoder baseline, including its actual frozen-feature protocol.
- **Scope and evidence:** T5-style encoder trained from scratch by masked patch reconstruction. Classification, forecasting, imputation and anomaly detection with different adaptation regimes.
- **Boundary:** Frozen representation transfer is not necessarily unseen-dataset transfer; sequence normalization and omitted sampling-rate metadata limit physical interpretation.
- **Access:** Official MIT code, research pipeline, Time Series Pile and small/base/large Hugging Face checkpoints; embedding API verified.

**Evidence locations:** [Sections 3.1-3.4; Appendix F.2](https://arxiv.org/html/2402.03885v3) · [Usage / Representation Learning](https://huggingface.co/AutonLab/MOMENT-1-large) · [embed and classify](https://github.com/moment-timeseries-foundation-model/moment/blob/main/momentfm/models/moment.py) · [Publication/official source](https://arxiv.org/abs/2402.03885) · [Abstract and submission history](https://arxiv.org/abs/2402.03885)

<!-- paper:v-jepa -->

### V-JEPA

**[Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471)**

Bardes, Adrien et al. · TMLR 2024. [Status source](https://arxiv.org/abs/2404.08471) · [Official implementation](https://github.com/facebookresearch/jepa)

- **Contribution:** Not deeply inspected
- **Scope and evidence:** Not deeply inspected Screening only
- **Boundary:** Scope explicitly bounded in decision reason; not all existing entries were fully re-read.
- **Access:** Official source linked; artifact completeness not independently reproduced.

**Evidence locations:** [Publication/official source](https://arxiv.org/abs/2404.08471) · [Abstract and submission history](https://arxiv.org/abs/2404.08471)

<!-- paper:units -->

### UniTS

**[UniTS: A Unified Multi-Task Time Series Model](https://arxiv.org/abs/2403.00131)**

Shanghua Gao et al. · NeurIPS 2024. [Status source](https://arxiv.org/abs/2403.00131) · [Official implementation](https://github.com/mims-harvard/UniTS)

- **Contribution:** Restore the shared multitask backbone, while distinguishing frozen backbone plus learned prompts from pure frozen probing.
- **Scope and evidence:** Sample/prompt/GEN/CLS tokens, time-variable attention, dynamic linear layers and shared prediction towers. A single co-trained model covers 38 forecasting/classification datasets; new tasks use few-shot fine-tuning or prompt tuning.
- **Boundary:** Dataset prompts are learned context, not natural-language zero-shot instructions; all reported regimes are not one unchanged checkpoint.
- **Access:** Official MIT code and release assets include units_x32_pretrain_checkpoint.pth and units_x128_pretrain_checkpoint.pth, plus supervised/adapted variants.

**Evidence locations:** [Sections 4.1-4.3, 5.2, 5.4; Appendix G](https://arxiv.org/html/2403.00131v3) · [Pretrained weights release](https://github.com/mims-harvard/UniTS/releases/tag/ckpt) · [tokenize; prompt/category token construction](https://github.com/mims-harvard/UniTS/blob/main/models/UniTS.py) · [Training settings and zero-shot learning](https://github.com/mims-harvard/UniTS) · [Publication/official source](https://arxiv.org/abs/2403.00131) · [Abstract and submission history](https://arxiv.org/abs/2403.00131)

<!-- paper:chronos -->

### Chronos

**[Chronos: Learning the Language of Time Series](https://arxiv.org/abs/2403.07815)**

Abdul Fatir Ansari et al. · TMLR 2024. [Status source](https://openreview.net/forum?id=gerNCVqqtR) · [Official implementation](https://github.com/amazon-science/chronos-forecasting)

- **Contribution:** Mean-scaled, quantized observations train a T5-style encoder-decoder forecast model.
- **Scope and evidence:** Mean-scaled, quantized observations train a T5-style encoder-decoder forecast model. Probabilistic forecasting in the original paper; frozen feature classification is evaluated by the separate 2025 transfer study.
- **Boundary:** Quantization and scaling alter amplitude detail; original Chronos, Bolt and Chronos-2 are different artifacts.
- **Access:** Official Apache-2.0 weights/code. Original ChronosPipeline.embed exists and returns encoder states plus scale.

**Evidence locations:** [Sections 3-5](https://arxiv.org/html/2403.07815v3) · [ChronosPipeline.embed](https://github.com/amazon-science/chronos-forecasting/blob/main/src/chronos/chronos.py) · [Model table / citation](https://github.com/amazon-science/chronos-forecasting)

<!-- paper:crosstimenet -->

### CrossTimeNet

**[Cross-Domain Pre-training with Language Models for Transferable Time Series Representations](https://arxiv.org/abs/2403.12372)**

Mingyue Cheng et al. · WSDM 2025 (official author repository). [Status source](https://github.com/ustc-time-series/CrossTimeNet) · [Official implementation](https://github.com/ustc-time-series/CrossTimeNet)

- **Contribution:** Restore a concrete cross-domain tokenization approach without pretending its raw-input interface is universal.
- **Scope and evidence:** Domain-specific VQ tokenizers feed a shared BERT-initialized encoder trained on masked discrete tokens. Cross-domain classification and forecasting; frozen linear evaluation and full fine-tuning.
- **Boundary:** Different tokenizers and output heads serve domains; latest manuscript and repository BibTeX disagree on the last author/title, so use manuscript metadata.
- **Access:** Source code verified; no trained tokenizer/shared-encoder checkpoint download located in official README or repository tree.

**Evidence locations:** [Sections 4.2-4.4; Appendices A and B.2](https://arxiv.org/html/2403.12372v3) · [Constructor, init_vqvae and forward](https://github.com/ustc-time-series/CrossTimeNet/blob/main/bert4timeseries.py) · [README and repository tree](https://github.com/ustc-time-series/CrossTimeNet) · [Methods and experiments](https://arxiv.org/html/2403.12372v3) · [README](https://github.com/ustc-time-series/CrossTimeNet)

<!-- paper:sleepfm-2024 -->

### SleepFM (2024)

**[SleepFM: Multi-modal Representation Learning for Sleep Across Brain Activity, ECG and Respiratory Signals](https://arxiv.org/abs/2405.17766)**

Thapa, Rahul et al. · 2024 preprint; later clinical extension is a distinct paper. [Status source](https://arxiv.org/abs/2405.17766) · [Official implementation](https://github.com/rthapa84/sleepfm-codebase)

- **Contribution:** Leave-one-out contrastive alignment across physiological modalities.
- **Scope and evidence:** Leave-one-out contrastive alignment across physiological modalities. Sleep staging, breathing-disorder detection and cross-modal retrieval.
- **Boundary:** Earlier fixed-format/lower-scale study; do not transfer the 2026 clinical outcomes to this 2024 paper.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Abstract and metadata](https://arxiv.org/abs/2405.17766)

<!-- paper:llm-ablation -->

### LLM forecasting ablations

**[Are Language Models Actually Useful for Time Series Forecasting?](https://arxiv.org/abs/2406.16964)**

Tan, Mingtian et al. · NeurIPS 2024. [Status source](https://arxiv.org/abs/2406.16964) · [Official implementation](https://github.com/BennyTMT/LLMsForTimeSeries)

- **Contribution:** Controlled architecture ablation
- **Scope and evidence:** Remove or replace LLMs in OneFitsAll, Time-LLM and CALF; compare a simple patch-attention baseline. LLM removal/replacement often preserves or improves forecast accuracy in tested setups.
- **Boundary:** The authors explicitly distinguish these forecasters from autoregressive text-conditioned reasoning; do not infer that all sensor-language models are useless.
- **Access:** Official source linked; artifact completeness not independently reproduced.

**Evidence locations:** [Overview; ablations; scope clarification](https://github.com/BennyTMT/LLMsForTimeSeries) · [Abstract and submission history](https://arxiv.org/abs/2406.16964)

<!-- paper:lsm -->

### LSM

**[Scaling Wearable Foundation Models](https://arxiv.org/abs/2410.13638)**

Narayanswamy, Girish et al. · ICLR 2025. [Status source](https://openreview.net/pdf?id=yb4QE6b22f)

- **Contribution:** Useful foundation for the LSM-2/SensorFM lineage; deprioritized versus public waveform/benchmark additions.
- **Scope and evidence:** MAE-style masked reconstruction across time and sensor-feature axes. Imputation/interpolation/extrapolation plus activity/exercise recognition; compute/data/model scaling.
- **Boundary:** Private wearable corpus; self-reported activity labels. Reconstruction scaling does not guarantee unseen-device physiological validity.
- **Access:** No usable official implementation verified in this review.

**Evidence locations:** [Sections 3-6](https://arxiv.org/html/2410.13638v1) · [Proceedings heading](https://openreview.net/pdf?id=yb4QE6b22f)

<!-- paper:cgmformer -->

### CGMformer

**[A pretrained transformer model for decoding individual glucose dynamics from continuous glucose monitoring data](https://pmc.ncbi.nlm.nih.gov/articles/PMC11970253/)**

Yurun Lu et al. · National Science Review 2025. [Status source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11970253/) · [Official implementation](https://github.com/YurunLu/CGMformer)

- **Contribution:** Substantive independent CGM research lineage, distinct from GluFormer despite similar name.
- **Scope and evidence:** Masked discrete glucose tokens with adaptive weighting; transferable day-level embeddings. Multicenter/external population evaluation, imputation, clinical screening/subtyping and meal-response modeling.
- **Boundary:** Major clinical/training cohorts require access requests. Dietary counterfactual simulations are not prospectively validated recommendation benefit.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Results; Methods; Code availability](https://pmc.ncbi.nlm.nih.gov/articles/PMC11970253/) · [Publication metadata](https://pubmed.ncbi.nlm.nih.gov/40191259/)

<!-- paper:anytouch -->

### AnyTouch

**[AnyTouch: Learning Unified Static-Dynamic Representation across Multiple Visuo-tactile Sensors](https://arxiv.org/abs/2502.12191)**

Feng, Ruoxuan et al. · ICLR 2025. [Status source](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4d893f766ab60e5337659b9e71883af4-Abstract-Conference.html) · [Official implementation](https://github.com/GeWu-Lab/AnyTouch)

- **Contribution:** Masked modeling, alignment and cross-sensor matching on TacQuad plus other datasets.
- **Scope and evidence:** Masked modeling, alignment and cross-sensor matching on TacQuad plus other datasets. Offline benchmarks and real pouring.
- **Boundary:** Optical sensor family; sensor overlap and differences in training mixtures complicate rankings.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2502.12191) · [Sections 3–5](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d893f766ab60e5337659b9e71883af4-Paper-Conference.pdf)

<!-- paper:mantis -->

### Mantis / MantisV2

**[Mantis: Lightweight Foundation Model for Time Series Classification](https://proceedings.mlr.press/v306/feofanov26a.html)**

Vasilii Feofanov et al. · ICML 2026; expanded family paper incorporates MantisV2. [Status source](https://proceedings.mlr.press/v306/feofanov26a.html) · [Official implementation](https://github.com/vfeofanov/mantis)

- **Contribution:** A frozen encoder can transfer; the classifier still needs target labels.
- **Scope and evidence:** Contrastive Transformer with temporal tokens, raw mean/std encoding, synthetic pretraining and intermediate-layer aggregation. Frozen-feature and adapted classification on UCR, UEA, HAR and EEG collections.
- **Boundary:** Classification does not establish universal state estimation. Channel-independent encoding and resizing limit cross-channel timing interpretation; layer/head choices are benchmark-sensitive. Raw statistics do not supply physical units.
- **Access:** Apache-2.0 package with transform(), adapters, and separately named Mantis-8M, MantisPlus and MantisV2 checkpoints; not executed in this audit.

**Evidence locations:** [Sections 3–4; Appendices A–C](https://arxiv.org/html/2502.15637v2) · [Sections 2.1, 3.1 and 5.3](https://arxiv.org/html/2602.17868v1) · [README: checkpoints, transform, adapters](https://github.com/vfeofanov/mantis) · [ICML record and full author list](https://proceedings.mlr.press/v306/feofanov26a.html)

<!-- paper:tspulse -->

### TSPulse

**[TSPulse: Tiny Pre-Trained Models with Disentangled Representations for Rapid Time-Series Analysis](https://arxiv.org/abs/2505.13033)**

Vijay Ekambaram et al. · ICLR 2026. [Status source](https://openreview.net/pdf?id=Kw2mvnzCoc) · [Official implementation](https://github.com/ibm-granite/granite-tsfm)

- **Contribution:** Adds a tiny, multi-view encoder with explicit shared-versus-specialized checkpoint evidence.
- **Scope and evidence:** Masked temporal/spectral reconstruction and register-token objectives produce three complementary representation views. Imputation, anomaly scoring, retrieval and adapted multivariate classification; separate unified-checkpoint ablation.
- **Boundary:** Main headline results use task-specialized variants; classification is not zero-shot label prediction.
- **Access:** Apache-2.0 official checkpoint family and reproduction notebooks; three named variants with different masks/patches/heads.

**Evidence locations:** [Sections 2-4; Appendices A.8, A.12, A.15](https://arxiv.org/html/2505.13033v3) · [Model Specialization and variants](https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1) · [Released configuration](https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1/blob/main/config.json)

<!-- paper:lsm-2 -->

### LSM-2

**[LSM-2: Learning from Incomplete Wearable Sensor Data](https://arxiv.org/abs/2506.05321)**

Xu, Maxwell A. et al. · Preprint; venue unconfirmed. [Status source](https://arxiv.org/abs/2506.05321)

- **Contribution:** Adaptive and Inherited Masking handles natural and artificial missingness.
- **Scope and evidence:** Adaptive and Inherited Masking handles natural and artificial missingness. Classification, regression, generation and targeted missingness experiments.
- **Boundary:** Private data; missing-data patterns may correlate with behavior or device operation.
- **Access:** No usable official implementation verified in this review.

**Evidence locations:** [Abstract and metadata](https://arxiv.org/abs/2506.05321)

<!-- paper:cauker -->

### CauKer

**[CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data](https://arxiv.org/abs/2508.02879v3)**

Shifeng Xie et al. · Expanded arXiv v3 combines ICML 2025 workshop and ICLR 2026 contributions. [Status source](https://arxiv.org/abs/2508.02879) · [Official implementation](https://github.com/ShifengXIE/CauKer)

- **Contribution:** Synthetic pretraining is a useful control for real-data overlap.
- **Scope and evidence:** Compose Gaussian-process kernels and propagate sequences through sampled structural causal graphs. Generator comparisons and scaling studies for classification encoders including Mantis and MOMENT.
- **Boundary:** Synthetic structural causality does not establish causal identification in measured physiology or robotics.
- **Access:** Official generator code and a CauKer2M dataset card are public; the card declares Apache-2.0. No full corpus download or integrity check.

**Evidence locations:** [Sections 3–5 and version note](https://arxiv.org/html/2508.02879v3) · [Official repository](https://github.com/ShifengXIE/CauKer) · [Dataset card and visible train split](https://huggingface.co/datasets/paris-noah/CauKer2M)

<!-- paper:forecasting-encoder-transfer -->

### Forecasting encoders for classification

**[Pre-trained Forecasting Models: Strong Zero-Shot Feature Extractors for Time Series Classification](https://arxiv.org/abs/2510.26777)**

Andreas Auer et al. · NeurIPS 2025 BERT2S workshop. [Status source](https://berts-workshop.github.io/accepted-papers/) · [Official implementation](https://github.com/NX-AI/tirex)

- **Contribution:** Use direct transfer experiments to judge forecasting encoders, rather than assuming forecast pretraining either guarantees or forbids reusable features.
- **Scope and evidence:** Frozen forecasting hidden states are pooled across time/layers/channels, optionally augmented by statistics and differenced-series embeddings. Several forecasters match strong classification-pretrained comparators under fitted RF/linear/1-NN probes.
- **Boundary:** Authors also develop TiRex; no comprehensive supervised/ROCKET comparison. Failed runs can substitute DTW results; long/large datasets are excluded.
- **Access:** Paper details extraction and classifiers; official TiRex classification package/docs support its implementation.

**Evidence locations:** [Sections 2-5; Appendix B.1-B.4](https://arxiv.org/html/2510.26777v1) · [Title/author byline and workshop heading](https://openreview.net/pdf?id=vhngjDHyB0) · [Classification overview and API links](https://nx-ai.github.io/tirex/how-to/classification)

<!-- paper:timesx -->

### TimesX

**[Rethinking Multimodal Time-Series Forecasting Evaluation](https://arxiv.org/abs/2607.06973)**

Liu, Haoxin et al. · ICML 2026 (author project). [Status source](https://haoxin1998.github.io/TimesX-project/) · [Official implementation](https://github.com/google-research/google-research/tree/master/TimesX/dataset_agent)

- **Contribution:** Concrete contamination and synthetic-benchmark caution.
- **Scope and evidence:** Refreshable real data; time-bounded event context and cutoff-aware evaluations. Synthetic/real benchmark rank reversals and cutoff sensitivity.
- **Boundary:** Forecasting background; no raw sensor physics or causal-effect validation.
- **Access:** Official implementation linked; weights and dataset permissions require separate checks.

**Evidence locations:** [Design principles and findings](https://haoxin1998.github.io/TimesX-project/) · [Submission history](https://arxiv.org/abs/2607.06973)

<!-- paper:unishape -->

### UniShape

**[A Unified Shape-Aware Foundation Model for Time Series Classification](https://arxiv.org/abs/2601.06429)**

Zhen Liu et al. · AAAI 2026. [Status source](https://ojs.aaai.org/index.php/AAAI/article/download/39574/43535) · [Official implementation](https://github.com/ZLiu21/UniShape)

- **Contribution:** A classification-native shared encoder with a separately tested unseen-dataset feature-extraction setting.
- **Scope and evidence:** Multiscale shape adapter and instance/shape prototype pretraining for class-discriminative representations. Fine-tuned classification on UCR and frozen features plus Random Forest on thirty additional datasets.
- **Boundary:** Primarily univariate classification; source labels and target RF fitting preclude describing the complete pipeline as unsupervised or label-free.
- **Access:** Official source includes distinct finetune and zeroshot checkpoint files; artifact presence verified, no inference rerun.

**Evidence locations:** [Background; Implementation; Pretraining Analysis; Zero-Shot Feature Extraction](https://arxiv.org/html/2601.06429v1) · [README and pretrained_model_ckpt](https://github.com/ZLiu21/UniShape) · [prepareUCR/prepareUEA normalization flags](https://github.com/ZLiu21/UniShape/blob/main/datapre/pretrain_dataset_pre.py) · [normalize_dataset](https://github.com/ZLiu21/UniShape/blob/main/datapre/dataloader.py)

<!-- paper:languagebind -->

### LanguageBind

**[LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment](https://arxiv.org/abs/2310.01852)**

Bin Zhu et al. · ICLR 2024 (per arXiv comments). [Status source](https://arxiv.org/abs/2310.01852) · [Official implementation](https://github.com/PKU-YuanGroup/LanguageBind)

- **Contribution:** Documented alignment ancestor for sensor-language work that binds through language rather than images.
- **Scope and evidence:** Freezes the language encoder from video-language pretraining and contrastively trains encoders for other modalities into that space, using language as the bind. VIDAL-10M dataset and results on 15 video, audio, depth and infrared benchmarks.
- **Boundary:** No physiological, inertial or tactile modality; dataset is CC BY-NC 4.0; a semantic-alignment ancestor rather than a physical-sensing contribution.
- **Access:** Official implementation linked; weights, data and licence terms require separate checks.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2310.01852) · [Repository](https://github.com/PKU-YuanGroup/LanguageBind)

<!-- paper:meta-transformer -->

### Meta-Transformer

**[Meta-Transformer: A Unified Framework for Multimodal Learning](https://arxiv.org/abs/2307.10802)**

Yiyuan Zhang et al. · Preprint; venue not verified. [Status source](https://arxiv.org/abs/2307.10802) · [Official implementation](https://github.com/invictus717/MetaTransformer)

- **Contribution:** Early unified-tokenizer ancestor that treats IMU and time series as modalities.
- **Scope and evidence:** Unified tokenizer maps raw inputs from twelve modalities into a shared token space processed by a frozen modality-shared encoder with task-specific heads, without paired training data. Perception, application and data-mining tasks across twelve modalities, including IMU and time series.
- **Boundary:** Single arXiv version with no verified venue; IMU/time-series results are a small part of a vision-centric framework.
- **Access:** Official implementation linked; weights, data and licence terms require separate checks.

**Evidence locations:** [Abstract and submission history](https://arxiv.org/abs/2307.10802) · [Repository](https://github.com/invictus717/MetaTransformer)

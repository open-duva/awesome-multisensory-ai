# General time-series encoding: evidence matrix

[Home](../README.md) · [Research Map](../atlas/dist/index.html)

22 reviewed encoding methods, shared backbones, and evaluation references. This is a comparison set, not a ranking. A frozen encoder with a fitted target classifier is not label-free classification. Background status denotes this collection's physical-sensing scope, not a judgment that these methods are unimportant.

Generated from `encoder_profile` and the evidence fields in the [catalog](../data/catalog.json). Inspect the linked methods before treating variable channel count, cross-dataset adaptation, and held-out-domain transfer as equivalent.

| Work | Reusable artifact | Embedding granularity | Transfer protocol | Pretraining scope |
| --- | --- | --- | --- | --- |
| [T-Loss / Franceschi et al.](../topics/background.md#t-loss--franceschi-et-al) | Reusable algorithm plus dataset-specific checkpoint(s); not one multivariate foundation checkpoint. | One fixed-size vector per selected window or whole variable-length sequence. | Freeze source encoder, train an RBF SVM using target labels; variable lengths supported without retraining solely for length. | Main evaluation retrains per dataset; FordA encoder is reused in an explicit transfer condition. |
| [TST / MVTS Transformer](../topics/background.md#tst--mvts-transformer) | Reusable architecture/pretraining pipeline; train a model for a compatible target layout. | Contextual timestamp vectors; paper concatenates them for window classification/regression; pooling is possible. | Full fine-tuning versus frozen extracted features; not arbitrary-domain zero-shot encoder reuse. | Mostly target-training-set pretraining; more same-domain unlabelled samples tested. |
| [TNC](../topics/background.md#tnc) | Reusable objective and dataset-specific RNN/CNN code; no shared universal checkpoint. | One embedding per fixed-duration window; sliding windows form a state trajectory. | Frozen representation evaluation within each domain; not an inter-modality pretrained-model transfer study. | Independent self-supervised models for synthetic, ECG and activity-feature datasets. |
| [TS2Vec](../topics/background.md#ts2vec) | Reusable training algorithm and encoder API; fit a source/dataset encoder yourself. | One embedding per timestamp; max-pool arbitrary subsequences or entire series. | Frozen FordA features plus target-trained SVM; FordA-to-Yahoo/KPI cold-start anomaly detection. | Primarily per-dataset self-supervision; explicit separate FordA transfer experiments. |
| [TS-TCC](../topics/background.md#ts-tcc) | Reusable training framework and dataset configs; model weights are generated per experiment. | Downsampled latent sequence internally; flattened CNN window vector for classification. | Frozen linear probes, label-limited fine-tuning, or source-condition supervised fine-tuning followed by target-condition testing. | Separate unlabelled pretraining per dataset; operating-condition transfer for bearing faults. |
| [TF-C](../topics/background.md#tf-c) | Training recipe plus a source-specific small-debugging checkpoint; not a turnkey universal sensor model. | Fixed-size window embedding from time/frequency branches, combined for target tasks. | Source-only SSL, then labelled target fine-tuning; target datasets are unseen during source pretraining. | Separate source datasets or pooled-source experiments; the main one-to-many condition pretrains on SleepEEG. |
| [InfoTS](../topics/background.md#infots) | Paper/design reference; official linked repository is README-only at audit date. | Instance vectors and local-subsequence objectives; no verified public encoding API. | Downstream supervised probe evaluation; no published universal shared-checkpoint protocol. | Per-dataset/task augmentation and representation learning. |
| [NuTime](../topics/background.md#nutime) | Released shared NuTime checkpoint | Window tokens; sequence embedding | Frozen features and supervised adaptation; keep ensemble results separate | Pooled real training splits, including target benchmark domains |
| [TimesFM (original)](../topics/background.md#timesfm-original) | Official TimesFM 1.0/2.0 weights and archived v1 code; current 3.0 is a distinct later release. | Decoder patch hidden states; classification study modifies code to expose all layers then pools/concatenates them. | Original zero-shot forecast evaluation; later frozen hidden-state features plus trained target classifier. | Large web-demand/public and synthetic numerical corpus; original forecasting pretraining with mixed frequencies. |
| [TimesURL](../topics/background.md#timesurl) | Reusable TS2Vec-derived method and code; no common pretrained checkpoint identified. | Timestamp vectors with subsequence/full-series aggregation. | Freeze source encoder, fit target-labelled RBF SVM; compare with target-trained encoder. | Main benchmarks retrain per dataset; explicit ten-UCR source-to-target transfer matrix. |
| [TS-JEPA](../topics/background.md#ts-jepa) | Sennadir/TS_JEPA experimental implementation; a single broadly pretrained downloadable model is not established. | 128-dimensional patch latent states from a small Transformer; task head consumes frozen learned representations. | Frozen encoder with trained small classification/regression head; limited-label fine-tuning experiments also appear. | Pretraining separately uses each dataset training split; two source-to-related-target transfers are reported. |
| [Moirai (1.x)](../topics/background.md#moirai-1x) | Salesforce/moirai-1.1-R-{small,base,large}; Uni2TS library, which is unrelated to Harvard UniTS. | Patch states indexed across time and variates; forecast head decodes distribution parameters. Classification needs an extraction/pooling wrapper. | Original shared zero-shot forecasting; later 1.1 study freezes hidden states and fits labeled classifiers. | LOTSA, over 27B observations across nine domains, with variable forecast tasks and frequencies. |
| [MOMENT](../topics/background.md#moment) | AutonLab/MOMENT-1-large (also small/base); momentfm task_name=embedding; one checkpoint reused across datasets. | Internal channel × patch × hidden states. embed(reduction=none) retains them; mean averages channels and valid patches into one vector. | Paper classification freezes encoder and fits an RBF-SVM; this is nonlinear probing, not label-free classification. Other tasks use zero-shot reconstruction or fitted heads/fine-tuning. | Heterogeneous public Time Series Pile. Only training splits are used, including some target-archive training data. |
| [UniTS](../topics/background.md#units) | Official ckpt release contains SSL x32/x128 and supervised x64 weights. Match checkpoint and task-data configuration. | Sample tokens preserve patch × variable × hidden axes; CLS/task features serve prediction, rather than a canonical single-vector embedding API. | UniTS-PMT freezes backbone but trains task tokens; UniTS-FT updates weights. New-dataset zero-shot forecasting uses a separately trained shared-prompt configuration. | 38 heterogeneous datasets; unified masked reconstruction or separately evaluated supervised multi-task co-training. |
| [Chronos](../topics/background.md#chronos) | Original amazon/chronos-t5-small/base/large checkpoints; ChronosPipeline.embed(context). Newer families require separate version-aware evaluation. | Context-token encoder states returned with scale; sequence pooling is downstream policy, not a guaranteed physical-state vector. | Original zero-shot forecasting; later frozen-feature studies fit a labeled target classifier without encoder updates. | Public multi-domain numerical series plus Gaussian-process synthetic data; univariate forecast pretraining. |
| [CrossTimeNet](../topics/background.md#crosstimenet) | Official training/source code; ready pretrained time-series weights were not verified. BERT initialization alone is not the full artifact. | Last-layer token states; official classifier flattens patch states into a domain-specific head. | Frozen encoder plus fitted linear layer and full fine-tuning are tested. Shared domain training is distinct from transfer to unseen modalities. | Mixed HAR/EEG/ECG training data for classification; forecasting has separate codebook/configurations. |
| [Mantis / MantisV2](../topics/background.md#mantis--mantisv2) | MantisV2 / MantisPlus; distinguish original Mantis-8M | Intermediate-layer tokens aggregated into sequence features | Frozen encoder + fitted LR/RF; optional full or adapter fine-tuning | Synthetic for Plus/V2; original 8M uses real mixtures |
| [TSPulse](../topics/background.md#tspulse) | ibm-granite/granite-timeseries-tspulse-r1: main AD, hybrid-dualhead imputation/search, and block-dualhead classification revisions. | Per-channel temporal and spectral patch embeddings plus register embeddings; retrieval uses register view, classification TSLens combines views. | Zero-shot reconstruction/retrieval; target decoder/head/fuser adaptation for classification. Appendix A.15 uses one imputation/search checkpoint across four tasks. | Heterogeneous Monash/LibCity data, about 1B time points in Appendix A.8; univariate pretraining. |
| [HiMAE](../resources/watchlist.md#himae) | Official synthetic PVC example checkpoint/probe and pretraining code. Full clinical-pretrained artifact equivalence was not verified. | Multiple intermediate CNN temporal scales; pooled bottleneck features support a small downstream probe. | Frozen linear probes and separately reported fine-tuning; source study datasets are held out of downstream pretraining sources. | About 80,000 hours of green PPG from seven Samsung studies; private multi-device corpus. ECG analysis is separately pretrained. |
| [Forecasting encoders for classification](../topics/background.md#forecasting-encoders-for-classification) | Official TiRex classification API/workflow plus published extraction protocol; model artifacts come from their original publishers. | Mean across temporal states, then concatenate layers and channel embeddings; Chronos/Bolt use their single-layer embedding API. | Frozen backbone plus target-label-trained 300-tree RF, linear layer or 1-NN. Zero-shot describes feature extraction, not label-free classification. | Existing forecasters; separates benchmark-exposed classification encoders from forecasting models reported unexposed. |
| [UniShape](../topics/background.md#unishape) | Official pretrained_model_ckpt includes unishape_checkpoint_finetune.pth and unishape_checkpoint_zeroshot.pth; choose the matching protocol. | Learned class/shape tokens summarize selected multiscale subsequences for a sequence-level representation. | UCR experiments fine-tune per target; thirty additional datasets freeze the encoder and train a target Random Forest. | Approximately 1.89M series from training splits of UCR, UEA and TFC-8; default uses 10% labels. |
| [TS2Vec-FM](../resources/watchlist.md#ts2vec-fm) | A single 1.64M student is studied; official downloadable student weights were not verified as of 2026-10-25. | 640-dimensional per-timestamp representations; temporal max pooling yields one vector per channel. | Frozen encoder with target LogReg or 200-tree RF; UCR RF accuracy selects checkpoint, UEA is held out of that selection. | CauKer-generated univariate synthetic corpus; encoder weights do not train on target real data. |

## T-Loss / Franceschi et al.

[Unsupervised Scalable Representation Learning for Multivariate Time Series](https://arxiv.org/abs/1901.10738) · Background · Causal dilated CNN with temporal negative sampling

- **Channel interface:** Channels jointly enter a fixed-input convolution; changed channel count/meaning requires adaptation.
- **Normalization / physical scale:** Dataset-wise z-score (UEA per channel); official legacy loaders combine train/test statistics—fit train only for a new leakage-controlled benchmark.
- **Useful property:** Simple scalable baseline; length-independent pooled vector; demonstrated transfer and low-label use.
- **Encoding boundary:** Max pooling discards timing; subsequences may not preserve event meaning; published normalization protocol needs a visible caveat.
- **Generalization tested:** Main protocol learns one encoder per dataset; frozen FordA encoder also transfers to other univariate datasets with new target SVMs.
- **Baselines / protocol:** DTW, BOSS, shapelet and supervised ensembles; sparse-label ResNet; encoder/negative-count variants.
- **Availability:** Official code; a CricketX checkpoint is present and an external pretrained-model index is linked. External index accessibility was not verified; these are dataset-specific artifacts.

**Evidence:** [3–5; S1–S2](https://arxiv.org/pdf/1901.10738) · [README Files; Pretrained Models](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries) · [Normalization post-publication note](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries/blob/master/ucr.py) · [Normalization post-publication note](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries/blob/master/uea.py)

## TST / MVTS Transformer

[A Transformer-based Framework for Multivariate Time Series Representation Learning](https://arxiv.org/abs/2010.02803) · Background · Masked-value reconstruction transformer

- **Channel interface:** Each timestamp jointly projects a fixed m-channel vector; padding mask handles variable lengths up to configured maximum.
- **Normalization / physical scale:** Train-set per-variable standardization in code; validation/test reuse stored stats; optional per-sample scaling is a separate configuration.
- **Useful property:** Explicit cross-variable reconstruction; useful contrastive-free control; real classification and scalar-regression evaluation.
- **Encoding boundary:** Long high-rate streams are costly; changing channels or output sequence length needs architectural handling; do not select models using README TEST-as-validation examples.
- **Generalization tested:** Pretraining mainly reuses each target dataset’s training samples, with optional extra unlabelled samples; no one-checkpoint cross-domain study.
- **Baselines / protocol:** Supervised transformer, ROCKET, XGBoost, LSTM, dilation-CNN/T-Loss and DTW; frozen-feature versus full fine-tuning.
- **Availability:** Official reusable framework, preprocessing and experiment scripts; no general pretrained model bank identified.

**Evidence:** [3; 4; Tables 1–5; section 5](https://health-nlp.com/files/pubs/kdd21.pdf) · [README Example commands](https://github.com/gzerveas/mvts_transformer) · [Pre-process features](https://github.com/gzerveas/mvts_transformer/blob/master/src/main.py) · [Normalizer](https://github.com/gzerveas/mvts_transformer/blob/master/src/datasets/data.py)

## TNC

[Unsupervised Representation Learning for Time Series with Temporal Neighborhood Coding](https://arxiv.org/abs/2106.00750) · Background · Temporal-neighborhood discrimination; encoder-agnostic objective

- **Channel interface:** Whole multivariate windows; ECG uses a two-channel strided CNN, other settings a recurrent encoder with fixed input features.
- **Normalization / physical scale:** ECG preprocessing uses training-set feature means/std; HAR consumes the archive’s already engineered/scaled feature vectors.
- **Useful property:** Explicit local nonstationarity; positive-unlabelled correction reduces false-negative pressure.
- **Encoding boundary:** Stationarity is not physiological-state identity; chosen windows can mix states, and ADF fails with missing samples.
- **Generalization tested:** Separate encoders per dataset; held-out examples/subjects within each setting. No shared ECG-to-IMU checkpoint transfer is demonstrated.
- **Baselines / protocol:** CPC and T-Loss with matched encoders; supervised encoder, kNN/DTW and k-means.
- **Availability:** Official training, preprocessing and evaluation code. No reusable general pretrained checkpoint listed; README advises manual neighborhoods for missing values.

**Evidence:** [2; 3.1–3.3; 4; Appendix A.2–A.4](https://arxiv.org/pdf/2106.00750) · [README Note](https://github.com/sanatonek/TNC_representation_learning) · [generate_processed_db; _normalize](https://github.com/sanatonek/TNC_representation_learning/blob/master/data/afib_data.py) · [Input files and subject grouping](https://github.com/sanatonek/TNC_representation_learning/blob/master/data/HAR_data.py)

## TS2Vec

[TS2Vec: Towards Universal Representation of Time Series](https://arxiv.org/abs/2106.10466) · Background · Hierarchical context-contrastive dilated CNN

- **Channel interface:** Joint fixed-dimensional channels; input_dims must match; any NaN masks the timestamp.
- **Normalization / physical scale:** UCR: preserve existing normalization, otherwise fit global train mean/std; UEA: training-set per-variable StandardScaler.
- **Useful property:** Flexible granularity; straightforward non-language baseline; masked-data and source-transfer evidence.
- **Encoding boundary:** Generic numerical representations do not encode sensor units or sampling semantics; future context must be removed for online use.
- **Generalization tested:** Main results retrain per dataset. Appendix D transfers a frozen FordA encoder to UCR targets with target-labelled SVMs; cold-start anomaly tests transfer FordA to Yahoo/KPI.
- **Baselines / protocol:** T-Loss, TNC, TS-TCC and TST under matched 320-dimensional SVM evaluation; objective, augmentation and backbone ablations.
- **Availability:** Official training/inference code and reproduction scripts. No general shared pretrained checkpoint is supplied by the inspected repository; training produces dataset-specific saved models.

**Evidence:** [2; 3; Appendix C.1, D; Table 11](https://arxiv.org/pdf/2106.10466) · [README Usage/Code Example](https://github.com/zhihanyue/ts2vec) · [load_UCR; load_UEA; forecasting loaders](https://github.com/zhihanyue/ts2vec/blob/main/datautils.py) · [TSEncoder.forward](https://github.com/zhihanyue/ts2vec/blob/main/models/encoder.py) · [Publication/official source](https://arxiv.org/abs/2106.10466) · [Abstract and submission history](https://arxiv.org/abs/2106.10466)

## TS-TCC

[Time-Series Representation Learning via Temporal and Contextual Contrasting](https://arxiv.org/abs/2106.14112) · Background · Temporal/contextual contrastive CNN with autoregressive context module

- **Channel interface:** CNN input_channels and classifier feature length are fixed by dataset config; no arbitrary channel-count interface.
- **Normalization / physical scale:** No universal scaler in runtime loader; preprocessing varies. Epilepsy script fits MinMax on all samples before split and should be corrected for a fresh evaluation.
- **Useful property:** Tests temporal and contextual objectives; useful low-label and domain-shift controls.
- **Encoding boundary:** Augmentations encode invariances that may remove physical information; operating-condition transfer is narrower than sensor-domain transfer.
- **Generalization tested:** Main encoders train per dataset. Fault transfer trains/fine-tunes on one operating condition and tests another; not arbitrary EEG-to-IMU zero-shot use.
- **Baselines / protocol:** Random encoder, supervised counterpart, SSL-ECG, CPC and adapted SimCLR; objective and augmentation ablations.
- **Availability:** Official code, configurations and preprocessing; train self_supervised before linear/fine-tune modes. No broadly reusable released checkpoint identified.

**Evidence:** [3; 4.2; 5.1–5.3](https://www.ijcai.org/proceedings/2021/0324.pdf) · [README Training; datasets](https://github.com/emadeldeen24/TS-TCC) · [base_Model.forward](https://github.com/emadeldeen24/TS-TCC/blob/main/models/model.py) · [Scaler and train_test_split order](https://github.com/emadeldeen24/TS-TCC/blob/main/data_preprocessing/epilepsy/preprocess.py)

## TF-C

[Self-Supervised Contrastive Pre-Training For Time Series via Time-Frequency Consistency](https://arxiv.org/abs/2206.08496) · Background · Dual time/frequency contrastive encoders with consistency alignment

- **Channel interface:** Paper: shared single-lead model then concatenate channel features. Current example loader: retain first channel and truncate length.
- **Normalization / physical scale:** Released loader consumes preprocessed tensors without a general input standardizer; FFT magnitudes are unnormalized in example code.
- **Useful property:** Directly studies heterogeneous source-to-target adaptation; complementary time/spectrum objectives.
- **Encoding boundary:** Samples with different rates do not share calibrated frequency bins; phase is discarded; released debugging checkpoint differs from paper CNN and full data.
- **Generalization tested:** Target data excluded during source pretraining; each target receives its own labelled adaptation. Cross-frequency bin alignment is not physically calibrated.
- **Baselines / protocol:** Random initialization, kNN, TS2Vec, TS-TCC, CLOCS, Mixing-up, SimCLR and TS-SD; time/frequency/consistency ablations.
- **Availability:** Official code/data links and an example SleepEEG checkpoint. January 2023 release changes CNNs to transformers and uses only 1,280 source examples for debugging; it is not the original full-data model.

**Evidence:** [3–5; Appendix E–F](https://arxiv.org/pdf/2206.08496) · [README Updated Jan. 2023](https://github.com/mims-harvard/TFC-pretraining) · [Load_Dataset; data_generator](https://github.com/mims-harvard/TFC-pretraining/blob/main/code/TFC/dataloader.py)

## InfoTS

[Time Series Contrastive Learning with Information-Aware Augmentations](https://arxiv.org/abs/2303.11911) · Background · Learned augmentation selector plus dilated CNN contrastive encoder

- **Channel interface:** Paper uses a joint fixed-feature linear projection and dilated CNN; no arbitrary-channel tokenizer is established.
- **Normalization / physical scale:** No general sensor calibration recipe is specified by the inspected paper; absence of implementation prevents verifying an input scaler.
- **Useful property:** Makes fidelity-versus-diversity and label availability explicit; challenges ad hoc invariance assumptions.
- **Encoding boundary:** Selected augmentations still come from a predefined bank; pseudo-label optimization is not proof of physical semantic preservation.
- **Generalization tested:** Learned augmentation/encoder per dataset/task; no broad shared-checkpoint transfer is established.
- **Baselines / protocol:** TS2Vec, TNC, TS-TCC, T-Loss and task baselines; predefined augmentation and objective ablations.
- **Availability:** Full primary paper and author-hosted HTML are accessible; linked official repository has no runnable implementation or model weights in its inspected public tree.

**Evidence:** [Information-aware Criteria; Meta-Contrastive Learning; Experimental Details](https://arxiv.org/pdf/2303.11911) · [Time Series Meta-Contrastive Learning](https://users.cs.fiu.edu/~dluo/papers/aaai23/main.html) · [Repository file tree; README](https://github.com/chengw07/InfoTS)

## NuTime

[NuTime: Numerically Multi-Scaled Embedding for Large-Scale Time-Series Pretraining](https://arxiv.org/abs/2310.07402v3) · Background · Shared pretrained encoder

- **Channel interface:** Shared window encoder; concatenate channels then fit a projection
- **Normalization / physical scale:** Normalize shape while encoding window mean and standard deviation
- **Useful property:** Explicit numerical scale representation
- **Encoding boundary:** Does not identify units, calibration, or causal mechanisms
- **Generalization tested:** One checkpoint across tasks; UCR/UEA training data are in the pretraining pool, so test-set holdout does not imply unseen-domain transfer.
- **Baselines / protocol:** TS2Vec, TF-C, ROCKET and HIVE-COTE variants; strongest supervised comparisons ensemble five fine-tuned runs.
- **Availability:** Official MIT code and checkpoint_bias9.pth are listed; downloading and running the checkpoint were not tested.

**Evidence:** [Sections 3–4; limitations](https://arxiv.org/html/2310.07402v3) · [README, encoders and checkpoint listing](https://github.com/microsoft/NuTime)

## TimesFM (original)

[A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688) · Background · Forecast-pretrained patched decoder; representation use is separately evaluated, not implied by its name.

- **Channel interface:** Original model is univariate; independent per-variate classification is distinct from newer multivariate releases.
- **Normalization / physical scale:** Original paper uses context scaling from the first input patch mean/std; hidden features do not inherently preserve original units.
- **Useful property:** Shared prediction backbone and tested cross-task feature extraction provide a useful decoder comparison.
- **Encoding boundary:** Requires layer extraction logic; old and new releases differ; no automatic physical-state or cross-sensor semantic calibration.
- **Generalization tested:** Shared forecast model across histories, horizons and granularities; encoder-transfer evidence comes from a separate study.
- **Baselines / protocol:** ARIMA, local/global forecast baselines, PatchTST and LLMTime.
- **Availability:** Official code and historical Hugging Face checkpoints; v1 directory retains versions 1/2.

**Evidence:** [Sections 4-6](https://arxiv.org/html/2310.10688v4) · [Archived Model Versions](https://github.com/google-research/timesfm) · [Appendix B.2](https://arxiv.org/html/2510.26777v1)

## TimesURL

[TimesURL: Self-supervised Contrastive Learning for Universal Time Series Representation Learning](https://arxiv.org/abs/2312.15709) · Background · Hierarchical contrastive CNN plus masked reconstruction

- **Channel interface:** Fixed joint-channel input projection; explicit masks; UEA loader appends time coordinate.
- **Normalization / physical scale:** Training-fit masked scaler; UEA StandardScaler per feature; loader-specific normalization retained for UCR.
- **Useful property:** Direct extension of a strong baseline; joint objectives; published transfer appendix.
- **Encoding boundary:** Hard negatives and spectral mixing are assumptions, not physics guarantees; results inherit multiple historical baseline implementations.
- **Generalization tested:** Main results train per dataset; transfer reuses one encoder on nine other univariate datasets with target-trained SVMs.
- **Baselines / protocol:** TS2Vec, InfoTS, T-Loss, TNC, TST and TS-TCC; augmentation, hard-negative and reconstruction ablations.
- **Availability:** Official implementation and eight-page appendix. No shared pretrained checkpoint identified in the repository.

**Evidence:** [Proposed Framework; Experimental Results](https://arxiv.org/pdf/2312.15709) · [Experimental Details; Transfer Learning; Table 3](https://github.com/Alrash/TimesURL/blob/main/AAAI24_appendix.pdf) · [README Codes](https://github.com/Alrash/TimesURL) · [load_UCR; load_UEA](https://github.com/Alrash/TimesURL/blob/main/src/datautils.py) · [normalize_with_mask](https://github.com/Alrash/TimesURL/blob/main/src/utils.py)

## TS-JEPA

[Joint Embeddings Go Temporal](https://arxiv.org/abs/2509.25449) · Background · Dataset-trained JEPA representation method, not a demonstrated general pretrained encoder release.

- **Channel interface:** Demonstrated on scalar sensor series; multivariate channel-invariant transfer is not established.
- **Normalization / physical scale:** Supplied CSV loaders standardize floating columns using loaded-data statistics; split scope must be audited before reuse.
- **Useful property:** Tests latent prediction against input reconstruction, autoregression and random-encoder controls.
- **Encoding boundary:** No multi-domain shared checkpoint; few datasets; exact downstream head capacity is not uniformly specified; findings are not universal JEPA dominance.
- **Generalization tested:** FordA-to-FordB and FaultDetectionA-to-B transfer; not a broad shared-checkpoint corpus.
- **Baselines / protocol:** MAE, autoregression, TS2Vec, random frozen encoder and supervised CNN/Transformer.
- **Availability:** Official experimental source code verified; no broad cross-dataset pretrained checkpoint identified.

**Evidence:** [Sections 2-4; Appendix](https://arxiv.org/html/2509.25449v1) · [Repository; src/data_loaders/data_class.py](https://github.com/Sennadir/TS_JEPA) · [Workshop manuscript](https://openreview.net/pdf?id=FIdbozebmy)

## Moirai (1.x)

[Unified Training of Universal Time Series Forecasting Transformers](https://arxiv.org/abs/2402.02592) · Background · Forecast-trained masked Transformer encoder with any-variate attention (Moirai 1.x).

- **Channel interface:** Flattens variate/time patches with any-variate attention; high-channel classification can require univariate fallback due to memory.
- **Normalization / physical scale:** Nonlearnable instance normalization; patch size selected from frequency-specific options. Restore scale for numerical predictions.
- **Useful property:** Explicit support for variable channels and temporal frequency regimes; public corpus and checkpoints.
- **Encoding boundary:** Forecast objective, memory-heavy joint tokens and externally chosen embedding readout; arbitrary channel count is not sensor-meaning equivalence.
- **Generalization tested:** One model supports differing numbers of variates and frequencies; practical memory grows with joint tokens.
- **Baselines / protocol:** PatchTST, TiDE, TFT, DeepAR, AutoARIMA and seasonal-naive forecasting.
- **Availability:** Official LOTSA/code and Salesforce/moirai-1.1-R-small/base/large weights; forecast API verified.

**Evidence:** [Sections 3-4](https://arxiv.org/html/2402.02592v2) · [Releases; Getting Started](https://github.com/SalesforceAIResearch/uni2ts) · [Appendix B.2](https://arxiv.org/html/2510.26777v1)

## MOMENT

[MOMENT: A Family of Open Time-series Foundation Models](https://arxiv.org/abs/2402.03885) · Background · Shared pretrained masked-reconstruction Transformer encoder; not a text-model checkpoint.

- **Channel interface:** Channels encoded independently through shared weights. Default pooled embedding erases channel identity; retain channelwise states when alignment matters.
- **Normalization / physical scale:** RevIN over observed context; reference inputs use length 512 and patch 8 with resampling/padding. Temporal sampling resolution is not explicitly modeled.
- **Useful property:** Open drop-in embeddings; shared pretraining; patch-level access; multiple tested downstream uses.
- **Encoding boundary:** Fixed preprocessing length, no pretrained cross-channel interaction, and normalized amplitude; original classification comparisons mix shared and per-dataset training.
- **Generalization tested:** One pretrained family reused; training splits from evaluation archives can occur in pretraining.
- **Baselines / protocol:** TS2Vec, TNC, TS-TCC, T-Loss, task specialists and classical controls.
- **Availability:** Official MIT code, research pipeline, Time Series Pile and small/base/large Hugging Face checkpoints; embedding API verified.

**Evidence:** [Sections 3.1-3.4; Appendix F.2](https://arxiv.org/html/2402.03885v3) · [Usage / Representation Learning](https://huggingface.co/AutonLab/MOMENT-1-large) · [embed and classify](https://github.com/moment-timeseries-foundation-model/moment/blob/main/momentfm/models/moment.py) · [Publication/official source](https://arxiv.org/abs/2402.03885) · [Abstract and submission history](https://arxiv.org/abs/2402.03885)

## UniTS

[UniTS: A Unified Multi-Task Time Series Model](https://arxiv.org/abs/2403.00131) · Background · Shared multitask time-series backbone with pretrained GEN/CLS towers and dataset/task tokens.

- **Channel interface:** Variable attention models channel interactions with variable-count-compatible backbone; prompts/category tokens remain tied to dataset configuration.
- **Normalization / physical scale:** Official tokenize() centers/scales each channel by sample-context statistics and pads to patch boundaries; numerical predictions restore scale.
- **Useful property:** Genuine shared multi-task weights, joint channel processing, transferable prompt adaptation and downloadable pretraining checkpoints.
- **Encoding boundary:** Task-token fitting uses labels for classification. Variable channel count does not imply semantic alignment of new sensors or invariance to unit/placement changes.
- **Generalization tested:** Separates supervised multitask co-training, SSL/prompt adaptation, new-domain transfer and special zero-shot forecasting.
- **Baselines / protocol:** Task-specific forecasting/classification networks and repurposed language models.
- **Availability:** Official MIT code and release assets include units_x32_pretrain_checkpoint.pth and units_x128_pretrain_checkpoint.pth, plus supervised/adapted variants.

**Evidence:** [Sections 4.1-4.3, 5.2, 5.4; Appendix G](https://arxiv.org/html/2403.00131v3) · [Pretrained weights release](https://github.com/mims-harvard/UniTS/releases/tag/ckpt) · [tokenize; prompt/category token construction](https://github.com/mims-harvard/UniTS/blob/main/models/UniTS.py) · [Training settings and zero-shot learning](https://github.com/mims-harvard/UniTS) · [Publication/official source](https://arxiv.org/abs/2403.00131) · [Abstract and submission history](https://arxiv.org/abs/2403.00131)

## Chronos

[Chronos: Learning the Language of Time Series](https://arxiv.org/abs/2403.07815) · Background · Forecast-pretrained encoder-decoder with an official encoder-embedding API.

- **Channel interface:** Original model encodes univariate sequences; multivariate classification generally concatenates separate channel representations.
- **Normalization / physical scale:** Divides by mean absolute context value (zero-preserving), then uniform quantization; carry returned scale when absolute values matter.
- **Useful property:** Public ready weights and direct embedding access make it an informative forecast-versus-encoding control.
- **Encoding boundary:** Forecast quality alone is insufficient evidence for other tasks; pooling, quantization, channel identity and sampling-rate metadata need explicit handling.
- **Generalization tested:** One checkpoint reused across unseen forecasting datasets; original paper only hypothesizes broader representation use.
- **Baselines / protocol:** Classical/local forecast models and supervised deep forecasters; later study supplies classification controls.
- **Availability:** Official Apache-2.0 weights/code. Original ChronosPipeline.embed exists and returns encoder states plus scale.

**Evidence:** [Sections 3-5](https://arxiv.org/html/2403.07815v3) · [ChronosPipeline.embed](https://github.com/amazon-science/chronos-forecasting/blob/main/src/chronos/chronos.py) · [Model table / citation](https://github.com/amazon-science/chronos-forecasting)

## CrossTimeNet

[Cross-Domain Pre-training with Language Models for Transferable Time Series Representations](https://arxiv.org/abs/2403.12372) · Background · Shared discrete-token BERT encoder with domain-specific learned VQ-VAE front ends.

- **Channel interface:** Official code creates separate VQ-VAEs for 12-channel ECG, 2-channel EEG and 9-channel HAR; shared BERT sees offset token vocabularies.
- **Normalization / physical scale:** No unit-aware normalization is implemented in the inspected shared model/loader. Domain preprocessing and tokenizer training must remain explicit.
- **Useful property:** Models multichannel patches before discretization and shares a language-initialized sequence backbone across heterogeneous domains.
- **Encoding boundary:** Domain-specific front ends, patch sizes and flattened heads constrain length/channel reuse; missing verified checkpoints increases reproduction burden.
- **Generalization tested:** Classification pretraining mixes train splits from HAR, EEG and ECG; domain tokenization is not automatically transferable to arbitrary channels.
- **Baselines / protocol:** Reconstruction/contrastive methods and random-initialization/backbone ablations.
- **Availability:** Source code verified; no trained tokenizer/shared-encoder checkpoint download located in official README or repository tree.

**Evidence:** [Sections 4.2-4.4; Appendices A and B.2](https://arxiv.org/html/2403.12372v3) · [Constructor, init_vqvae and forward](https://github.com/ustc-time-series/CrossTimeNet/blob/main/bert4timeseries.py) · [README and repository tree](https://github.com/ustc-time-series/CrossTimeNet) · [Methods and experiments](https://arxiv.org/html/2403.12372v3) · [README](https://github.com/ustc-time-series/CrossTimeNet)

## Mantis / MantisV2

[Mantis: Lightweight Foundation Model for Time Series Classification](https://proceedings.mlr.press/v306/feofanov26a.html) · Background · Shared pretrained encoder

- **Channel interface:** Channels encoded separately; PCA/learned mixing optional
- **Normalization / physical scale:** Normalize shape, but final architecture bypasses normalization for raw patch mean/std; interpolation still changes effective time scale.
- **Useful property:** Compact classification-oriented shared features
- **Encoding boundary:** Zero-shot applies to the backbone, not the complete labeled classification task
- **Generalization tested:** Synthetic Mantis+/V2 avoids real pretraining-sample overlap; original Mantis-8M used a real mixture overlapping target training sets.
- **Baselines / protocol:** MOMENT, NuTime, forecasting-derived features, tabular models and statistical features; some older baselines use reported results.
- **Availability:** Apache-2.0 package with transform(), adapters, and separately named Mantis-8M, MantisPlus and MantisV2 checkpoints; not executed in this audit.

**Evidence:** [Sections 3–4; Appendices A–C](https://arxiv.org/html/2502.15637v2) · [Sections 2.1, 3.1 and 5.3](https://arxiv.org/html/2602.17868v1) · [README: checkpoints, transform, adapters](https://github.com/vfeofanov/mantis) · [ICML record and full author list](https://proceedings.mlr.press/v306/feofanov26a.html)

## TSPulse

[TSPulse: Tiny Pre-Trained Models with Disentangled Representations for Rapid Time-Series Analysis](https://arxiv.org/abs/2505.13033) · Background · Compact MLP-mixer time-series encoder with temporal, spectral and semantic/register representations.

- **Channel interface:** Pretraining is channel-independent; target fine-tuning can activate identity-initialized channel mixers. Very high channel counts use pooling fallback.
- **Normalization / physical scale:** RevIN and separately scaled FFT components. Base length 512; classification interpolates inputs to 512, affecting physical timescales.
- **Useful property:** Explicit granularity choices, small public weights, missingness-aware masking, and a real one-checkpoint multi-task ablation.
- **Encoding boundary:** Semantic invariance to amplitude/phase can discard calibrated physical information; specialized and unified results must not be conflated.
- **Generalization tested:** Monash/LibCity pretraining is disjoint from evaluation; classification learns a target decoder/fuser.
- **Baselines / protocol:** MOMENT, UniTS, VQShape, statistical detectors and interpolation.
- **Availability:** Apache-2.0 official checkpoint family and reproduction notebooks; three named variants with different masks/patches/heads.

**Evidence:** [Sections 2-4; Appendices A.8, A.12, A.15](https://arxiv.org/html/2505.13033v3) · [Model Specialization and variants](https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1) · [Released configuration](https://huggingface.co/ibm-granite/granite-timeseries-tspulse-r1/blob/main/config.json)

## HiMAE

[HiMAE: Hierarchical Masked Autoencoders Discover Resolution-Specific Structure in Wearable Time Series](https://arxiv.org/abs/2510.25785) · Watchlist · PPG-focused hierarchical waveform encoder; modality-agnostic architecture does not prove modality-agnostic pretrained weights.

- **Channel interface:** Main evaluation is one PPG waveform stream; no arbitrary heterogeneous channel fusion is demonstrated.
- **Normalization / physical scale:** Study: 100 Hz, 10-second windows, quality filtering/bandpass and [-1,1] scaling; public synthetic demo uses 25 Hz and must not be conflated.
- **Useful property:** Explicit multiresolution feature probes and edge-runtime evidence connect abstract embeddings to waveform structure.
- **Encoding boundary:** Not a generic cross-domain checkpoint; private data and demo/study mismatch constrain reproducibility; blood-pressure regression is weak.
- **Generalization tested:** Disjoint PPG task datasets and multiple wearable devices; no universal cross-modality checkpoint demonstrated.
- **Baselines / protocol:** Adapted SimCLR/DINO/MSN/Swin, LSM and PaPaGei.
- **Availability:** Official code and himae_synth.ckpt plus PVC probe demo; README explicitly describes synthetic examples.

**Evidence:** [Sections 3-5; Appendix G.2/G.6](https://arxiv.org/html/2510.25785v1) · [Brief description; data format; PVC linear probe](https://github.com/Simonlee711/HiMAE) · [Proceedings heading](https://openreview.net/pdf?id=iPAy5VpGQa)

## Forecasting encoders for classification

[Pre-trained Forecasting Models: Strong Zero-Shot Feature Extractors for Time Series Classification](https://arxiv.org/abs/2510.26777) · Background · Cross-model frozen-representation evaluation, not a new foundation checkpoint.

- **Channel interface:** Per-variate extraction and concatenation; high-dimensional Moirai examples fall back to independent channels.
- **Normalization / physical scale:** Adds eight-patch mean/std/min/max and differenced-input embeddings to recover information lost through model normalization.
- **Useful property:** Tests the actual hypothesis of forecasting-to-classification transfer with extraction and augmentation ablations.
- **Encoding boundary:** Omitted long/large datasets, DTW fallback for failed runs, learned target probes, and incomplete strong supervised baselines bound aggregate rankings.
- **Generalization tested:** Encoder weights stay fixed; target classifiers still train on labels. Forecast models are distinguished by pretraining exposure.
- **Baselines / protocol:** TiRex, Chronos/Bolt, TimesFM 1/2, Moirai 1.1, Toto, MOMENT, Mantis, NuTime and DTW.
- **Availability:** Paper details extraction and classifiers; official TiRex classification package/docs support its implementation.

**Evidence:** [Sections 2-5; Appendix B.1-B.4](https://arxiv.org/html/2510.26777v1) · [Title/author byline and workshop heading](https://openreview.net/pdf?id=vhngjDHyB0) · [Classification overview and API links](https://nx-ai.github.io/tirex/how-to/classification)

## UniShape

[A Unified Shape-Aware Foundation Model for Time Series Classification](https://arxiv.org/abs/2601.06429) · Background · Shape-aware classification foundation encoder with prototype-based, partially supervised pretraining.

- **Channel interface:** Multivariate pretraining streams are decomposed into univariate channels; paper classification benchmark is univariate.
- **Normalization / physical scale:** Inputs interpolate to 512. Official loader supports global normalization fitted on training data or per-instance normalization; retain the selected config rather than assuming unit preservation.
- **Useful property:** Interpretable multiscale discriminative intervals; released shared weights and held-out-dataset feature tests.
- **Encoding boundary:** Interpolation changes absolute timing; class/shape semantics are not physical units or general multimodal alignment; two checkpoint variants are released.
- **Generalization tested:** Thirty additional datasets test frozen feature transfer; UCR training data occur in pretraining.
- **Baselines / protocol:** Raw-series RF, Mantis, NuTime, MOMENT, UniTS, Chronos and Moirai.
- **Availability:** Official source includes distinct finetune and zeroshot checkpoint files; artifact presence verified, no inference rerun.

**Evidence:** [Background; Implementation; Pretraining Analysis; Zero-Shot Feature Extraction](https://arxiv.org/html/2601.06429v1) · [README and pretrained_model_ckpt](https://github.com/ZLiu21/UniShape) · [prepareUCR/prepareUEA normalization flags](https://github.com/ZLiu21/UniShape/blob/main/datapre/pretrain_dataset_pre.py) · [normalize_dataset](https://github.com/ZLiu21/UniShape/blob/main/datapre/dataloader.py)

## TS2Vec-FM

[Turning TS2Vec into a Foundation Model for Time Series Classification](https://arxiv.org/abs/2610.28602) · Watchlist · Shared convolutional classification encoder distilled from synthetic-pretrained TS2Vec specialists.

- **Channel interface:** Native variable-length convolution, no required interpolation; multivariate channels are encoded independently and concatenated.
- **Normalization / physical scale:** Separate raw-amplitude and instance-normalized shape views feed distinct stems; both are distilled into one representation.
- **Useful property:** Explicit amplitude/shape tradeoff, native-length processing and a strong per-dataset TS2Vec reproduction.
- **Encoding boundary:** No verified ready checkpoint; extremely recent preprint; UCR is not a wholly untouched model-selection benchmark; no cross-channel pretraining.
- **Generalization tested:** One synthetic-trained encoder reused; UCR RF accuracy selects pretraining checkpoints, while UEA is not used for selection.
- **Baselines / protocol:** Per-dataset TS2Vec, MantisV2, NuTime, MOMENT, forecasting encoders, vision features and catch22+.
- **Availability:** Original paper and detailed reproduction/ablation tables available; no official code/checkpoint link located in paper or targeted search.

**Evidence:** [Sections 2-3; Appendix C-D](https://arxiv.org/html/2610.28602v1) · [History and authors](https://arxiv.org/abs/2610.28602)

# Code and tools

[Home](../README.md) · [Paper index](papers.md)

## Author-linked implementation entry points

**85 author-linked code entry points** for curated core/background records. Public visibility, source-code license, pretrained weights, and complete reproducibility are separate claims. Several projects are archived or have restricted/incomplete releases.

| Work | Role | Availability boundary |
| --- | --- | --- |
| [T-Loss / Franceschi et al.](https://github.com/White-Link/UnsupervisedScalableRepresentationLearningTimeSeries) | Background | Official code; a CricketX checkpoint is present and an external pretrained-model index is linked. External index accessibility was not verified; these are dataset-specific artifacts. |
| [CLOCS](https://github.com/danikiyasseh/CLOCS) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [wav2vec 2.0](https://github.com/facebookresearch/fairseq) | Background | Official source linked; artifact completeness not independently reproduced. |
| [TST / MVTS Transformer](https://github.com/gzerveas/mvts_transformer) | Background | Official reusable framework, preprocessing and experiment scripts; no general pretrained model bank identified. |
| [TNC](https://github.com/sanatonek/TNC_representation_learning) | Background | Official training, preprocessing and evaluation code. No reusable general pretrained checkpoint listed; README advises manual neighborhoods for missing values. |
| [BENDR](https://github.com/SPOClab-ca/BENDR) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [TS2Vec](https://github.com/zhihanyue/ts2vec) | Background | Official training/inference code and reproduction scripts. No general shared pretrained checkpoint is supplied by the inspected repository; training produces dataset-specific saved models. |
| [TS-TCC](https://github.com/emadeldeen24/TS-TCC) | Background | Official code, configurations and preprocessing; train self_supervised before linear/fine-tune modes. No broadly reusable released checkpoint identified. |
| [RMA](https://github.com/antonilo/rl_locomotion) | Background | Author project links a GPL-3.0 successor repository for Cross-Modal Supervision, explicitly built on RMA; not an exact frozen original release. |
| [LIMU-BERT](https://github.com/dapowan/LIMU-BERT-Public) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [ObjectFolder 2.0](https://github.com/rhgao/ObjectFolder) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [Oxford wearable SSL](https://github.com/OxWearables/ssl-wearables) | Selected | Code, Torch Hub feature extractors and checkpoints provided under an academic-use license; UK Biobank data require application. |
| [TF-C](https://github.com/mims-harvard/TFC-pretraining) | Background | Official code/data links and an example SleepEEG checkpoint. January 2023 release changes CNNs to transformers and uses only 1,280 source examples for debugging; it is not the original full-data model. |
| [SenseFi](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [IMU2CLIP](https://github.com/facebookresearch/imu2clip) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Touch and Go](https://github.com/fredfyyang/Touch-and-Go) | Selected | official code and [dataset project](https://touch-and-go.github.io/). This paper also appears in the dataset index; it is counted once in the bibliography. |
| [See, Hear, and Feel](https://github.com/JunzheJosephZhu/see_hear_feel) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [InfoTS](https://github.com/chengw07/InfoTS) | Background | Full primary paper and author-hosted HTML are accessible; linked official repository has no runnable implementation or model weights in its inspected public tree. |
| [ImageBind](https://github.com/facebookresearch/ImageBind) | Selected | official code and pretrained models; inspect the model license and each training dataset's access conditions. |
| [BIOT](https://github.com/ycq091044/BIOT) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [MM-Fi](https://github.com/ybhbingo/MMFi_dataset) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [NuTime](https://github.com/microsoft/NuTime) | Background | Official MIT code and checkpoint_bias9.pth are listed; downloading and running the checkpoint were not tested. |
| [TimesFM (original)](https://github.com/google-research/timesfm) | Background | Official code and historical Hugging Face checkpoints; v1 directory retains versions 1/2. |
| [OneLLM](https://github.com/csuhan/OneLLM) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [TimesURL](https://github.com/Alrash/TimesURL) | Background | Official implementation and eight-page appendix. No shared pretrained checkpoint identified in the repository. |
| [LaBraM](https://github.com/935963004/LaBraM) | Selected | official code, preprocessing instructions, and pretrained-model links. Some source EEG corpora require registration or separate agreements. |
| [TS-JEPA](https://github.com/Sennadir/TS_JEPA) | Background | Official experimental source code verified; no broad cross-dataset pretrained checkpoint identified. |
| [UniTouch](https://github.com/cfeng16/UniTouch) | Selected | official implementation and [project page](https://cfeng16.github.io/UniTouch/), with model-use instructions. Verify repository and checkpoint permissions directly; a public GitHub repository alone does not grant a reuse license. |
| [Moirai (1.x)](https://github.com/SalesforceAIResearch/uni2ts) | Background | Official LOTSA/code and Salesforce/moirai-1.1-R-small/base/large weights; forecast API verified. |
| [MOMENT](https://github.com/moment-timeseries-foundation-model/moment) | Background | Official MIT code, research pipeline, Time Series Pile and small/base/large Hugging Face checkpoints; embedding API verified. |
| [V-JEPA](https://github.com/facebookresearch/jepa) | Background | Official source linked; artifact completeness not independently reproduced. |
| [TVL](https://github.com/Max-Fu/tvl) | Selected | Official code plus original and corrected Hugging Face data. Official README recommends TVL-revise to fix swapped image/tactile directories. An explicit dataset license was not found; Apache-2.0 code terms do not settle data reuse. |
| [Generic neuromotor interface](https://github.com/facebookresearch/generic-neuromotor-interface) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [UniTS](https://github.com/mims-harvard/UniTS) | Background | Official MIT code and release assets include units_x32_pretrain_checkpoint.pth and units_x128_pretrain_checkpoint.pth, plus supervised/adapted variants. |
| [MERL](https://github.com/cheliu-computation/MERL) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Chronos](https://github.com/amazon-science/chronos-forecasting) | Background | Official Apache-2.0 weights/code. Original ChronosPipeline.embed exists and returns encoder states plus scale. |
| [CrossTimeNet](https://github.com/ustc-time-series/CrossTimeNet) | Background | Source code verified; no trained tokenizer/shared-encoder checkpoint download located in official README or repository tree. |
| [SiamQuality](https://github.com/chengding0713/SiamQuality) | Selected | Official source code visible; no published weight file or reuse license found in inspected tree. Pretraining data require author request. |
| [Octopi](https://github.com/clear-nus/octopi) | Selected | PhysiCLeAR videos are visible in the official repository. The current directory differs in file count from the paper, and no complete repository/data license was located; do not inherit MIT from upstream acknowledgments. |
| [SleepFM (2024)](https://github.com/rthapa84/sleepfm-codebase) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [PHIA](https://github.com/yahskapar/personal-health-insights-agent) | Selected | official code and evaluation resources. The linked repository uses noncommercial content terms; verify data and service dependencies before reuse. The citation below follows the revised paper's title, which differs from early releases. |
| [T3](https://github.com/alanzjl/t3) | Selected | Official FoTa card lists split archives and models and declares MIT. Viewer inability to open split ZIP files is not proof that the archive is corrupt. Complete download/integrity not tested. |
| [LLM forecasting ablations](https://github.com/BennyTMT/LLMsForTimeSeries) | Background | Official source linked; artifact completeness not independently reproduced. |
| [ECG-FM](https://github.com/bowang-lab/ECG-FM) | Selected | official preprocessing, configurations, public checkpoint links, and a MIMIC-IV-ECG benchmark. Use the revised manuscript when checking cohort sizes; early abstracts differ. |
| [GluFormer](https://github.com/Guylu/GluFormer) | Selected | Official implementation linked; weights and dataset permissions require separate checks. Predominantly non-diabetic pretraining and observational risk analyses. Trial-outcome prediction is not validated treatment selection. Public code does not establish unrestricted pretrained-weight access. |
| [NeuroLM](https://github.com/935963004/NeuroLM) | Selected | MIT implementation, preprocessing scripts and four model/tokenizer checkpoint entries verified on Hugging Face. |
| [HPT](https://github.com/liruiw/HPT) | Selected | MIT code; Hugging Face checkpoint file listings verified. Published 1B-scale exploration exceeds currently linked checkpoint sizes; no training reproduced. |
| [ECGFounder](https://github.com/PKUDigitalHealth/ECGFounder) | Selected | MIT code and MIT-tagged public Hugging Face 1-lead/12-lead checkpoints verified by metadata/file listing. Exact preprocessing required; full training-data access and model execution not verified. |
| [SensorBench](https://github.com/nesl/LLM_sensor_processing) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [SensorLLM](https://github.com/cruiseresearchgroup/SensorLLM) | Selected | official code, training/evaluation instructions, and configurations. The original author repository redirects to the current research-group repository. Check backbone and dataset terms separately. |
| [PaPaGei](https://github.com/Nokia-Bell-Labs/papagei-foundation-model) | Selected | official code and linked model weights; upstream datasets retain separate terms. The official repository is archived as of this review. |
| [3D-ViTac](https://github.com/binghao-huang/3d-vitac-training-code) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Sparsh](https://github.com/facebookresearch/sparsh) | Selected | official code, checkpoints, and benchmark-data instructions. The original repository is archived; review its license and the constituent datasets separately. |
| [FoAR](https://github.com/Alan-Heoooh/FoAR) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [CBraMod](https://github.com/wjq-learning/CBraMod) | Selected | MIT code and a Hugging Face pretrained weight entry verified; underlying EEG datasets have separate access conditions. |
| [FuSe](https://github.com/fuse-model/FuSe) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [SensorQA](https://github.com/benjamin-reichman/SensorQA) | Selected | official QA data and evaluation code; underlying ExtraSensory terms apply separately. This is Reichman et al.'s benchmark, distinct from similarly named QA resources used in other sensor papers. |
| [Pulse-PPG](https://github.com/maxxu05/pulseppg) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [SensorChat](https://github.com/Orienfish/SensorChat) | Selected | official implementation, data-processing instructions, and links to SensorQA. Compare like input conditions when reproducing benchmark results. |
| [CGMformer](https://github.com/YurunLu/CGMformer) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [SleepFM clinical](https://github.com/zou-group/sleepfm-clinical) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [AnyTouch](https://github.com/GeWu-Lab/AnyTouch) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [Mantis / MantisV2](https://github.com/vfeofanov/mantis) | Background | Apache-2.0 package with transform(), adapters, and separately named Mantis-8M, MantisPlus and MantisV2 checkpoints; not executed in this audit. |
| [GenForce](https://github.com/Zhuochenn/GenForce_Code) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Sparsh-skin](https://github.com/facebookresearch/sparsh-multisensory-touch) | Selected | Official code and public pretraining/downstream data directories. The data card lacks an explicit license; the code license should not be assumed to license the data. |
| [TSPulse](https://github.com/ibm-granite/granite-tsfm) | Background | Apache-2.0 official checkpoint family and reproduction notebooks; three named variants with different masks/patches/heads. |
| [HoloLLM](https://github.com/NTUMARS/HoloLLM) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Tartan IMU](https://github.com/superxslam/TartanIMU) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [SensorLM](https://github.com/Google-Health/consumer-health-research/tree/main/sensorlm) | Selected | official reference code and released examples/data resources. A public repository should not be interpreted as access to the complete private wearable pretraining cohort or every reported checkpoint. |
| [Sparsh-X](https://github.com/facebookresearch/sparsh-multisensory-touch) | Selected | Official training/evaluation code, weight links and a public dataset directory; the Hugging Face dataset metadata declares CC BY-NC 4.0. Large archives were not downloaded. |
| [VLA-Touch](https://github.com/clear-nus/vla-touch) | Selected | official implementation. Check its setup and linked component models before assuming all training data or checkpoints are packaged together. |
| [CauKer](https://github.com/ShifengXIE/CauKer) | Background | Official generator code and a CauKer2M dataset card are public; the card declares Apache-2.0. No full corpus download or integrity check. |
| [OpenTSLM](https://github.com/OpenTSLM/OpenTSLM) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [Forecasting encoders for classification](https://github.com/NX-AI/tirex) | Background | Paper details extraction and classifiers; official TiRex classification package/docs support its implementation. |
| [AnyPPG](https://github.com/PKUDigitalHealth/AnyPPG) | Selected | Code, preprocessing, supplementary PDF and PPG checkpoint entry visible. No repository license found; phenotype checkpoints/mappings remain promised. |
| [TinyMyo](https://github.com/pulp-bio/BioFoundation) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [TimesX](https://github.com/google-research/google-research/tree/master/TimesX/dataset_agent) | Background | Official implementation linked; weights and dataset permissions require separate checks. |
| [UniShape](https://github.com/ZLiu21/UniShape) | Background | Official source includes distinct finetune and zeroshot checkpoint files; artifact presence verified, no inference rerun. |
| [EEG-FM-Compass](https://github.com/Dingkun0817/EEG-FM-Benchmark) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [OSF](https://github.com/yang-ai-lab/OSF-Open-Sleep-FM) | Selected | MIT code and OSF-Base weight entry verified. Source datasets require access; preprocessing remains promised. |
| [AnyTouch 2](https://github.com/GeWu-Lab/AnyTouch2) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [SenTSR-Bench](https://github.com/amazon-science/SenTSR-Bench) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [CSFM](https://github.com/guxiao0822/Cardiac-Sensing-FM) | Selected | Official implementation linked; weights and dataset permissions require separate checks. Private CODE data limit full reproduction. Weights require a signed Academic Access Agreement. Synthesized waveforms are estimates, not replacement measurements. |
| [PPG-Bench](https://github.com/mannas-ai/ppg-bench) | Selected | Official implementation linked; weights and dataset permissions require separate checks. |
| [LingBot-Touch](https://github.com/Robbyant/lingbot-touch) | Selected | Apache-2.0 inference code, sensor adapters, sample clips and [Tiny](https://huggingface.co/robbyant/lingbot-touch-tiny) / [Small](https://huggingface.co/robbyant/lingbot-touch-small) encoder weights. Full pretraining data, training pipeline and downstream heads are not included; new sensors require geometry and signal adaptation. |

## Supporting toolkits

| Toolkit | Useful role | Boundary |
| --- | --- | --- |
| [WFDB Python](https://github.com/MIT-LCP/wfdb-python) | Read physiological waveforms, units, channels, sampling and annotations. | Parsing data does not establish measurement validity or synchronization. |
| [Braindecode](https://github.com/braindecode/braindecode) | EEG preprocessing and strong specialist baselines. | Default pipelines/splits are not cross-device robustness evidence. |
| [TACTO](https://github.com/facebookresearch/tacto) | Controlled optical tactile simulation. | Simulation is not real sensor calibration; the official repository is archived. |

These three are infrastructure, not additional counted paper contributions.

## Access pitfalls worth retaining

- **CSFM:** public code does not remove its academic agreement requirement for weights.
- **TVL:** use the recommended corrected dataset and preserve checkpoint revision; original/retrained model statistics differ.
- **PhysiCLeAR/Octopi:** data files are visible, but no explicit full repository/data license was located. Upstream acknowledgments do not grant a new license.
- **Tartan IMU:** the original paper and 2026 challenge releases have different preprocessing and model details. Match a result to its exact version.
- **OSF:** checkpoint availability does not imply unrestricted NSRR data access or that promised preprocessing code is already released.
- **SenTSR-Bench:** Apache-2.0 applies to code; the dataset card states CC BY-NC 4.0.
- **Watchlist models:** SensorFM, TouchWorld, T-WLA and other entries have separate unresolved release questions. See [watch notes](watchlist.md).

## Reproducing a result

Record code revision, checkpoint, license, source data version, preprocessing, original/effective sampling rate, normalization, split files, random seeds, and compute. Check person/session/device overlap and caption/label leakage. Match available modalities and latency when comparing methods. A useful released encoder is not the same as a reproducible original pretraining run.

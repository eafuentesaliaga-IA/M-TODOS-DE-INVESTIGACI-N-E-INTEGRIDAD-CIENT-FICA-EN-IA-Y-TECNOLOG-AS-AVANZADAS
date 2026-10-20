# Model Card

## Model details
- **Name / version:** Multimodal 3D reconstruction of transparent objects using TransparentGS and deflectometry-guided Riemannian optimization — provisional proposal; implemented model version: UNKNOWN — to investigate
- **Owner / contact:** Doctoral researcher leading the project; contact email: UNKNOWN — to investigate
- **Date:** 2026-10-19 (date of this card, not the training date)
- **Architecture:** Proposed architecture: TransparentGS as the Gaussian Splatting and inverse rendering baseline using multi-view RGB images; planned incorporation of transmissive deflectometry constraints and Riemannian updates of Gaussian primitives (particularly SPD covariance matrices). The proposed integration has not yet been implemented or validated.
- **License:** UNKNOWN — to investigate (license for the original implementation is yet to be determined; verify the TransparentGS license separately).

## Intended use
- **Primary intended uses:** Doctoral research on geometric 3D reconstruction of static transparent objects using multi-view RGB images and optical-geometric constraints from transmissive deflectometry.
- **Out-of-scope / misuse:** DO NOT use for industrial inspection, certified metrology, or critical decisions without implementation, calibration, and experimental validation. Hollow, multilayer, or heterogeneous objects are outside the initial scope.
- **Intended users:** Researchers in computer vision, computational optics, and 3D reconstruction.

## Factors
- **Relevant groups / conditions:** Conditions to study: strong refraction and reflection, geometric complexity, optical properties, number of RGB views, quality of deflectometric correspondences, calibration, and initialization.
- **Evaluation factors:** Planned breakdown by scene/object and optical or calibration conditions; results for each condition: UNKNOWN — to investigate.

## Metrics
- **Performance measures:** Candidate metrics: Chamfer Distance, point-to-surface error, geometric precision/completeness, surface-normal angular error, spurious/missing surfaces, convergence, runtime, and memory usage.
- **Decision thresholds:** A 0.5 classification threshold is not applicable; geometric tolerances and convergence criteria: UNKNOWN — to investigate.
- **Variation approach:** Compare seeds/initializations using mean ± standard deviation under the same protocol; exact number of runs and results: UNKNOWN — to investigate.

## Evaluation data
- **Datasets:** Planned scenes of transparent objects with geometric ground truth and, for multimodal variants, calibrated deflectometric measurements. Final dataset, version, and splits: UNKNOWN — to investigate.
- **Preprocessing:** Planned: camera/screen calibration, multi-view RGB organization, and decoding of pattern correspondences; executed and verified pipeline: UNKNOWN — to investigate.

## Training data
- **Datasets:** TransparentGS baseline with public data still to be reproduced; the proposed method will require multi-view RGB and deflectometric observations. Number of scenes, provenance, and final splits: UNKNOWN — to investigate.
- **Known limitations:** The proposed extension does not yet have a confirmed trained model or independent evaluation; deflectometric acquisition and data licenses remain to be verified. The initial scope is limited to solid, static, approximately homogeneous objects.

## Quantitative analyses
- **Overall results:** UNKNOWN — to investigate. No confirmed experimental results are available for the proposed doctoral variant.
- **Disaggregated results:** UNKNOWN — to investigate. Four configurations are proposed: A) TransparentGS; B) A + Riemannian optimization; C) A + deflectometry; D) C + Riemannian optimization. D vs. C isolates the optimizer's effect with the same physical information; B vs. A does so without deflectometry.

## Ethical considerations
- **Risks:** Overstating accuracy or novelty without evidence; using unvalidated results for metrology or inspection; overlooking scene/object biases and possible dataset licensing restrictions.
- **Mitigations:** Clearly label the provisional status, document data provenance and licenses, retain negative results, establish comparable protocols, and avoid deployment in critical applications without validation.

## Caveats and recommendations
- **Caveats:** The proposed algorithmic contribution, final Riemannian metric, and physical coupling remain under investigation; no claim is made that the method outperforms conventional optimization or that its combination is novel.
- **Recommendations:** First reproduce the original TransparentGS; select and document the dataset and calibrated captures; run A–D ablations under comparable conditions with geometric metrics, variability, and computational cost.

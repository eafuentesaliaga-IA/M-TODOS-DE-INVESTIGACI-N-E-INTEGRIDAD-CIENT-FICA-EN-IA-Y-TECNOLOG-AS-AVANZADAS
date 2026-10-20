# Datasheet — Proposed Multimodal Transparent-Object Dataset (NOT YET COLLECTED)

## Motivation
- **Purpose:** Proposed multimodal research dataset for evaluating 3D geometry reconstruction of transparent objects. It is intended to compare TransparentGS (RGB baseline) against a proposed method that adds transmissive deflectometry and Riemannian optimization. Dataset status: PLANNED — no samples collected or generated.
- **Created by / funded by:** Planned by the doctoral researcher for the PhD project. Collaborators, institutional support, and funding: UNKNOWN — to investigate.

## Composition
- **What instances represent:** Planned unit of analysis: one transparent object/scene, with registered multi-view RGB images; corresponding deflectometry pattern observations and reference images (without the object); camera/screen calibration and poses; and, when available, independent 3D ground-truth geometry. Synthetic scenes may include exact meshes and optical simulation metadata. No actual instances are available yet.
- **Labels:** Planned geometric references: 3D surface/mesh or point cloud, object masks, calibrated camera poses, deflectometric pattern correspondences or phase maps, and data-quality flags where appropriate. Ground-truth acquisition and annotation protocol: UNKNOWN — to investigate.
- **Sample vs population:** A future research sample of selected transparent objects, NOT a representative sample of all transparent materials or shapes. Object count, materials, geometry classes, train/validation/test sizes, and real/synthetic proportions: UNKNOWN — to investigate.
- **Missing data:** No missing-value statistics can be reported before acquisition. Potential gaps to record include occluded/reflection-dominated pixels, invalid or ambiguous fringe decoding, incomplete camera calibration, and missing independent 3D ground truth. Observed missingness: UNKNOWN — to investigate.

## Collection process
- **How collected:** PLANNED, NOT EXECUTED: capture calibrated multi-view RGB images of each static transparent object; display known structured patterns on a calibrated screen behind the object and record their refracted appearance, together with no-object reference captures. Record camera/screen geometry and acquisition settings. Optionally begin with physically based synthetic data generated using a documented refractive rendering setup, then validate using real captures. Collect independent reference geometry where feasible. Exact acquisition apparatus: UNKNOWN — to investigate.
- **Timeframe:** Collection has not started. Planned acquisition dates and dataset release date: UNKNOWN — to investigate.
- **Consent / ethics:** The intended subjects are inanimate objects, not people. Avoid identifiable people or private environments in captures. Rights to objects, any third-party image assets, simulator resources, and institutional ethics requirements: UNKNOWN — to investigate.

## Preprocessing / cleaning / labeling
- **Steps:** PLANNED: calibrate camera intrinsics/extrinsics and the screen coordinate system; align and register RGB/deflectometry frames; segment the object; decode pattern correspondences or phase and attach quality/confidence masks; check units and reference-frame consistency; validate geometric ground truth; document failures and exclude unusable captures by predefined rules. Separate train/validation/test by OBJECT or acquisition session to reduce leakage; document any per-split normalization. No preprocessing has yet been executed.
- **Raw data available:** NOT YET AVAILABLE. The planned release should preserve raw RGB frames, raw fringe/pattern and reference captures, calibration files, acquisition logs, annotations, and preprocessing code, subject to licensing and storage constraints.

## Uses
- **Appropriate uses:** Once created and validated: research in transparent-object 3D reconstruction; fair baseline-versus-proposal comparisons on identical object/scene splits; RGB-only and RGB-plus-deflectometry ablation studies; analysis of geometry error, robustness, calibration sensitivity, and computational cost.
- **Should NOT be used for:** Should NOT be used for certified industrial metrology, safety-critical inspection, broad claims of real-world generalization, or training/evaluation claims before data collection and independent validation. Do not claim that RGB-only TransparentGS and RGB-plus-deflectometry variants have equal sensor information: report the extra modality and its acquisition cost explicitly.

## Distribution
- **How distributed:** NOT RELEASED. Candidate distribution: a versioned research repository with a dataset manifest, acquisition protocol, calibration metadata, checksums, and train/validation/test splits. Repository URL, format, access conditions, and hosting location: UNKNOWN — to investigate.
- **License / restrictions:** UNKNOWN — to investigate. Obtain permission for captured, simulated, or third-party assets; verify any borrowed baseline dataset licenses separately; choose a distribution license before publication.

## Maintenance
- **Maintainer:** Proposed responsibility: the doctoral researcher. Formal maintainer, public contact, and hosting institution: UNKNOWN — to investigate.
- **Update plan:** PLANNED: assign dataset versions; publish a change log, collection and calibration protocols, manifest, checksums, known failure cases, and split definitions. Reassess updates after pilot capture. Actual maintenance schedule: UNKNOWN — to investigate.

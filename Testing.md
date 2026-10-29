# 🧪 Testing Strategy

This document defines the testing approach used to validate the reliability, correctness, and performance of the 3D Medical Imaging Processing Pipeline.

## 1. Objectives of Testing
Our testing strategy focuses on three main pillars:
* **Correctness:** Ensuring the Multi-Planar Reconstruction (MPR) algorithm maps 2D planes into 3D voxel space accurately without indexing or boundary errors.
* **Data Integrity:** Verifying that input formats (NRRD volumes and CSV spatial coordinates) are parsed cleanly into internal data structures without corruption.
* **Performance:** Validating that the vectorized NumPy pipeline maintains high execution speed (targeting >100 FPS) on standard datasets.

## 2. Test Suites & Implementation
We utilize **pytest** to automate and execute our test suite:

* **Data Ingestion & Loaders (`CSVPointLoader` & `VolumeLoader`):**
  - Validates parsing of raw CSV coordinate points and NRRD volumetric datasets.
  - Ensures accurate construction of `DenseMatrix3D` and `Plane` objects with correct dimensions, data types (`uint8`), and orientation.
  - Verifies robust error handling when encountering missing or malformed input files.

* **Algorithm & Projection Tests (`test_projection.py`):**
  - Tests the core mathematical logic, vector extraction ($u, v$ axes), and 2D-to-3D coordinate transformation.
  - Checks boundary conditions and edge cases using `np.clip` to prevent out-of-bounds indexing.

* **Integration & Pipeline Tests (`Ex0.py`):**
  - Validates the full workflow from reading raw inputs to rendering the final sliced video (`mpr_output_video.mp4`).

## 3. Execution Instructions
To run the full automated test suite with live terminal print outputs, execute:
```bash
python -m pytest -s
```
To run a specific test file :
```bash
python -m pytest -s tests/test_projection.py
```
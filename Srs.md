

# Software Requirements Specification (SRS)
## 3D Medical Volume MPR Pipeline

---

## 1. Introduction
### 1.1 Purpose
This document specifies the software requirements for the 3D Multi-Planar Reconstruction (MPR) and projection pipeline, designed to process 3D medical volume data and generate high-performance 2D slices and video exports.

### 1.2 Scope
* Efficient handling of 3D volumetric data structures wrapping NumPy arrays.
* Fast geometric slicing and projection of arbitrary planes onto 2D grids.
* Real-time benchmark execution targeting high frame rates (100–300+ FPS).
* Exporting computed projection frames into standard video formats (MP4).

---

## 2. Overall Description
### 2.1 Product Perspective
The system is built as a modular Python library utilizing `NumPy` for vectorized matrix operations and `OpenCV` (`cv2`) for visualization and video rendering, integrated with `pytest` for performance validation.

### 2.2 User Characteristics
* Computer Science students and researchers requiring high-performance matrix manipulations and volumetric rendering simulations.

---

## 3. Specific Requirements
### 3.1 Functional Requirements
* **Volume Loading:** Ability to load and wrap 3D dense matrix data structures.
* **Plane Projection:** Map 3D spatial plane coordinates to 2D projection matrices using vectorized slicing.
* **Video Rendering:** Compile sequential projection frames into an `.mp4` video file using `cv2.VideoWriter`.

### 3.2 Performance Requirements
* **Frame Rate:** The projection engine must maintain a minimum benchmark performance of 100 FPS.
* **Memory Efficiency:** Avoid scalar lookups (`get_voxel`) in tight loops; rely entirely on direct NumPy array slicing (`_data[x, y, z]`).

---

## 4. System Models & Architecture
- **`DenseMatrix3D`**: Manages underlying 3D numerical data.
- **`Plane`**: Defines spatial orientation and coordinates for slicing.
- **`CsvLoader`**: Responsible for reading CSV files and converting each collection of points into a `Plane` object.
- **`Projection`**: Core module executing the mathematical transformation from 3D to 2D.
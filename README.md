# 3D Medical Imaging Processing Pipeline

## 🚀 Quick Start: How to Run the Project

Follow these simple step-by-step instructions to run the project on your machine, even if you are new to Git and GitHub!

### Step 1: Clone the Repository
Open your terminal (or Command Prompt) and run:
```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd oop_proj_1
```

### Step 2: (Optional but Recommended) Create a Virtual Environment
It's good practice to run Python projects in an isolated environment:
* **On Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install all required Python packages (NumPy, OpenCV, pytest, nrrd, etc.):
```bash
pip install -r requirements.txt
```

### Step 4: Run the Benchmark & Video Generator
To run the automated tests, execute the high-speed MPR projection benchmark, and generate the output video (`mpr_output_video.mp4`):
```bash
pytest
```
> 💡 *Note: You can open the generated `mpr_output_video.mp4` file using your system's video player (such as VLC or Windows Media Player).*

---

## 📌 Problem Definition
In modern medical imaging, processing volumetric data (such as 3D scans) efficiently and reliably is a critical challenge. Medical professionals and researchers need robust tools to load, manipulate, and inspect multi-dimensional datasets (like NRRD files) without relying on heavy, closed-source proprietary software. 

## 🎯 Project Scope
The goal of this project is to build a modular, object-oriented pipeline in Python for processing 3D medical imaging data. 

### What the project covers:
- **Modular Architecture**: Strict separation of concerns between I/O operations (`VolumeLoader`), in-memory matrix management (`DenseMatrix3D`), visual verification (`matplot`), and projection engines (`Projection`).
- **Data Loading**: Efficient reading of 3D volume files in NRRD format into structured NumPy arrays.
- **Voxel-Level & Vectorized Operations**: Safe programmatic access (`get_voxel`/`set_voxel`) alongside high-performance NumPy vectorized array slicing for high-FPS plane projections.
- **Visual Inspection & Video Export**: Tools to render 2D slices and automatically compile projection frames into `.mp4` video format using OpenCV (`cv2`).
- **Automated Testing & Benchmarks**: Comprehensive test suites using `pytest` to validate functionality, matrix accuracy, and real-time FPS performance targets (100–300+ FPS).

### What is out of scope:
- Advanced clinical diagnosis or machine learning segmentation models.
- Support for non-standard or proprietary medical imaging formats beyond the defined dataset.
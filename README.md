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
### Step 4: Run the Main Pipeline (`Ex0.py`)
To execute the MPR projection pipeline, process the 3D volume using the plane coordinates from the CSV file, and generate the output video (`mpr_output_video.mp4`), run:

```bash
python Ex0.py <your nrrd file path> <your csv file path> mpr_output_video.mp4
```

### Step 5(optional): Run the Benchmark & Video Generator (with Print Outputs)
To run the automated tests, execute the high-speed MPR projection benchmark, see live print outputs directly in your terminal, and generate the output video (`mpr_output_video.mp4`):
```bash
python -m pytest -s
```
> 💡 *Note: You can open the generated `mpr_output_video.mp4` file using your system's video player (such as VLC or Windows Media Player).*

---



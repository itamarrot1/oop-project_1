import time
import pytest
import numpy as np
import cv2
# Import your classes and functions according to the project structure
from VolumeLoader import VolumeLoader
from DenseMatrix3D import DenseMatrix3D
from CSVPointLoader import CSVPointLoader
from Projection import project_plane_to_2d

@pytest.fixture
def load_test_data():
    """Fixture to load the volume and the planes once for the tests."""
    
    # ==========================================
    # <--- כאן שמים את הנתיבים לקבצים שלך --->
    # ==========================================
    nrrd_path = "data/nrrd/MRHead_1.nrrd"  # <--- החלף בנתיב לקובץ ה-NRRD שלך
    csv_path = "data/csvFiles/head.csv"         # <--- החלף בנתיב לקובץ ה-CSV שלך (עם 281 הנקודות)
    # ==========================================
    
    volumeLoader  = VolumeLoader(nrrd_path)   # Adjust method name if different in your class
    volume = volumeLoader.load()
    matrix = DenseMatrix3D(volume) 
    csvLoader = CSVPointLoader(csv_path) # Adjust method name if different
    planes = csvLoader.load_planes()
    
    return matrix, planes

import cv2
import time

def test_projection_fps_benchmark(load_test_data):
    volume, planes = load_test_data
    resolution = 256
    output_filename = "mpr_output_video.mp4"
    num_frames_per_plane = 20  # Number of repetitions per plane to create a realistic benchmark load
    total_frames = len(planes) + (len(planes) * (num_frames_per_plane - 1)) # סך הכל פרייימים מדויק
    
    # הגדרת כתיבת הווידאו באמצעות OpenCV
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filename, fourcc, 30, (resolution, resolution), isColor=False)
    
    print(f"\n🚀 Starting FPS benchmark & video generation for a total of {len(planes) * num_frames_per_plane} frames...")
    
    start_time = time.perf_counter()
    
    # Running the frames loop
    for rep in range(num_frames_per_plane):
        for plane in planes:
            projected_image = project_plane_to_2d(plane, volume, resolution)
            
            # Basic validation that the function returns a matrix of the correct size
            assert projected_image.shape == (resolution, resolution)
            
            # שמירת הפריים לסרטון רק בריצה הראשונה (כדי לא לייצר סרטון כפול וארוך מדי, או בכל ריצה אם תרצה)
            if rep == 0:
                frame = cv2.normalize(projected_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
                out.write(frame)

    end_time = time.perf_counter()
    
    # סגירת קובץ הווידאו
    out.release()
    
    elapsed_time = end_time - start_time
    fps = (len(planes) * num_frames_per_plane) / elapsed_time
    
    print(f"\n" + "=" * 40)
    print(f"          📊 FPS BENCHMARK RESULTS          ")
    print(f"=" * 40)
    print(f"⏱️ Total runtime: {elapsed_time:.4f} seconds")
    print(f"🎯 Average frame rate: {fps:.2f} FPS")
    print(f"🎥 Video successfully saved as '{output_filename}'")
    print(f"=" * 40)
    
    # Assignment performance threshold requirement (recommended >= 100 FPS)
    # assert fps >= 100, f"Performance too low: {fps:.2f} FPS (Target: >=100)"
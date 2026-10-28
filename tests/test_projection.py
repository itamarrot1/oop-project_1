import time
import pytest
import numpy as np
import cv2
# Import classes and functions directly from the main directory
from src.VolumeLoader import VolumeLoader
from src.DenseMatrix3D import DenseMatrix3D
from src.CSVPointLoader import CSVPointLoader
from src.Projection import project_plane_to_2d

@pytest.fixture
def load_test_data():
    """Fixture to load the volume and the planes once for the tests."""
    
    # ==========================================
    # <--- Set your file paths here --->
    # ==========================================
    nrrd_path = "data/nrrd/MRHead_1.nrrd"  # <--- Replace with the path to your NRRD file
    csv_path = "data/csvFiles/head.csv"         # <--- Replace with the path to your CSV file
    # ==========================================
    
    volumeLoader  = VolumeLoader(nrrd_path)
    volume = volumeLoader.load()
    matrix = DenseMatrix3D(volume) 
    csvLoader = CSVPointLoader(csv_path)
    planes = csvLoader.load_planes()
    
    return matrix, planes



def test_projection_fps_benchmark(load_test_data):
    volume, planes = load_test_data
    resolution = 256
    output_filename = "mpr_output_video.mp4"
    num_frames_per_plane = 20  # Number of repetitions per plane to create a realistic benchmark load
    
    # Configure video writer using OpenCV
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
            
            # Save the frame to the video only on the first iteration
            if rep == 0:
                frame = cv2.normalize(projected_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
                out.write(frame)

    end_time = time.perf_counter()
    
    # Release the video writer object
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
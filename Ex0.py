import sys
import os
import time
import cv2
import numpy as np
from src.VolumeLoader import VolumeLoader
from src.CSVPointLoader import CSVPointLoader
from src.DenseMatrix3D import DenseMatrix3D
from src.Projection import project_plane_to_2d

def main():
    # 1. Validate command line arguments (file.nrrd, file.csv, file.mp4)
    if len(sys.argv) < 4:
        print("Error: Missing arguments.")
        print("Usage: python Ex0.py <file.nrrd> <file.csv> <file.mp4>")
        sys.exit(1)

    nrrd_path = sys.argv[1]
    csv_path = sys.argv[2]
    output_mp4_path = sys.argv[3]

    print("=== Starting MPR Pipeline Execution ===")
    print(f"NRRD File: {nrrd_path}")
    print(f"CSV Points File: {csv_path}")
    print(f"Output Video: {output_mp4_path}")

    # 2. Verify that input files exist
    if not os.path.exists(nrrd_path):
        print(f"Error: NRRD file not found at '{nrrd_path}'")
        sys.exit(1)
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at '{csv_path}'")
        sys.exit(1)

    try:
        # 3. Load the NRRD volumetric data using VolumeLoader
        print("Loading volumetric data...")
        loader = VolumeLoader(nrrd_path)
        raw_volume = loader.load()
        
        # Wrap the volume data in a 3D matrix (DenseMatrix3D) as required by projection
        volume_matrix = DenseMatrix3D(raw_volume)
        print("Volume data loaded successfully.")

        # 4. Load the planes directly from the CSV file using CSVPointLoader
        print("Loading planes from CSV...")
        csv_loader = CSVPointLoader(csv_path)
        planes_list = csv_loader.load_planes()
        total_planes = len(planes_list)
        print(f"Loaded {total_planes} plane objects successfully.")

        # 5. Configure video writer (OpenCV VideoWriter) matching the test settings
        resolution = 256
        fps_target = 30
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_mp4_path, fourcc, fps_target, (resolution, resolution), isColor=False)

        # 6. Iterate through each plane, perform projection, measure time, and save to video
        print(f"\n🚀 Starting video generation and performance measurement for {total_planes} planes...")
        
        start_time = time.perf_counter()
        
        for idx, plane in enumerate(planes_list):
            projected_image = project_plane_to_2d(plane, volume_matrix, resolution=resolution)
            
            # Use OpenCV normalization identical to the test benchmark for visual quality
            frame = cv2.normalize(projected_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            # Write the frame to the video
            video_writer.write(frame)

        end_time = time.perf_counter()
        
        # Release the video writer resource
        video_writer.release()

        # 7. Calculate and print performance benchmark results
        elapsed_time = end_time - start_time
        actual_fps = total_planes / elapsed_time if elapsed_time > 0 else 0

        print(f"\n" + "=" * 40)
        print(f"          📊 PERFORMANCE RESULTS          ")
        print(f"=" * 40)
        print(f"⏱️ Total runtime: {elapsed_time:.4f} seconds")
        print(f"🎯 Actual frame rate: {actual_fps:.2f} FPS")
        print(f"🎥 Video successfully saved as '{output_mp4_path}'")
        print(f"=" * 40)

    except Exception as e:
        print(f"\nAn error occurred during execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
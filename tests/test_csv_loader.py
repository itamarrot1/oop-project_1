import os
import pytest
from src.CSVPointLoader import CSVPointLoader
from src.Plane import Plane
import numpy as np

FILENAME = "data/csvFiles/Ex0.csv"

def test_load_valid_csv():
    """Test that loads a valid CSV file and verifies that the data was read correctly row by row"""
    loader = CSVPointLoader(FILENAME)
    rows_data = loader.load_points()
    
    #Create a fit rows for test and Load all rows in :  Ex0.csv
    expected_rows = [
        # (Number of Point = 3)
        {
            "point_count": 3,
            "points": [
                (200.0, 200.0, 0.0),
                (0.0, 200.0, 400.0),
                (400.0, 200.0, 400.0),
            ]
        },
        # (Number of Point = 4)
        {
            "point_count": 4,
            "points": [
                (200.0, 0.0, 0.0),
                (200.0, 0.0, 500.0),
                (200.0, 400.0, 0.0),
                (200.0, 400.0, 500.0),
            ]
        },
        #  (Number of Point = 3)
        {
            "point_count": 3,
            "points": [
                (200.0, 200.0, -30.0),
                (-50.0, 200.0, 400.0),
                (400.0, 250.0, 400.0),
            ]
        },
        # (Number of Point = 4)
        {
            "point_count": 4,
            "points": [
                (200.0, 50.0, 0.0),
                (200.0, 0.0, 500.0),
                (200.0, 350.0, 0.0),
                (200.0, 400.0, 500.0),
            ]
        }
    ]
    
    # Verify that rows were loaded
    assert len(rows_data) > 0
    assert len(rows_data) == len(expected_rows), \
        f"Expected {len(expected_rows)} rows, but got {len(rows_data)} rows from CSV."
        
    print(f"\nSuccessfully loaded {len(rows_data)} rows from CSV.")
    
    # Iterate through rows using a standard index loop
    for row_index in range(len(expected_rows)):
        actual_row = rows_data[row_index]
        expected_row = expected_rows[row_index]
        
        # Verify point count from the first column
        assert actual_row["point_count"] == expected_row["point_count"], \
            f"Mismatch in point count at row {row_index + 1}! Expected {expected_row['point_count']}, but got {actual_row['point_count']}."
        
        # Verify points list length
        assert len(actual_row["points"]) == len(expected_row["points"]), \
            f"Mismatch in points list length at row {row_index + 1}!"
            
        # Iterate through points within the row using a standard index loop
        for point_index in range(len(expected_row["points"])):
            actual_point = actual_row["points"][point_index]
            expected_point = expected_row["points"][point_index]
            
            print(f"Row {row_index + 1}, Point {point_index}: actual={actual_point}, expected={expected_point}")
            
            assert actual_point == expected_point, \
                f"Mismatch at row {row_index + 1}, point {point_index + 1}! Expected {expected_point}, but got {actual_point}."
                
    print("\nAll 4 rows and their points verified successfully!\n")


def test_file_not_found():
    """Test that the class raises an error when the file name does not exist"""
    loader = CSVPointLoader("non_existent_file.csv")
    with pytest.raises(FileNotFoundError):
        loader.load_points()



def test_load_planes():
    """Test that loads planes using load_planes() and verifies Plane objects and NumPy integration"""
    loader = CSVPointLoader(FILENAME)
    planes = loader.load_planes()
    
    # Verify that planes were loaded successfully from Ex0.csv (expects 4 planes)
    assert len(planes) == 4, f"Expected 4 planes, but got {len(planes)}"
    
    # Verify each item is an instance of Plane
    for index, plane in  enumerate(planes):
        print(f"\n this is the {index+1} plane , he include {plane.point_count} points")
        assert isinstance(plane, Plane)
        
    # Check specific details for the first plane (should have 3 points)
    first_plane = planes[0]
    assert first_plane.point_count == 3
    
    np_points = first_plane.get_points_as_numpy()
    assert isinstance(np_points, np.ndarray)
    assert np_points.dtype == np.float32
    assert np_points.shape == (3, 3)
    
    # Check specific details for the second plane (should have 4 points)
    second_plane = planes[1]
    assert second_plane.point_count == 4
    assert second_plane.get_points_as_numpy().shape == (4, 3)
    
    print(f"\nSuccessfully verified {len(planes)} Plane objects with NumPy arrays!")
import csv
import os
from typing import List, Tuple, Dict, Any
from src.Plane import Plane 

class CSVPointLoader:
    """
    Handles loading and parsing of 3D spatial points from CSV files.
    Supports multi-point rows (ID in column 0, followed by X, Y, Z triplets).
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_points(self) -> List[Dict[str, Any]]:
        """
        Reads a CSV file where each row has an ID (number of points) followed by coordinate triplets.
        :return: A list of dictionaries, each containing the expected point count and the list of loaded (x, y, z) coordinates for that row.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"CSV file not found at: {self.file_path}")

        rows_data: List[Dict[str, Any]] = []

        with open(self.file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            for row_index, row in enumerate(reader):
                cleaned_row = [item.strip() for item in row if item.strip()]
                if not cleaned_row:
                    continue

                # Skip the header row (index 0)
                if row_index == 0:
                    continue

                try:
                    expected_count = int(cleaned_row[0])
                except ValueError:
                    continue

                coordinate_values = cleaned_row[1:]
                row_points: List[Tuple[float, float, float]] = []

                for i in range(0, len(coordinate_values), 3):
                    if i + 2 < len(coordinate_values):
                        try:
                            x = float(coordinate_values[i])
                            y = float(coordinate_values[i+1])
                            z = float(coordinate_values[i+2])
                            row_points.append((x, y, z))
                        except ValueError:
                            continue

                rows_data.append({
                    "point_count": expected_count,
                    "points": row_points
                })

        return rows_data

    def load_planes(self) -> List[Plane]:
        """
        Loads the CSV data and converts each row into a distinct Plane object,
        ensuring geometric separation and validation (minimum 3 points per plane).
        """
        raw_rows = self.load_points()
        planes_list = []
        
        for row in raw_rows:
            points = row.get("points", [])
            if points:
                # Creates a Plane object, which internally validates and converts to a fast NumPy array
                plane_obj = Plane(points)
                planes_list.append(plane_obj)
                
        return planes_list
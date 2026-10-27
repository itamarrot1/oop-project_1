import numpy as np
from typing import List, Tuple, Union

class Plane:
    """
    Represents a 3D geometric plane defined by 3 or more points 
    (e.g., triangles, trapezoids, or polygons lying on the same plane).
    """
    def __init__(self, points: Union[List[Tuple[float, float, float]], np.ndarray]):
        # Use np.asarray to prevent redundant copying if 'points' is already a NumPy array (Zero-copy)
        self.points = np.asarray(points, dtype=np.float32)
        
        # Validate that the plane has at least 3 points
        if self.points.shape[0] < 3:
            raise ValueError(f"A plane must be defined by at least 3 points. Received only {self.points.shape[0]} points.")
    
    def get_points_as_numpy(self) -> np.ndarray:
        """
        Returns all points of the plane as a continuous NumPy array of shape (N, 3),
        optimized for high-performance vectorized computations.
        """
        return self.points

    @property
    def point_count(self) -> int:
        """Returns the number of points defining this plane."""
        return self.points.shape[0]
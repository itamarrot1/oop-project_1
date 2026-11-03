import numpy as np


class DenseMatrix3D():

    def __init__(self, data: np.ndarray):
        """Constructor receives a pre-loaded 3D NumPy array."""
        self._data = data

    @property
    def shape(self) -> tuple[int, int, int]:
        # Returns the dimensions of the NumPy array (sx, sy, sz)
        return self._data.shape
    
    def _check_bounds(self, x: int, y: int, z: int) -> None:
        """Helper method to validate that coordinates are within matrix bounds."""
        sx, sy, sz = self.shape
        if not (0 <= x < sx and 0 <= y < sy and 0 <= z < sz):
            raise IndexError(
                f"Coordinates ({x}, {y}, {z}) are out of bounds for shape {self.shape}"
            )
        
    def get_voxel(self, x: int, y: int, z: int) -> int:
        """Retrieves a voxel value after validating bounds."""
        self._check_bounds(x, y, z)
        return int(self._data[x, y, z])

    def get_voxels(self, x_indices: np.ndarray, y_indices: np.ndarray, z_indices: np.ndarray) -> np.ndarray:
        """Retrieves a batch of voxel values for vectorized indices safely."""
        return self._data[x_indices, y_indices, z_indices]

    def set_voxel(self, x: int, y: int, z: int, value: int) -> None:
        # Updates a voxel value in the NumPy array
        self._data[x, y, z] = value



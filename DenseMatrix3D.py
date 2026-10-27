import numpy as np


class DenseMatrix3D():

    def __init__(self, data: np.ndarray):
        """Constructor receives a pre-loaded 3D NumPy array."""
        self._data = data

    @property
    def shape(self) -> tuple[int, int, int]:
        # Returns the dimensions of the NumPy array (sx, sy, sz)
        return self._data.shape

    def get_voxel(self, x: int, y: int, z: int) -> int:
        # Retrieves a voxel value directly from the NumPy array
        return int(self._data[x, y, z])

    def set_voxel(self, x: int, y: int, z: int, value: int) -> None:
        # Updates a voxel value in the NumPy array
        self._data[x, y, z] = value



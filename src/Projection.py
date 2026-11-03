import numpy as np
import src.Plane as Plane
import src.DenseMatrix3D as DenseMatrix3D


def project_plane_to_2d(plane: Plane, volume: DenseMatrix3D, resolution: int = 256) -> np.ndarray:
    """
    Projects a 3D plane into a 2D matrix of a predefined size.
    Uses NumPy for fast parallelized vector calculations without slow loops.
    """
    # 1. Extract plane points as a NumPy array
    points = plane.get_points_as_numpy()
    if points.shape[0] < 3:
        raise ValueError("A plane must be defined by at least 3 points.")

    # 2. Define origin point and direction vectors on the plane
    origin = points[0]
    u_vector = points[1] - origin
    v_vector = points[2] - origin

    # 3. Create a 2D coordinate grid with predefined resolution
    u_coords = np.linspace(0, 1, resolution, dtype=np.float32)
    v_coords = np.linspace(0, 1, resolution, dtype=np.float32)
    uu, vv = np.meshgrid(u_coords, v_coords)

    # 4. Parallelized vector mapping to 3D world coordinates
    # Shape: (resolution, resolution, 3)
    grid_3d = origin + (uu[..., np.newaxis] * u_vector) + (vv[..., np.newaxis] * v_vector)

    # 5. Extract volume dimensions for bounds checking
    vol_shape = volume.shape  # or volume._data.shape
    valid_mask = (
        (grid_3d[..., 0] >= 0) & (grid_3d[..., 0] < vol_shape[0]) &
        (grid_3d[..., 1] >= 0) & (grid_3d[..., 1] < vol_shape[1]) &
        (grid_3d[..., 2] >= 0) & (grid_3d[..., 2] < vol_shape[2])
    )
    # Convert to integer indices with clipping to handle points outside the volume
    x_indices = np.clip(np.round(grid_3d[..., 0]), 0, vol_shape[0] - 1).astype(np.intp)
    y_indices = np.clip(np.round(grid_3d[..., 1]), 0, vol_shape[1] - 1).astype(np.intp)
    z_indices = np.clip(np.round(grid_3d[..., 2]), 0, vol_shape[2] - 1).astype(np.intp)

    # 6. Vectorized voxel sampling from the volume matrix
    projected_image = volume._data[x_indices, y_indices, z_indices].copy()
    projected_image[~valid_mask] = 0

    return projected_image
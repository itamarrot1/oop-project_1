# 🧠 Core Algorithm: Multi-Planar Reconstruction (MPR) Projection

The core objective of this algorithm is to take a 3D volumetric dataset (such as an MRI or CT scan in NRRD format) and slice through it at an arbitrary spatial angle defined by anatomical points, extracting a clear 2D cross-sectional image.

To achieve maximum performance and hit high frame rates (>100 FPS), the entire pipeline is **fully vectorized using NumPy**, completely avoiding slow Python `for` loops.

---

## 🔍 Step-by-Step Breakdown

### 1. Plane Validation & Point Extraction
The algorithm receives a `Plane` object defined by a set of spatial coordinates (sourced from the CSV file). It verifies that the plane contains at least 3 points to uniquely define a flat surface in 3D space:
```python
points = plane.get_points_as_numpy()
if points.shape[0] < 3:
    raise ValueError("A plane must be defined by at least 3 points.")
```

### 2. Defining a Local Coordinate System (Vectors)
It selects the first point as an **origin point** ($origin$) and calculates two direction vectors on the plane ($\vec{u}$ and $\vec{v}$) by subtracting the origin from two adjacent points:
$$\vec{u} = \text{point}_1 - \text{origin}$$
$$\vec{v} = \text{point}_2 - \text{origin}$$

```python
origin = points[0]
u_vector = points[1] - origin
v_vector = points[2] - origin
```

### 3. Creating a 2D Grid ($u, v$)
Generates a normalized 2D grid of coordinates based on the target image resolution (default: $256 \times 256$) using `np.linspace` and `np.meshgrid`:
```python
u_coords = np.linspace(0, 1, resolution, dtype=np.float32)
v_coords = np.linspace(0, 1, resolution, dtype=np.float32)
uu, vv = np.meshgrid(u_coords, v_coords)
```

### 4. Vectorized Mapping to 3D World Coordinates
Transforms the 2D grid points into actual 3D spatial coordinates within the volumetric space using linear combinations of the directional vectors:
$$\text{Grid}_{3D} = \text{origin} + (u \cdot \vec{u}) + (v \cdot \vec{v})$$

```python
grid_3d = origin + (uu[..., np.newaxis] * u_vector) + (vv[..., np.newaxis] * v_vector)
```

### 5. Bounds Checking & Index Clipping
Rounds the 3D spatial coordinates to discrete voxel indices ($x, y, z$). Uses `np.clip` to ensure that any calculated points falling slightly outside the physical boundaries of the 3D volume matrix are safely clamped to the edge limits, preventing index out-of-bounds errors:
```python
vol_shape = volume.shape
x_indices = np.clip(np.round(grid_3d[..., 0]), 0, vol_shape[0] - 1).astype(np.intp)
y_indices = np.clip(np.round(grid_3d[..., 1]), 0, vol_shape[1] - 1).astype(np.intp)
z_indices = np.clip(np.round(grid_3d[..., 2]), 0, vol_shape[2] - 1).astype(np.intp)
```

### 6. Vectorized Voxel Sampling
Samples pixel intensity values directly from the 3D volume matrix in a single vectorized operation using advanced NumPy multidimensional indexing, returning the final 2D slice ready for rendering or video output:
```python
projected_image = volume._data[x_indices, y_indices, z_indices]
return projected_image
```

---

## ⚡ Key Performance Considerations
* **Zero Python Loops:** By relying entirely on NumPy's broadcast mechanisms and array slicing, the transformation is offloaded to optimized C/Fortran routines.
* **Compact Data Types:** Utilizing `np.float32` and `uint8` data types ensures low memory bandwidth usage and maintains peak execution speeds.
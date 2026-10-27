import numpy as np
import Plane
import DenseMatrix3D


def project_plane_to_2d(plane :Plane , volume: DenseMatrix3D  , resolution: int = 256) -> np.ndarray:
    """
    מבצע הטלה של מישור תלת-ממדי למטריצה דו-ממדית בגודל קבוע מראש.
    משתמש ב-NumPy לחישוב ווקטורי מקבילי מהיר ללא לולאות איטיות.
    """
    # 1. שליפת נקודות המישור כמערך NumPy
    points = plane.get_points_as_numpy()
    if points.shape[0] < 3:
        raise ValueError("A plane must be defined by at least 3 points.")

    # 2. הגדרת נקודת מוצא (Origin) וווקטורי כיוון על המישור
    origin = points[0]
    u_vector = points[1] - origin
    v_vector = points[2] - origin

    # 3. יצירת רשת קואורדינטות דו-ממדית בגודל קבוע מראש
    u_coords = np.linspace(0, 1, resolution, dtype=np.float32)
    v_coords = np.linspace(0, 1, resolution, dtype=np.float32)
    uu, vv = np.meshgrid(u_coords, v_coords)

    # 4. מיפוי ווקטורי מקבילי לקואורדינטות במרחב התלת-ממדי (3D World Coordinates)
    # Shape: (resolution, resolution, 3)
    grid_3d = origin + (uu[..., np.newaxis] * u_vector) + (vv[..., np.newaxis] * v_vector)

    # 5. חילוץ ממדי הנפח לצורך בקרת גבולות (Bounds Checking)
    # בהנחה שלמחלקת DenseMatrix3D יש גישה לממדים או למערך הפנימי
    vol_shape = volume.shape  # או volume._data.shape

    # המרה לאינדקסים שלמים, תוך הגבלה (Clipping) כדי לטפל בנקודות שמחוץ לנפח
    x_indices = np.clip(np.round(grid_3d[..., 0]), 0, vol_shape[0] - 1).astype(np.intp)
    y_indices = np.clip(np.round(grid_3d[..., 1]), 0, vol_shape[1] - 1).astype(np.intp)
    z_indices = np.clip(np.round(grid_3d[..., 2]), 0, vol_shape[2] - 1).astype(np.intp)

    # 6. דגימה ווקטורית של הווקסלים מתוך מטריצת הנפח
    projected_image = volume._data[x_indices, y_indices, z_indices]

    return projected_image
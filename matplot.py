# בתוך קובץ matplot.py
import matplotlib.pyplot as plt

def show_matrix_slice(matrix_instance, z_index, title="Matrix Slice"):
    """
    מקבל את אובייקט ה-DenseMatrix3D ומציג פרוסה מתוכו (כולל שינויים שבוצעו בזיכרון).
    """
    # גישה למטריצה מתוך אובייקט ה-DenseMatrix3D (נניח שהיא שמורה ב- _data או בצורה דומה)
    data = matrix_instance._data  # או דרך property אם הגדרת
    
    plt.figure(figsize=(6, 6))
    plt.imshow(data[:, :, z_index], cmap='gray', interpolation='nearest')
    plt.colorbar(label='Voxel Value')
    plt.title(f"{title} | Slice Z = {z_index}")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()
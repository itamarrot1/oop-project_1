import numpy as np
import nrrd

size = 50
cube = np.zeros((size, size, size), dtype=np.uint8)

# יצירת רשת קואורדינטות למרכז הקוביה
Y, X = np.ogrid[:size, :size]
center = size / 2

# מעבר על השכבות ויצירת צורות שונות בכל טווח
for z in range(5, 45):
    if z < 18:
        # בשכבות הראשונות: עיגול שגדל
        radius = z - 3
        mask = (X - center)**2 + (Y - center)**2 <= radius**2
        cube[mask, z] = 1
        
    elif 18 <= z < 32:
        # באמצע: ריבוע שמשנה את גודלו
        margin = abs(25 - z) + 5
        cube[margin:size-margin, margin:size-margin, z] = 1
        
    else:
        # בשכבות האחרונות: צורת יהלום/מעוין שקטנה
        dist = np.abs(X - center) + np.abs(Y - center)
        max_dist = 45 - z
        mask = dist <= max_dist
        cube[mask, z] = 1

# שמירה לקובץ NRRD חדש
nrrd.write('rich_shapes_cube.nrrd', cube)
print("נוצר קובץ עם צורות מגוונות!")
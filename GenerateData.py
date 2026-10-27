import numpy as np

def generate_realistic_view_files():
    """
    Generates realistic CSV files for front and side views containing 
    150 sequential slices each, mimicking a 3D Slicer slider movement.
    """
    header = "Number of Point,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4"
    
    # 1. Generate Front View (Coronal - sliding along the Y axis)
    front_lines = [header]
    y_steps = np.linspace(10.0, 490.0, 150) # 150 progressive slices
    
    for y in y_steps:
        # 4-point plane definition moving step by step along Y
        row = f"4,0,{y:.2f},0,500,{y:.2f},0,500,{y:.2f},500,0,{y:.2f},500"
    
    with open("front_view.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(front_lines))

    # 2. Generate Side View (Sagittal - sliding along the X axis)
    side_lines = [header]
    x_steps = np.linspace(10.0, 490.0, 150) # 150 progressive slices
    
    for x in x_steps:
        # 4-point plane definition moving step by step along X
        row = f"4,{x:.2f},0,0,{x:.2f},500,0,{x:.2f},500,500,{x:.2f},0,500"
        side_lines.append(row)
        
    with open("side_view.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(side_lines))
        
    print("Successfully generated 'front_view.csv' and 'side_view.csv' with 150 slices each!")

if __name__ == "__main__":
    generate_realistic_view_files()
import numpy as np
import nrrd
import os

class VolumeLoader:
    """
    this class is charge of reading a file of 3D object
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.volume_data = None
        self.header = None


    def load(self):
        """
       load the NRRD file
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"file {self.file_path} have not found")
            
        self.volume_data, self.header = nrrd.read(self.file_path)        
        return self.volume_data

    def get_header(self):
        """Returns the header of the loaded NRRD file."""
        return self.header


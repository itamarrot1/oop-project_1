import pytest
from VolumeLoader import VolumeLoader
from DenseMatrix3D import DenseMatrix3D

@pytest.fixture
def data():
    """Fixture that loads the 3D matrix data once for all tests."""
    loader = VolumeLoader("data/nrrd/MRHead_1.nrrd")
    raw_data = loader.load()
    matrix = DenseMatrix3D(raw_data)
    return matrix

def test_shape(data):
    """Test 1: Verify that the shape property returns correct matrix dimensions."""
    assert data.shape == (256, 256, 130)
    print(f"test pass the shape is {data.shape}")

def test_get_voxel(data):
    """Test 2: Verify that get_voxel retrieves the expected value from a specific coordinate."""
    val = data.get_voxel(15, 25, 25)
    assert val == 3

def test_set_voxel(data):
    """Test 3: Verify set_voxel correctly updates a value at given coordinate."""
    coord = (25, 25, 25)
    new_value = 0    
    data.set_voxel(coord[0], coord[1], coord[2], new_value)
    assert data.get_voxel(*coord) == new_value
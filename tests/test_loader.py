import pytest
from src.VolumeLoader import VolumeLoader


@pytest.fixture
def volume_filename():
    """Fixture that provides a default file path for testing."""
    return "data/nrrd/MRHead_1.nrrd"


def test_load_volume(volume_filename):
    """Test function to load a volume file using VolumeLoader, utilizing a fixture for the filename."""
    try:
        # 1. Create an instance of the volume loader with the filename from the fixture
        loader = VolumeLoader(volume_filename)
        
        # 2. Load the data from disk
        data = loader.load()
        
        # Verify that data and header are successfully loaded
        assert data is not None, "Volume data should not be None."
        assert loader.get_header() is not None, "Header should not be None."
        
        # Print specific header information for verification
        data_type = loader.get_header().get('type')
        print(f"Data type for {volume_filename}: {data_type}")

        # 3. Basic validity checks and success message
        print(f"File '{volume_filename}' loaded successfully!")

        return loader, data

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred during loading: {e}")
        raise
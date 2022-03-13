from importlib_resources import files
import pycounts.data

def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    data_file_path = files('pycounts.data').joinpath('flatland.txt').read_text()
    return data_file_path
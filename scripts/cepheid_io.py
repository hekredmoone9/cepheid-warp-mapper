import pandas as pd

def load_catalog(filepath: str) -> pd.DataFrame:
    """
    Load a Cepheid data file (expected to be a CSV) and return it as a Pandas DataFrame.

    The data file should contain columns for `RA`, `Dec`, `Period`, and `Extinction`.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file.
    
    Returns
    -------
    pd.DataFrame
        DataFrame containing the Cepheid catalog.
    """
    pass

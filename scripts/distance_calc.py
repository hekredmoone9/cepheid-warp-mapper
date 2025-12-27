import numpy as np
import pandas as pd

def calculate_distances(cepheid_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate distances to Cepheid variable stars using the Period-Luminosity relation.
    
    Parameters
    ----------
    cepheid_df : pd.DataFrame
        DataFrame containing Cepheid data with at least columns:
        - 'Period' : pulsation period in days
        - 'Extinction' : extinction in magnitudes
        - 'RA', 'Dec' : coordinates (optional, for reference)
    
    Returns
    -------
    pd.DataFrame
        Input DataFrame augmented with columns:
        - 'Absolute_Magnitude' : absolute magnitude calculated via PL relation
        - 'Distance_modulus' : distance modulus (magnitude)
        - 'Distance_pc' : distance in parsecs
        - 'Distance_error_pc' : error on distance (propagated from uncertainties)
    
    Notes
    -----
    Uses the classical Period-Luminosity relation for Galactic Cepheids:
        M = a * log10(P) + b
    with appropriate coefficients (e.g., from Gaia DR3 calibration).
    Extinction correction applied: m0 = m - A (where A is extinction).
    Distance modulus: mu = m0 - M.
    Distance: d = 10^(mu/5 + 1) parsecs.
    
    Error propagation should consider uncertainties in period, extinction,
    and PL relation coefficients.
    """
    # TODO: implement the Period-Luminosity relation
    # Example coefficients (placeholder values - replace with actual calibration)
    a = -2.43  # slope
    b = -1.43  # zero-point
    
    # TODO: calculate absolute magnitude M = a * log10(P) + b
    # TODO: apply extinction correction to obtain apparent magnitude m0
    # TODO: compute distance modulus mu = m0 - M
    # TODO: compute distance in parsecs
    # TODO: propagate errors
    
    # For now, return the input DataFrame with empty distance columns
    result = cepheid_df.copy()
    result['Absolute_Magnitude'] = np.nan
    result['Distance_modulus'] = np.nan
    result['Distance_pc'] = np.nan
    result['Distance_error_pc'] = np.nan
    
    return result
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def equatorial_to_galactocentric(ra_deg: float, dec_deg: float, distance_pc: float):
    """
    Convert equatorial coordinates (RA, Dec, distance) to galactocentric
    Cartesian coordinates (X, Y, Z) in parsecs.
    
    Parameters
    ----------
    ra_deg : float or array-like
        Right ascension in degrees.
    dec_deg : float or array-like
        Declination in degrees.
    distance_pc : float or array-like
        Distance in parsecs.
    
    Returns
    -------
    X, Y, Z : arrays of same shape as inputs
        Galactocentric coordinates (parsecs), with the Sun at (X, Y, Z) = (0, 0, 0)
        and the Galactic centre in the +X direction.
        
    Notes
    -----
    This is a simplified transformation. For precise work, use astropy.coordinates.
    """
    # TODO: implement proper coordinate transformation using astropy
    # For now, return dummy values
    return np.zeros_like(ra_deg), np.zeros_like(dec_deg), np.zeros_like(distance_pc)


def plot_3d_distribution(cepheid_df: pd.DataFrame, output_path: str = None):
    """
    Create a 3D scatter plot of Cepheid positions in galactocentric coordinates.
    
    Parameters
    ----------
    cepheid_df : pd.DataFrame
        DataFrame containing at least columns 'RA', 'Dec', 'Distance_pc'.
        Optional columns: 'Period', 'Extinction' for colour coding.
    output_path : str, optional
        If provided, save the figure to this path (e.g., 'figures/cepheids_3d.png').
    
    Returns
    -------
    fig : matplotlib.figure.Figure
        The created figure.
    ax : matplotlib.axes.Axes
        The 3D axes.
    """
    # Convert coordinates
    X, Y, Z = equatorial_to_galactocentric(
        cepheid_df['RA'].values,
        cepheid_df['Dec'].values,
        cepheid_df['Distance_pc'].values
    )
    
    # Create figure
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter plot; colour by period if available, else by distance
    if 'Period' in cepheid_df.columns:
        colors = cepheid_df['Period']
        cmap = 'viridis'
        label = 'Period (days)'
    else:
        colors = cepheid_df['Distance_pc']
        cmap = 'plasma'
        label = 'Distance (pc)'
    
    sc = ax.scatter(X, Y, Z, c=colors, cmap=cmap, s=20, alpha=0.7)
    
    # Add colour bar
    cbar = fig.colorbar(sc, ax=ax, pad=0.1)
    cbar.set_label(label)
    
    # Labels and title
    ax.set_xlabel('X (pc) → Galactic Centre')
    ax.set_ylabel('Y (pc)')
    ax.set_zlabel('Z (pc)')
    ax.set_title('3D distribution of Galactic Cepheids')
    
    # Optional: add a reference plane for the galactic disc (Z = 0)
    # (could be more sophisticated to show warping)
    xx, yy = np.meshgrid([X.min(), X.max()], [Y.min(), Y.max()])
    zz = np.zeros_like(xx)
    ax.plot_surface(xx, yy, zz, alpha=0.2, color='gray')
    
    # Save if requested
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Figure saved to {output_path}")
    
    return fig, ax


if __name__ == '__main__':
    # Example usage (requires data from previous tasks)
    print("This script visualizes the 3D distribution of Cepheids.")
    print("First run Task 1 and Task 2 to produce a catalog with distances.")
    print("Then call plot_3d_distribution(df, 'figures/cepheids_3d.png')")
    pass
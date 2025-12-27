# Project Tasks

This document outlines the three main tasks for the collaborative project "Mapping the Milky Way's Warp with Cepheid Variables". Each task corresponds to a GitHub issue that will be created shortly.

## Task 1: Implement the Data Loading Function
**Assigned to:** Junior Researcher 1 (@junior1)  
**Status:** Pending  
**Description:** Complete the function `load_catalog` in `scripts/cepheid_io.py` that loads the Cepheid catalog from a CSV file.

### Requirements
- The function should read a CSV file with columns: `RA`, `Dec`, `Period`, `Extinction`.
- It should return a pandas DataFrame with appropriate data types.
- Include basic error handling (e.g., file not found, missing columns).
- Write a simple test to verify the function works with a sample data file.

### Deliverables
- Updated `scripts/cepheid_io.py` with a working `load_catalog` function.
- A small test script (or docstring example) demonstrating its usage.

---

## Task 2: Calculate Distances Using the Period–Luminosity Relation
**Assigned to:** Junior Researcher 2 (@junior2)  
**Status:** Pending  
**Description:** Create a script `scripts/distance_calc.py` that calculates distances to each Cepheid using the Period–Luminosity relation and extinction corrections.

### Requirements
- Implement the classical PL relation: `M = a * log10(P) + b` with appropriate coefficients (to be determined from literature).
- Apply extinction correction to obtain the dereddened apparent magnitude.
- Compute the distance modulus and convert it to a distance in parsecs.
- Propagate uncertainties (if available) to estimate distance errors.
- The function should accept a DataFrame produced by Task 1 and return the same DataFrame augmented with distance columns.

### Deliverables
- A complete `scripts/distance_calc.py` with a well‑documented `calculate_distances` function.
- A Jupyter notebook or script that demonstrates the distance calculation on a sample dataset.

---

## Task 3: Visualize the 3D Distribution and Warp
**Assigned to:** Both researchers (collaborative)  
**Status:** Pending  
**Description:** Create a script `scripts/visualize_warp.py` that reads the processed catalog (with distances) and generates a 3D plot showing the spatial distribution of the Cepheids and the galactic warp.

### Requirements
- Convert equatorial coordinates (RA, Dec, distance) to galactocentric coordinates (X, Y, Z).
- Produce a 3D scatter plot (using Matplotlib or Plotly) colour‑coded by some property (e.g., period, distance).
- Overplot a model of the galactic plane (optional) to highlight the warp.
- Save the figure in the `figures/` directory.

### Deliverables
- A working visualization script.
- At least one high‑quality figure that clearly illustrates the warp of the Milky Way disc.

---

## Notes
- All code must be documented and follow PEP 8 style guidelines.
- Each task should be developed in a separate branch and merged via a Pull Request.
- The mentor will review each PR and provide feedback before merging.

These tasks will be mirrored as GitHub issues with the same assignments. Please refer to the issues for the most up‑to‑date information and discussion.
A percolation model using an n-by-n grid of sites. Each site is either open or blocked. The system percolates if there is a connection of open sites possible from top edge to bottom.
Each site can be independently open with a probability p. There is a threshold probability p* such that p above this would almost always percolate otherwise almost never percolates.

Here p* is estimated using Monte Carlo simulation, as follows:
*   Initialize all sites to be blocked.
*   Repeat the following unil system percolates:
    *   Choose a blocked site randomly
    *   Open the choosen site
*   The fraction of sites that are open provides an estimate of the percolation threshold.
Monte Carlo simulation takes t samples.

Here a 50x50 grid has been used and took 10,000 samples.

The file `model.py` has a class for the grid with all the required functions.

The file `create-data.py` creates the data using the model and creates `data.csv`.

`notebook.ipynb` is used to for analysis of `data.csv`.

Finally the threshold probability is found to be 0.59241956, with a standard deviation of 0.026125203.
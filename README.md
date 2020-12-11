A percolation model using an n-by-n grid of sites. Each site is either open or blocked. The system percolates if there is a connection of open sites possible from top edge to bottom.
Each site can be independently open with a probability p. There is a threshold probability p* such that p above this would almost always percolate otherwise almost never percolates.
Here p* is estimated using Monte Carlo simulation, as follows:
*   Initialize all sied to be blocked.
*   Repeat the following unil system percolates:
    *   Choose a blocked site randomly
    *   Open the choosen site
*   The fraction of sites that are open provides an estimate of the percolation threshold.
Monte Carlo simulation takes t samples.

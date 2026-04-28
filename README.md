# Computational Economics

A collection of my projects and experiments focused on computational economics, market microstructure, financial engineering, and applied mathematics. The repository contains both sequential pipelines (e.g., synthetic market data generation -> order book rebuild -> execution -> risk) and standalone implementations of mathematical theory and algorithms.

## Setup and Usage

### Prerequisites
- Python 3.8 or higher
- `pip` (or an equivalent Python package manager)
- (Optional but recommended) A virtual environment (`venv` or `conda`) to isolate dependencies

### Installation
Clone the repository and install dependencies:
```bash
    git clone https://github.com/mazidhee/computational-economics.git
    cd computational-economics
    pip install -r requirements.txt
```

## Structure

The repository is organized into two main sections:
1. A sequential computational pipeline of components that often run together
2. A maths sandbox of standalone notebooks and scripts for theory and experimentation

### Part 1: Computational Economics

Some components are designed to run concurrently or in a particular order. Use the exact folder names below when navigating the repository.

- Folder 1: `geometric-brownian-motion`

    Run this first to start the synthetic exchange data stream.

    cd "geometric-brownian-motion"
    python "stochastic_ generator.py"

- Folder 2: `microstructure-state-rebuilder`

    Consumes raw JSON deltas and reconstructs the Limit Order Book (L2) and top-of-book.

    cd "microstructure-state-rebuilder"
    python state_rebuilder.py


- Folder 3: `order-flow-imbalance`

    cd "order flow imbalance"
    python ofi_calculator.py

- Folder 4: `twap-vwap-algo`

    cd "twap-vwap-algo"
    python vwap_execution.py

- Folder 5: `zero-intelligence-market`

    cd "zero-intelligence-market"
    python agent_simulation.py

- Folder 6: `rolling-value`

    cd "rolling-value"
    python risk_manager.py


### Part 2: Mathematical Sandbox & Explorations

This section contains standalone scripts and notebooks created while learning and experimenting with mathematical concepts. These do not depend on the pipeline above and are safe to run independently.

- `calculus` - numerical derivatives, integration, optimization examples
- `linear-algebra` - matrix utilities, eigenvalue computations, numerical solvers
- `statistics-probability` - distributions, Monte Carlo simulations, hypothesis testing
- `qs` - algorithmic puzzles, translated proofs, and question solutions


## Notes & Recommendations
- Use a virtual environment before installing dependencies to avoid version conflicts.
- If you plan to run the full pipeline, start the data generator first, then bring up downstream consumers (L2 rebuilder, OFI, execution algos, etc.).
- Many components expect a continuous stream of JSON deltas or simulated ticks; inspect each folder's README or header comments for per-script configuration.


## Contribution & Contact
Contributions are welcome. If you'd like to suggest improvements or report an issue, please open an issue or submit a pull request on the GitHub repository.


---

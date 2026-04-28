# Zero-Intelligence Market (Agent-Based Modeling)

Purpose

A computational economics experiment inspired by Gode & Sunder to test price discovery in a continuous double auction populated by simple "zero-intelligence" agents.

Suggested filename and usage

```bash
cd "zero intelligence market"
python agent_simulation.py --n-buyers 10 --n-sellers 10 --rounds 1000
```

Behavior
- Create buyer and seller agents with random reservation prices
- Let agents submit random bids/asks to a central matching routine
- Track executed prices and visualize convergence (matplotlib)

Dependencies (typical)
- Python 3.8+
- numpy, matplotlib (optional)


# TWAP / VWAP Execution Algorithm 

Purpose

This component simulates institutional execution strategies (TWAP/VWAP) by slicing large parent orders into smaller child orders to minimize market impact. The engine should monitor the live market stream (from the L2 rebuilder) and adapt execution timing and size to the observed liquidity.

Suggested filename and usage

```bash
cd "execution algo"
python vwap_execution.py --parent-size 10000 --duration 3600
```

Typical behavior
- Accept a parent order (size, side, time horizon)
- Slice into child orders (fixed or adaptive) and submit to a simulator or the live rebuilder
- Track execution vs VWAP benchmark and report slippage

Dependencies (typical)
- Python 3.8+
- numpy, pandas (optional)

Integration
- Run `geometric brownian motion` and `microstructure state rebuilder` first for market data.
- The execution engine should subscribe to the L2/top-of-book stream and optionally publish its child orders back into the rebuilder for end-to-end testing.



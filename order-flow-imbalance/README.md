# Order Flow Imbalance (OFI) Calculator

Purpose

This component consumes a Level-2 order book stream (from the Level 2 State Rebuilder) and computes a rolling Order Flow Imbalance (OFI) metric. OFI is used to quantify short-term buy/sell pressure and can be a lightweight signal for intraday strategies.

Behavior (planned)
- Consume L2 deltas or Top-of-Book updates from `microstructure state rebuilder`.
- Maintain a sliding window (default: 1,000 ticks) and compute OFI statistics.
- Emit simple signals (e.g., `BUY`, `SELL`, or `NEUTRAL`) when the imbalance crosses configured thresholds.

Suggested filename and usage

```bash
cd "order flow imbalance"
python ofi_calculator.py --window 1000 --threshold 0.1
```

Dependencies (typical)
- Python 3.8+
- numpy, pandas (recommended for rolling-window calculations)

Configuration
- `--window` (int): number of ticks in the sliding window (default: 1000)
- `--threshold` (float): imbalance threshold for producing signals

Integration
- Start `microstructure-state-rebuilder` first to provide the L2 stream.
- Connect this script to the rebuilder via a local pipe, socket, or shared messaging layer.

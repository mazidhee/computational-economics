# Level 2 State Rebuilder (Microstructure)

This component ingests exchange-level JSON "delta" messages (Add / Cancel / Update) and reconstructs an in-memory Level-2 Limit Order Book (LOB). It is implemented in `state_rebuilder.py` and designed to be fast and lightweight using a hash map for order metadata and heaps for best-bid / best-ask extraction.

Key features
- Reconstructs L2 state from incremental deltas
- Maintains Top-of-Book (best bid / best ask) using heaps + lazy deletion
- Self-contained demo stream for quick testing

Quick start

```bash
cd "microstructure state rebuilder"
python state_rebuilder.py
```

Dependencies
- Python 3.8 or higher
- Uses only the Python standard library (`heapq`); no external packages required for the basic script

Input message schema

The rebuilder expects JSON-like messages with the following fields (examples):

```json
{"action": "add", "id": "order_1", "side": "bid", "price": 99}
{"action": "cancel", "id": "order_1"}
{"action": "update", "id": "order_1", "side": "ask", "price": 101}
```

Notes on integration
- The included `state_rebuilder.py` file contains a small built-in stream for demo purposes and prints the Top-of-Book after each delta.
- To integrate with the market data generator, run the generator first and stream JSON deltas into this script (via WebSocket, socket, or STDIN). Example generator:

```bash
cd "../geometric brownian motion"
python "stochastic_ generator.py"
```

- The implementation uses lazy deletion for cancelled orders: cancelled entries remain on the heap and are skipped when popped. This avoids costly heap removals and keeps the rebuilder performant.

Recommended next steps
- Replace the demo stream with a socket/WebSocket/STOMP consumer if you want live integration.
- Add logging, CLI flags for input mode (stdin vs websocket), and unit tests for delta handling.

Maintainer
- (Repository maintained by the author.)

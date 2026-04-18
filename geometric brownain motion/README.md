# Overview
The Stochastic Generator is a robust, lightweight Python script designed to simulate a realistic, continuous stream of market data. By mathematically modeling asset price movements, this tool acts as a local, synthetic exchange. It generates high-fidelity "ticks" (bids and asks) for testing algorithmic trading systems, charting libraries, or data pipelines without relying on external, rate-limited financial APIs.

## Features
* **Mathematical Realism:** Utilizes Geometric Brownian Motion (GBM) to simulate realistic asset price paths, incorporating adjustable *drift* (directional momentum) and *volatility* (price fluctuations).
* **Synthetic Tick Generation:** Continuously generates bid and ask prices based on the simulated asset value.
* **Dual Output Modes:** * **WebSocket Server:** Streams live data to local clients (perfect for building decoupled architectures).
  * **Standard Output (stdout):** Prints directly to the terminal for quick debugging and simple piping.
* **Zero External Dependencies:** Completely decouples your development environment from third-party API limits, internet outages, or subscription fees.

## Geometric Brownian Motion (GBM)
The core engine of this simulator is based on the GBM stochastic process.

The process is defined by the stochastic differential equation:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Where:
* **$S_t$**: The asset price at time $t$
* **$\mu$**: The percentage drift (expected return)
* **$\sigma$**: The percentage volatility
* **$W_t$**: A Wiener process (Standard Brownian Motion)

This ensures the generated prices follow a log-normal distribution, preventing the asset price from ever dropping below zero while realistically simulating market noise.

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

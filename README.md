# Computational Economics

This repository contains a collection of my six atomic projects focused on computational economics, market microstructure, and financial engineering. The codebase is organized sequentially, building a complete pipeline from synthetic market data generation to risk management.

## Repository Structure

### Folder 1: A Stochastic Generator
This module creates a standalone market data source, removing the need for external, rate-limited APIs. Uses Geometric Brownian Motion (GBM) to mathematically simulate asset price paths, factoring in drift and volatility.

---

## Setup and Usage
### Prerequisites
Ensure you have Python 3.8 or higher installed. The projects rely on standard scientific and asynchronous networking libraries.

Installation
Clone this repository to your local machine:

```bash
https://github.com/mazidhee/computational-economics.git
cd computational-economics
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
### Execution Guide
Because these projects build on top of one another, some scripts require others to be running simultaneously (for instance, the data generator needs to be running before the order book rebuilds the state).

Navigate to the respective folders to run each component:

Folder 1: Market Data Simulator
Run this first to start the synthetic exchange.

```bash
cd "geometric brownain motion"
python stochastic_generator.py
```
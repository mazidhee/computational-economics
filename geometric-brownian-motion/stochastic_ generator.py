import random
import math
import time
import json
import asyncio
import websockets

class NormalDistribution:
    def sample(self) -> float:
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        return z

class GeometricBrownianMotion:
    """
    tick - new_price = current * exp(drift_term + random_shock)
    """

    def __init__(self, mu: float, sigma: float, dt: float):
        self.mu = mu #drift
        self.sigma = sigma #volatility
        self.dt = dt #time step
        self.rng = NormalDistribution()

    def next_price(self, current_price: float) -> float:
        Z = self.rng.sample()
        drift_term = (self.mu - 0.5 * self.sigma ** 2) * self.dt
        shock_term = self.sigma * math.sqrt(self.dt) * Z
        return current_price * math.exp(drift_term + shock_term)

class Tick:
    def __init__(self, symbol: str, mid: float, spread: float):
        self.symbol = symbol
        self.mid = round(mid, 4)
        self.bid = round(mid - spread / 2, 4)
        self.ask = round(mid + spread / 2, 4)
        self.timestamp = time.time()

    def to_dict(self) -> dict:
        return {
            "symbol":    self.symbol,
            "mid":       self.mid,
            "bid":       self.bid,
            "ask":       self.ask,
            "timestamp": self.timestamp,
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict())

class MarketSimulator:
    def __init__(
        self,
        symbol:        str   = "YEAH",
        start_price:   float = 150.0,
        mu:            float = 0.0001,
        sigma:         float = 0.02,
        spread:        float = 0.10,
        dt:            float = 1 / 252,
        interval_ms:   int   = 100,
    ):
        self.symbol      = symbol
        self.price       = start_price
        self.spread      = spread
        self.interval_s  = interval_ms / 1000
        self.gbm         = GeometricBrownianMotion(mu, sigma, dt)
        self.clients     = set()

    async def register_client(self, websocket):
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    async def run(self):
        print(f"Starting {self.symbol} at {self.price:.2f}")
        try:
            while True:
                self.price = self.gbm.next_price(self.price)
                tick = Tick(self.symbol, self.price, self.spread)
                tick_data = str(tick)
                
                print(tick_data)
                
                if self.clients:
                    websockets.broadcast(self.clients, tick_data)
                    
                await asyncio.sleep(self.interval_s)
        except KeyboardInterrupt:
            pass

async def main():
    sim = MarketSimulator(
        symbol      = "DHEE",
        start_price = 150.0,
        mu          = 0.0001, 
        sigma       = 0.02, #2% daily volatility
        spread      = 0.10, #10 cent bid/ask spread
        dt          = 1 / 252, #one trading day per tick
        interval_ms = 100, 
    )
    
    async with websockets.serve(sim.register_client, "localhost", 8765):
        await sim.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
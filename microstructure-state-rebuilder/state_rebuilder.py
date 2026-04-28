import heapq


class OrderBook:
    def __init__(self):
        self.orders = {}
        self.bids = []
        self.asks = []

    def add_order(self, order_id, side, price):
        self.orders[order_id] = {"price": price, "side": side, "status": "active"}
        if side == "bid":
            heapq.heappush(self.bids, (-price, order_id))
        elif side == "ask":
            heapq.heappush(self.asks, (price, order_id))

    def cancel_order(self, order_id):
        if order_id in self.orders:
            self.orders[order_id]["status"] = "canceled"

    def update_order(self, order_id, side, new_price):
        self.cancel_order(order_id)
        self.add_order(order_id, side, new_price)

    def get_best_bid(self):
        while self.bids:
            price, order_id = self.bids[0]
            if self.orders[order_id]["status"] == "canceled":
                heapq.heappop(self.bids)
            else:
                return -price
        return None

    def get_best_ask(self):
        while self.asks:
            price, order_id = self.asks[0]
            if self.orders[order_id]["status"] == "canceled":
                heapq.heappop(self.asks)
            else:
                return price
        return None


if __name__ == "__main__":
    book = OrderBook()
    stream_of_deltas = [
        {"action": "add", "id": "order_1", "side": "bid", "price": 99},
        {"action": "add", "id": "order_2", "side": "ask", "price": 105},
        {"action": "add", "id": "order_3", "side": "bid", "price": 100},
        {"action": "add", "id": "order_4", "side": "ask", "price": 102},
        {"action": "cancel", "id": "order_3"},
        {"action": "update", "id": "order_4", "side": "ask", "price": 101},
    ]

    print("Processing live exchange deltas\n")

    for msg in stream_of_deltas:
        action = msg.get("action")
        order_id = msg.get("id")
        side = msg.get("side")
        price = msg.get("price")

        print(f"Received Delta: {msg}")

        if action == "add":
            book.add_order(order_id, side, price)
        elif action == "cancel":
            book.cancel_order(order_id)
        elif action == "update":
            book.update_order(order_id, side, price)

        best_bid = book.get_best_bid()
        best_ask = book.get_best_ask()
        print(
            f"TOP OF BOOK | Bid: {best_bid if best_bid else 'None'} | Ask: {best_ask if best_ask else 'None'}\n"
        )

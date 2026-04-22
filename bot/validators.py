def validate(symbol, side, order_type, qty, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol should be like BTCUSDT")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if float(qty) <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")
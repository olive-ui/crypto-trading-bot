from bot.client import send_request


def place_order(symbol, side, order_type, qty, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": qty
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return send_request("/fapi/v1/order", params)
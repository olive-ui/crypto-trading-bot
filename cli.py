import argparse
import logging

from bot.orders import place_order
from bot.validators import validate
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Crypto Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:
    validate(
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    print("\nOrder request:")
    print(vars(args))

    logging.info(f"Request: {vars(args)}")

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    if "error" in response or "code" in response:
        print("\nOrder failed:")
        print(response)
        logging.error(response)
    else:
        print("\nOrder placed successfully:")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        logging.info(response)

except Exception as e:
    print("\nError:", str(e))
    logging.error(str(e))
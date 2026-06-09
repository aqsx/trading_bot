import argparse
import logging

from binance.exceptions import (
    BinanceAPIException,
    BinanceRequestException
)

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logging


def main():

    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        logging.info(
            f"ORDER REQUEST | "
            f"Symbol={args.symbol} | "
            f"Side={side} | "
            f"Type={order_type} | "
            f"Qty={args.quantity} | "
            f"Price={args.price}"
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {args.quantity}")

        if args.price is not None:
            print(f"Price       : {args.price}")

        client = BinanceClient().get_client()

        manager = OrderManager(client)

        if order_type == "MARKET":

            result = manager.place_market_order(
                args.symbol,
                side,
                args.quantity
            )

        else:

            if args.price is None:
                raise ValueError(
                    "Price is required for LIMIT orders."
                )

            result = manager.place_limit_order(
                args.symbol,
                side,
                args.quantity,
                args.price
            )

        logging.info(
            f"ORDER RESPONSE | {result}"
        )

        print("\n===== ORDER SUCCESS =====")

        print(
            f"Order ID     : "
            f"{result.get('orderId', 'N/A')}"
        )

        print(
            f"Status       : "
            f"{result.get('status', 'N/A')}"
        )

        print(
            f"Executed Qty : "
            f"{result.get('executedQty', 'N/A')}"
        )

        if "avgPrice" in result:
            print(
                f"Average Price: "
                f"{result.get('avgPrice')}"
            )

        print("\n✓ Order placed successfully")

    except ValueError as e:

        logging.error(
            f"VALIDATION ERROR | {e}"
        )

        print("\n===== INPUT ERROR =====")
        print(str(e))

    except BinanceAPIException as e:

        logging.error(
            f"BINANCE API ERROR | "
            f"Code={e.code} | "
            f"Message={e.message}"
        )

        print("\n===== BINANCE API ERROR =====")
        print(f"Code    : {e.code}")
        print(f"Message : {e.message}")

    except BinanceRequestException as e:

        logging.error(
            f"NETWORK ERROR | {e}"
        )

        print("\n===== NETWORK ERROR =====")
        print(str(e))

    except ConnectionError as e:

        logging.error(
            f"CONNECTION ERROR | {e}"
        )

        print("\n===== CONNECTION ERROR =====")
        print(str(e))

    except Exception as e:

        logging.exception(
            "UNEXPECTED ERROR"
        )

        print("\n===== UNEXPECTED ERROR =====")
        print(str(e))


if __name__ == "__main__":
    main()
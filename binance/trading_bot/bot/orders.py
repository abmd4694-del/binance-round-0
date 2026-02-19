import logging
from .client import BinanceClient
from .validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

logger = logging.getLogger("trading_bot")

def place_trade(
    client: BinanceClient,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    """
    Orchestrates the order placement: validates input and calls the API.
    """
    try:
        # Validation
        v_symbol = validate_symbol(symbol)
        v_side = validate_side(side)
        v_type = validate_order_type(order_type)
        v_qty = validate_quantity(quantity)
        v_price = validate_price(price, v_type)

        logger.info(f"Placing {v_type} {v_side} order for {v_qty} {v_symbol}...")

        # API Call
        response = client.post_order(
            symbol=v_symbol,
            side=v_side,
            order_type=v_type,
            quantity=v_qty,
            price=v_price
        )

        logger.info(f"Order placed successfully: ID {response.get('orderId')}")
        return response

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        raise
    except Exception as e:
        logger.error(f"Order Placement Failed: {e}")
        raise

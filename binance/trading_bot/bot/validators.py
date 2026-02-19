from typing import Optional

def validate_symbol(symbol: str) -> str:
    """
    Validates the trading symbol.
    """
    if not symbol.isalnum():
        raise ValueError(f"Invalid symbol: {symbol}. Must be alphanumeric.")
    return symbol.upper()

def validate_side(side: str) -> str:
    """
    Validates order side (BUY/SELL).
    """
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side: {side}. Must be 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    """
    Validates order type (MARKET/LIMIT).
    """
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(f"Invalid order type: {order_type}. Must be 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: float) -> float:
    """
    Validates order quantity.
    """
    if quantity <= 0:
        raise ValueError(f"Quantity must be positive. Got: {quantity}")
    return quantity

def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    """
    Validates price for LIMIT orders.
    """
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price must be positive for LIMIT orders.")
    return price

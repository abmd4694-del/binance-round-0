import os
import sys
import typer
from typing import Optional
from dotenv import load_dotenv
from bot.client import BinanceClient
from bot.orders import place_trade
from bot.logging_config import setup_logging

# Load environment variables
load_dotenv()

app = typer.Typer(help="Binance Futures Trading Bot CLI", no_args_is_help=True)

# Setup logging
logger = setup_logging()

def get_client() -> BinanceClient:
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        typer.secho("Error: API credentials not found. Set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET in .env file.", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
    return BinanceClient(api_key, api_secret)

@app.callback()
def callback():
    """
    Binance Futures Trading Bot CLI
    """


@app.command()
def order(
    symbol: str = typer.Option(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="Order side: BUY or SELL"),
    type: str = typer.Option(..., help="Order type: MARKET or LIMIT"),
    qty: float = typer.Option(..., help="Quantity to trade"),
    price: Optional[float] = typer.Option(None, help="Price for LIMIT orders")
):
    """
    Place a new order on Binance Futures Testnet.
    """
    try:
        client = get_client()
        response = place_trade(client, symbol, side, type, qty, price)
        
        # Pretty print response
        typer.secho("\n--- Order Summary ---", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"Symbol: {response.get('symbol')}")
        typer.echo(f"Order ID: {response.get('orderId')}")
        typer.echo(f"Status: {response.get('status')}")
        typer.echo(f"Type: {response.get('type')}")
        typer.echo(f"Side: {response.get('side')}")
        typer.echo(f"Executed Qty: {response.get('executedQty')}")
        typer.echo(f"Avg Price: {response.get('avgPrice')}")
        
    except Exception as e:
        typer.secho(f"\nFailed to place order: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()

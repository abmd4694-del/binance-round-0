# Binance Futures Trading Bot

A simplified Python trading bot for Binance Futures Testnet (USDT-M).

## Features

- Place **MARKET** and **LIMIT** orders.
- Support for **BUY** and **SELL** sides.
- Clean CLI interface using `Typer`.
- Logging to console and file (`trading_bot.log`).
- Input validation and error handling.

## specific Requirements

- Python 3.x
- Binance Futures Testnet Account

## Setup

1. **Clone/Download the repository**

   ```bash
   # If you have the zip, extract it.
   cd binance
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   - Copy `.env.example` to `.env`:
     - Windows: `copy .env.example .env`
     - Linux/Mac: `cp .env.example .env`
   - Edit `.env` and add your **Testnet** API Key and Secret.

## Usage

Run the bot using the CLI entry point:

```bash
python trading_bot/cli.py --help
```

### Place a Market Order

```bash
python trading_bot/cli.py order --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```

### Place a Limit Order

```bash
python trading_bot/cli.py order --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 50000
```

## Project Structure

- `trading_bot/cli.py`: Main entry point.
- `trading_bot/bot/client.py`: Handles API authentication and requests.
- `trading_bot/bot/orders.py`: Orchestrates validation and order placement.
- `trading_bot/bot/validators.py`: Input validation logic.
- `trading_bot/bot/logging_config.py`: Logging configuration.

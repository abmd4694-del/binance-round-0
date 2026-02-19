import hashlib
import hmac
import time
import requests
import logging
from urllib.parse import urlencode

logger = logging.getLogger("trading_bot")

class BinanceClient:
    """
    A simple wrapper for Binance Futures Testnet API.
    """
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _get_signature(self, params: dict) -> str:
        """
        Generates HMAC SHA256 signature for the request.
        """
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def _request(self, method: str, endpoint: str, params: dict = None):
        """
        Internal method to handle API requests with error handling.
        """
        if params is None:
            params = {}

        # Timestamp is mandatory for signed endpoints
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000
        
        # Generate signature
        params["signature"] = self._get_signature(params)

        url = f"{self.BASE_URL}{endpoint}"
        
        logger.debug(f"Sending {method} request to {url} with params: {params}")

        try:
            response = self.session.request(method, url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            error_msg = e.response.text
            try:
                error_json = e.response.json()
                if "msg" in error_json:
                    error_msg = f"{error_json.get('code')} - {error_json.get('msg')}"
            except ValueError:
                pass
            
            logger.error(f"HTTP Error: {error_msg}")
            raise Exception(f"Binance API Error: {error_msg}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request Error: {str(e)}")
            raise

    def post_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None, time_in_force: str = "GTC"):
        """
        Places an order on Binance Futures.
        """
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders.")
            params["price"] = price
            params["timeInForce"] = time_in_force

        return self._request("POST", "/fapi/v1/order", params)

    def get_account_info(self):
        """
        Retrieves account information (balances, etc.).
        """
        return self._request("GET", "/fapi/v2/account")

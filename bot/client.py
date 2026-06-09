import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:

    def __init__(self):

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        print("API Loaded:", bool(api_key))
        print("Secret Loaded:", bool(api_secret))

        self.client = Client(
            api_key,
            api_secret
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

    def get_client(self):
        return self.client
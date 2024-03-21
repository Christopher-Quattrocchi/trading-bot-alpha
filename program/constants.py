from dydx3.constants import API_HOST_SEPOLIA, API_HOST_MAINNET
from web3 import Web3
from decouple import config # allow access to env vars

#!!! SELECT MODE !!!!!
MODE = "DEVELOPMENT"

# Close all open positions and orders
ABORT_ALL_POSITIONS = True

# Find Cointegrated Pairs
FIND_COINTEGRATED_PAIRS = True

# Place Trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# Eth Address
ETHEREUM_ADDRESS = "0xF0119230DC248Ae4160e6dBD7998Ed4E907CC8f6"

# KEYS - PRODUCTION
# Must be on Mainnet on DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - DEVELOPMENT
# Must be on Testnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_SEPOLIA

# HTTP Provider
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/s57XDeF1IRY34W8TKS1sSvtL9Dojsg60"
HTTP_PROVIDER_TESTNET = "https://eth-sepolia.g.alchemy.com/v2/k-QfJ1gbTOoMPJU2ofSxHN2-TLrXxwvl"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET
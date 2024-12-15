# blockchain/ganache_connection.py
from web3 import Web3

# Connect to Ganache (default URL is http://127.0.0.1:8545)
ganache_url = 'http://127.0.0.1:7545'  # Ganache default URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connection is successful using the lowercase method
if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Get the first account from Ganache
account = web3.eth.accounts[0]  # This is the default account in Ganache
print(f"Using account: {account}")

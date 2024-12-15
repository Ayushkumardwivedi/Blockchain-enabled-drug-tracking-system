# blockchain/views.py
from django.http import JsonResponse,HttpResponse
from .ganache_connection import web3

from web3 import Web3

def send_transaction(request):
    web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

    ether_amount = 0.1  # Replace with the actual Ether amount
    wei_amount = web3.to_wei(ether_amount, 'ether')  # Use `to_wei` method

    print(f"Amount in Wei: {wei_amount}")
    # Add your transaction logic here

    return HttpResponse(f"Transaction amount in Wei: {wei_amount}")


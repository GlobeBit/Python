"""Simple Ethereum interactions with Web3.py.

This script keeps the original flow of the repository:
1. Connect to an Ethereum node
2. Retrieve the latest block
3. Check a wallet balance
4. Interact with the BAYC contract (owner, supply, symbol, token details)
"""

from __future__ import annotations

import json
import os
from typing import Any

from web3 import Web3

# BAYC contract address on Ethereum mainnet
CONTRACT_ADDRESS = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"

# Read from env var instead of hardcoding credentials.
PROVIDER_URL = os.getenv("INFURA_HTTPS_URI", "<your Infura HTTPs URI>")

# Minimal ABI for the read-only functions used in this example.
BAYC_MINIMAL_ABI = json.loads(
    """
    [
      {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
      {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
      {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
      {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "tokenURI", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"},
      {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ownerOf", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}
    ]
    """
)


def connect(provider_url: str) -> Web3:
    """Create a Web3 connection to an HTTPS provider."""
    web3 = Web3(Web3.HTTPProvider(provider_url))
    if not web3.is_connected():
        raise ConnectionError(
            "Unable to connect to Ethereum provider. Check INFURA_HTTPS_URI."
        )
    return web3


def latest_block(web3: Web3) -> Any:
    """Fetch the latest block."""
    return web3.eth.get_block("latest")


def wallet_balance_wei(web3: Web3, wallet: str) -> int:
    """Return wallet balance in Wei."""
    checksum_wallet = Web3.to_checksum_address(wallet)
    return web3.eth.get_balance(checksum_wallet)


def bayc_contract(web3: Web3):
    """Build a BAYC contract instance with minimal ABI."""
    return web3.eth.contract(address=CONTRACT_ADDRESS, abi=BAYC_MINIMAL_ABI)


def main() -> None:
    web3 = connect(PROVIDER_URL)

    print("Connected:", web3.is_connected())
    print("Latest block:", latest_block(web3))

    wallet = "0x85F34591e36b86E3c7417A9a3551A0DFe1A71b37"
    print("Wallet balance (Wei):", wallet_balance_wei(web3, wallet))

    contract = bayc_contract(web3)
    token_id = 2321

    print("BAYC owner:", contract.functions.owner().call())
    print("BAYC total supply:", contract.functions.totalSupply().call())
    print("BAYC symbol:", contract.functions.symbol().call())
    print(f"BAYC tokenURI({token_id}):", contract.functions.tokenURI(token_id).call())
    print(f"BAYC ownerOf({token_id}):", contract.functions.ownerOf(token_id).call())


if __name__ == "__main__":
    main()

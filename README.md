# Ethereum Python Interactions

This repository demonstrates simple Ethereum interactions in Python using Web3.py.

## What this repo contains

- `ethereum-interactions/bored_ape_interaction.py`:
  - Connects to an Ethereum HTTPS provider (e.g., Infura)
  - Fetches the latest block
  - Reads a wallet balance in Wei
  - Interacts with the Bored Ape Yacht Club contract (owner, total supply, symbol, token URI, ownerOf)

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install web3
export INFURA_HTTPS_URI="https://mainnet.infura.io/v3/<your-key>"
python ethereum-interactions/bored_ape_interaction.py
```

## Notes

- The script is read-only (no transactions are sent).
- The provider URL is read from `INFURA_HTTPS_URI`.

## Improvement proposals (keeping current idea and structure)

1. **Dependency pinning**
   - Add a `requirements.txt` or `pyproject.toml` with pinned versions for reproducibility.
2. **Configuration clarity**
   - Add a `.env.example` showing required environment variables.
3. **Error handling for RPC calls**
   - Catch and explain common JSON-RPC/network errors for smoother onboarding.
4. **Minimal test coverage**
   - Add unit tests for helper functions and optionally mock Web3 calls.
5. **Output formatting**
   - Print selected latest-block fields (number/hash/timestamp) to keep output readable.
6. **Structure-preserving split**
   - Keep one script for demo use, but move constants and ABI into a small helper module.

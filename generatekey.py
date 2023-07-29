import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account

# Get the mnemonic phrase from the environment variable
# Replace "http://127.0.0.1:7545" with the RPC URL of your local Ganache node or Infura URL
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
mnemonic = "journey napkin survey hold spread plastic firm identify advance private then river"
# Create a Wallet object from the mnemonic seed phrase
wallet = Wallet(mnemonic)

# Derive the first 5 accounts of the m/44'/60'/0'/0/ path
for account_index in range(5):
    # Derive the account's private key and public key
    private_key, public_key = wallet.derive_account("eth", account_index)

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private_key)

    # Print the account address associated with the Ethereum account
    print(f"Account {account_index}: {account.address}")

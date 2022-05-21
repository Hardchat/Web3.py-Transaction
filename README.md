# Web3.py-Transaction
Creating and Submitting Transactions to Web3 Enabled Blockchains using JSON-RPC endpoints.

# Installation
```git clone https://github.com/Hardchat/Web3.py-Transaction/```

# Usage
1. Select the Blockchain you want to use by entering the corresponding number.
2. Enter your wallet details
3. Enter the wallet address you want to send your coins to.
4. View your transaction at the link provided.

# Notes
**Disclaimer**: This program is functional but is a Proof of Concept that illustrates Web3.py usage. If you want a more secure and feature-rich solution, the Metamask wallet is suggested. 

**Gas**: This implementation uses the built-in estimate gas function of Web3.py and a static gas limit of 100,000 to cover these native token transactions.

**Private Key**: You are required to supply your wallet's private key for all transactions so you can sign the transactions. Without this key authentication, anyone would be able to submit transactions only by knowing your wallet address.

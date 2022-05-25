from web3 import Web3


class Blockchain:
    chainId = 0
    rpc_url = 0
    block_explorer = 0
    chain_name = 0

    def __init__(self, chainId, rpc_url, block_explorer, chain_name):
        self.chainId = chainId
        self.rpc_url = rpc_url
        self.block_explorer = block_explorer
        self.chain_name = chain_name

print("\nChoose the number for your desired Blockchain:\n\n1) Avalanche C-Chain\n2) Harmony\n3) Multivac\n")

option_list = ["1", "2", "3"]
choice = 0
selection = input("Choice: ")

while selection not in option_list:
    print("[Error]: Please input the correct number of the Blockchain you want to utilize.\n")
    selection = input("Choice: ")
        
else:
    if selection == "1":
        avalanche = Blockchain("43114", "https://api.avax.network/ext/bc/C/rpc", "https://snowtrace.io/tx/", "Avalanche")
        choice = avalanche
    elif selection == "2":
        harmony = Blockchain("1666600000", "https://api.harmony.one", "https://explorer.harmony.one/tx/", "Harmony")
        choice = harmony
    elif selection == "3":
        multivac = Blockchain("62621", "https://rpc.mtv.ac", "https://e.mtv.ac/transaction.html?hash=", "MultiVAC")
        choice = multivac

    rpc_url = Web3(Web3.HTTPProvider(choice.rpc_url))
    sender_address = input("Enter your wallet address: ")
    wallet_balance = rpc_url.eth.getBalance(rpc_url.toChecksumAddress(sender_address))
    wallet_balance = rpc_url.fromWei(wallet_balance, 'ether')
    print(f'\n{choice.chain_name} Wallet: {sender_address} has: {wallet_balance} coins.')
    amount_to_send = input("\nEnter the amount of coins you want to send: ")
    
    while float(amount_to_send) > float(wallet_balance):
        print(f'\n[Error]: Amount chosen is greater than available balance. Try again.')
        amount_to_send = input("\nEnter the amount of coins you want to send: ")
    else:
        receiver_address = input("\nEnter the address you wish to send the coins to: ")
        sender_private_key = input("\nEnter your wallet private key (to sign the transaction): ")
        nonce = rpc_url.eth.getTransactionCount(rpc_url.toChecksumAddress(sender_address))
        gas_price = rpc_url.eth.gas_price
        build_transaction = {
            'chainId': int(choice.chainId),
            'value': rpc_url.toWei(float(amount_to_send), 'ether'),
            'gas': 100000,  # Gas limit for the transaction
            'gasPrice': gas_price,
            'nonce': nonce,
            'to': rpc_url.toChecksumAddress(receiver_address)
            }
        try:
            signed_transaction = rpc_url.eth.account.signTransaction(build_transaction, private_key=sender_private_key)
            transaction = rpc_url.eth.sendRawTransaction(signed_transaction.rawTransaction)
            transaction_hash = rpc_url.toHex(transaction)
            print(f'\nView your transaction here: {choice.block_explorer}{transaction_hash}')
        except:
            print(f'\n[Failed]: Make sure your balance is high enough to also pay the gas fee for this transaction and try again.')

# from turtle import up
from brownie import accounts, config, SimpleStorage, network

# import os


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    # methods for storing keys
    #
    # 1. to use brownie's inbuild faux accounts list
    # only good for using with Ganache; NOT web client
    # account = accounts[0]

    # 2. to load using Terminal (safest option)
    # account = accounts.load("unpackAI_account")
    #
    # Terminal commands:
    # $ brownie accounts new {account_name}
    # $ brownie will then prompt for the private key
    #       and a user password for encryption
    #
    # $ brownie accounts delete {account_name}
    # $ brownie accounts list
    #

    # 3. use dotevn method (note: import os)
    # using os.getenv
    # account = accounts.add(os.getenv("PRIVATE_KEY"))

    # 4. using brownie-config (note: from brownie import config)
    # this is useful for importing various wallets(?)
    # account = accounts.add(config["wallets"]["from_key"])

    # pull account based on network
    account = get_account()

    # repreating web3.py (Lesson 4) process using brownie
    simple_storage = SimpleStorage.deploy({"from": account})
    # Transact
    # Call ('view' function -> no gas required)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # store 15; recall this is a txn so uses gas
    transaction = simple_storage.store(15, {"from": account})
    # wait for (n) blocks confirmation
    transaction.wait(1)
    # use view function to pull info from blockchain
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()

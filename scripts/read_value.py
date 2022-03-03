from brownie import SimpleStorage, accounts, config


def read_contract():
    # index -1 will always give us the latest deployment
    simple_storage = SimpleStorage[-1]
    # ABI
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()

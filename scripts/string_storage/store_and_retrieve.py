import os
from brownie import accounts, StringStorage
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)

def store_and_retrieve():
    string_storage = StringStorage[0]

    tx1 = string_storage.store("Hello", {"from": accounts[0]})
    tx1.wait(1)
    account_1_string = string_storage.retrieve()

    print(accounts[0])
    print(accounts[1])
    print(account_1_string)

    tx2 = string_storage.store("World", {"from": accounts[1]})
    tx2.wait(1)
    account_2_string = string_storage.retrieve()
    print(account_2_string)

def main():
    store_and_retrieve()
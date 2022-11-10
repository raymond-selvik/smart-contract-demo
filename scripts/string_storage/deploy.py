import os
from brownie import accounts, StringStorage
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)

def deploy_string_storage():
    account = accounts[0]
    string_storage = StringStorage.deploy({
        "from" : account
        })
    tx1 = string_storage.store("Hello", {"from": accounts[0]})
    tx1.wait(1)
    account_1_string = string_storage.retrieve()
    print(account_1_string)

def main():
    deploy_string_storage()
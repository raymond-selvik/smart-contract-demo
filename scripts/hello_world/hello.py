import os
from brownie import accounts, HelloWorld
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def hello_world():
    account = accounts[0]
    
    helloWorld = HelloWorld.deploy({
        "from" : account
        })

    reponse = helloWorld.sayHello({"from": account})
    print(reponse)
    reponse = helloWorld.getCallerAddress({"from": account})
    print(reponse)


def main():
    hello_world()

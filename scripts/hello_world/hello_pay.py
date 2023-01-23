import os
from brownie import accounts, HelloPay, Wei
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def hello_world():
    account = accounts[0]
    
    helloPay = HelloPay.deploy({
        "from" : account
        })

    reponse = helloPay.getBalance({"from": account})
    print(reponse)

    reponse = helloPay.pay({"from": account, "value" : Wei("100 ether")})
    print(reponse)

    reponse = helloPay.getBalance({"from": account})
    print(reponse)
 

def main():
    hello_world()

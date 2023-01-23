import os
from brownie import accounts, Lottery
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)

def enter():
    lottery = Lottery[0]

    account_1 = accounts[1]
    account_2 = accounts[2]


    lottery.enterLottery({"from" : account_1,"value" : 1})
    lottery.enterLottery({"from" : account_2,"value" : 1})


def main():
    enter()
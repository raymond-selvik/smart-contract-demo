import os
from brownie import accounts, Lottery, Wei
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def deploy_lottery():
    owner = accounts[0]
    
    global lottery
    lottery = Lottery.deploy({
        "from" : owner
        })

def enter():
    lottery = Lottery[0]

    account_1 = accounts[1]
    account_2 = accounts[2]


    lottery.enterLottery({"from" : account_1,"value" : Wei("100 ether")})
    lottery.enterLottery({"from" : account_2,"value" : Wei("100 ether")})

def pick_winner():
    lottery.pickWinner({"from" : accounts[0]})

def main():
    deploy_lottery()
    print("Deployed Lottery Smart Contract")
    input("Press key to continue....")

    enter()
    print("Account 1 and Account 2 has entered the lottery")
    input("Press key to continue....")

    pick_winner()
    print("Winner is picked")
    input("Press key to continue....")


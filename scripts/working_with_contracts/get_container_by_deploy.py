import os
from brownie import accounts, HelloWorld, interface
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)


def deploy_contract():
    contract = HelloWorld.deploy({"from" : accounts[0]})
    return contract, contract.address

def deploy_string_storage():
    hello_world, address = deploy_contract()

    print(hello_world.sayHello({"from" : accounts[0]}))
    print(hello_world.getCallerAddress(({"from" : accounts[0]})))

    print(hello_world.sayHello({"from" : accounts[1]}))
    print(hello_world.getCallerAddress(({"from" : accounts[1]})))

    print("=====================CONCTRACT BY CODE AND ADDRESS=======================")

    contract_by_address = HelloWorld.at(address)

    print(contract_by_address.sayHello({"from" : accounts[0]}))
    print(contract_by_address.getCallerAddress(({"from" : accounts[0]})))

    print("=================CONCTRACT BY INTERFACE AND ADDRESS=====================")
    contract_by_interface = interface.HelloWorldInterface(address)

    print(contract_by_interface.sayHello({"from" : accounts[0]}))
    print(contract_by_interface.getCallerAddress(({"from" : accounts[0]})))

def main():
    deploy_string_storage()
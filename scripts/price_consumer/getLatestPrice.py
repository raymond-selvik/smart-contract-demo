import os
from brownie import accounts, PriceConsumer
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)
gas_price(gas_strategy)

def store_and_retrieve():
    price_consumer = PriceConsumer.deploy(
        "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",
        {
        "from" : accounts[0]
        })

    latest_price  = price_consumer.getLatestPrice()
    print(latest_price)

def main():
    store_and_retrieve()
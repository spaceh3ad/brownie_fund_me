from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()

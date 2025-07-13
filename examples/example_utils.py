import json
import os
from pathlib import Path

import eth_account
from eth_account.signers.local import LocalAccount

from hyperliquid.exchange import Exchange
from hyperliquid.info import Info

def load_config():
    """Load configuration from config.json file"""
    config_path = Path(__file__).parent / "config.json"
    
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found at {config_path}. "
            "Please copy config.json.example to config.json and fill in your credentials."
        )
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Validate required fields
    required_fields = ['account_address', 'secret_key']
    for field in required_fields:
        if not config.get(field) or config[field] == "0x...":
            raise ValueError(f"Please set your {field} in config.json")
    
    # Validate token if present
    if 'token' in config and config['token']:
        try:
            int(config['token'])
        except ValueError:
            raise ValueError(f"Token must be a valid integer, got: {config['token']}")
    
    return config

def print_result(result, title="Result"):
    """Helper function to pretty print results"""
    print(f"\n{title}:")
    print("=" * len(title))
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)
    print() 


def setup(base_url=None, skip_ws=False, perp_dexs=None):
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        config = json.load(f)
    account: LocalAccount = eth_account.Account.from_key(config["secret_key"])
    address = config["account_address"]
    if address == "":
        address = account.address
    print("Running with account address:", address)
    if address != account.address:
        print("Running with agent address:", account.address)
    info = Info(base_url, skip_ws, perp_dexs=perp_dexs)
    user_state = info.user_state(address)
    spot_user_state = info.spot_user_state(address)
    margin_summary = user_state["marginSummary"]
    if float(margin_summary["accountValue"]) == 0 and len(spot_user_state["balances"]) == 0:
        print("Not running the example because the provided account has no equity.")
        url = info.base_url.split(".", 1)[1]
        error_string = f"No accountValue:\nIf you think this is a mistake, make sure that {address} has a balance on {url}.\nIf address shown is your API wallet address, update the config to specify the address of your account, not the address of the API wallet."
        raise Exception(error_string)
    exchange = Exchange(account, base_url, account_address=address, perp_dexs=perp_dexs)
    return address, info, exchange


def setup_multi_sig_wallets():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as f:
        config = json.load(f)

    authorized_user_wallets = []
    for wallet_config in config["multi_sig"]["authorized_users"]:
        account: LocalAccount = eth_account.Account.from_key(wallet_config["secret_key"])
        address = wallet_config["account_address"]
        if account.address != address:
            raise Exception(f"provided authorized user address {address} does not match private key")
        print("loaded authorized user for multi-sig", address)
        authorized_user_wallets.append(account)
    return authorized_user_wallets
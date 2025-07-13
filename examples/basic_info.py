#!/usr/bin/env python3
"""
Basic info example for Hyperliquid Python SDK
This script demonstrates how to fetch basic user information from Hyperliquid.
"""

from hyperliquid.info import Info
from hyperliquid.utils import constants
from example_utils import load_config, print_result

def main():
    """Fetch and display basic account information"""
    try:
        # Load configuration
        config = load_config()
        account_address = config['account_address']
        
        # Initialize Info client (read-only, no private key needed)
        # Use TESTNET_API_URL for testing or MAINNET_API_URL for real trading
        info = Info(constants.TESTNET_API_URL, skip_ws=True)
        
        print(f"Fetching information for account: {account_address}")
        
        # Get user state
        user_state = info.user_state(account_address)
        print_result(user_state, "User State")
        
        # Get open orders
        open_orders = info.open_orders(account_address)
        print_result(open_orders, "Open Orders")
        
        # Get user fills (recent trades)
        user_fills = info.user_fills(account_address)
        print_result(user_fills[:5] if user_fills else [], "Recent Fills (last 5)")
        
        # Get all mids (market prices)
        all_mids = info.all_mids()
        print_result(dict(list(all_mids.items())[:10]), "Market Prices (first 10)")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Copied config.json.example to config.json")
        print("2. Set your account_address in config.json")
        print("3. The account exists on the network you're using")

if __name__ == "__main__":
    main() 
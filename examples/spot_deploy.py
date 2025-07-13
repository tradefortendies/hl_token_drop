#!/usr/bin/env python3
"""
Spot Deploy Example for Hyperliquid Python SDK
This script demonstrates spot token management starting from user genesis (step 2).

IMPORTANT: This assumes you already have a registered token. Set your token index in config.json.
"""

import example_utils

from hyperliquid.utils import constants

# Set to True to register the spot pair (TOKEN/USDC)
REGISTER_SPOT = False
# Set to True to register hyperliquidity for the spot pair
REGISTER_HYPERLIQUIDITY = False

def main():
    address, info, exchange = example_utils.setup(constants.TESTNET_API_URL, skip_ws=True)

    # Load token from config
    config = example_utils.load_config()
    if 'token' not in config or not config['token']:
        print("Error: Token not specified in config.json")
        return
    token = int(config['token'])
    hyperliquidity_address = config['hyperliquidity_address']
    airdrop_wallet_address = config['airdrop_wallet_address']

    # Step 2: User Genesis
    #
    # User genesis can be called multiple times to associate balances to specific users and/or
    # tokens for genesis.
    #
    # Associate 9499100000000000000 wei with user 0x0000000000000000000000000000000000000001
    # Associate 500000000000000000 wei with hyperliquidity
    # Associate 1M tokens each as an example with airdrop wallets that are part of genesis
    user_genesis_result = exchange.spot_deploy_user_genesis(
        token,
        [
            (airdrop_wallet_address, "9499100000000000000"),
            (hyperliquidity_address, "500000000000000000"),
            ("0xEf920E4D5fF99B5e5BaF27A919dee46D4719Eb5B", "100000000000000"),
            ("0x0ac6d5e95f0d9342eddd94bba7483e64496dfbd6", "100000000000000"),
            ("0x026433a0683fe1fcd3c75131f20983526f30f363", "100000000000000"),
            ("0x4c1c77a0ccB5E9dcEFf0b51d2eF6B8Fd87Cf4eCf", "100000000000000"),
            ("0x25dd028fb9ebc9e6244fb1b2329d7b1a5c53b36c", "100000000000000"),
            ("0x9db844d9aed745a8af4917b5323d52d83362d072", "100000000000000"),
            ("0x949374d5677bb336d948bd4b0ec0e37a3fc20e03", "100000000000000"),
            ("0xc8dad4333de7aba9f2aa8f5cbb0e727cac3bfdff", "100000000000000"),
            ("0xf7b4fb02ae66143d001c1e4e43cb39f450f0b674", "100000000000000"),
        ],
        [],
    )
    print(user_genesis_result)
    # No-op
    user_genesis_result = exchange.spot_deploy_user_genesis(token, [], [])
    print(user_genesis_result)

    # Step 3: Genesis
    #
    # Finalize genesis. The max supply of 10000000000000000000 wei needs to match the total
    # allocation above from user genesis.
    #
    # "noHyperliquidity" can also be set to disable hyperliquidity. In that case, no balance
    # should be associated with hyperliquidity from step 2 (user genesis).
    genesis_result = exchange.spot_deploy_genesis(token, "10000000000000000000", False)
    print(genesis_result)

    if REGISTER_SPOT:
        # Step 4: Register Spot
        #
        # Register the spot pair (TOKEN/USDC) given base and quote token indices. 0 represents USDC.
        # The base token is the first token in the pair and the quote token is the second token.
        register_spot_result = exchange.spot_deploy_register_spot(token, 0)
        print(register_spot_result)
        # If registration is successful, a spot index will be returned. This spot index is required for
        # registering hyperliquidity.
        if register_spot_result["status"] == "ok":
            spot = register_spot_result["response"]["data"]
        else:
            return

        if REGISTER_HYPERLIQUIDITY:
            # Step 5: Register Hyperliquidity
            #
            # Registers hyperliquidity for the spot pair. In this example, hyperliquidity is registered
            # with a starting price of $2, an order size of 4, and 100 total orders.
            #
            # This step is required even if "noHyperliquidity" was set to True.
            # If "noHyperliquidity" was set to True during step 3 (genesis), then "n_orders" is required to be 0.
            register_hyperliquidity_result = exchange.spot_deploy_register_hyperliquidity(spot, 2.0, 4.0, 100, None)
            print(register_hyperliquidity_result)


if __name__ == "__main__":
    main()
# Hyperliquid Python Scripts

This repository contains Python scripts for interacting with the [Hyperliquid](https://hyperliquid.xyz/) decentralized exchange using the [hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk).

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- A Hyperliquid account (Testnet or Mainnet)
- API credentials from Hyperliquid

### 1. Clone and Setup

```bash
# Clone this repository
git clone <your-repo-url>
cd latina_scripts

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example config
cd examples
cp config.json.example config.json

# Edit your configuration
vim config.json  # or use your preferred editor
```

Set your Hyperliquid credentials in `examples/config.json`:

```json
{
  "account_address": "0x1234567890abcdef...",
  "secret_key": "0xabcdef1234567890...",
  "comments": "Your Hyperliquid wallet address and private key"
}
```

### 3. Run Examples

```bash
# Test basic connectivity (read-only)
python examples/basic_info.py

# Run spot trading demo (safe demo mode)
python examples/spot_deploy.py
```

## 📁 Project Structure

```
latina_scripts/
├── venv/                     # Virtual environment
├── examples/                 # Example scripts
│   ├── config.json.example   # Configuration template
│   ├── example_utils.py      # Utility functions
│   ├── basic_info.py         # Basic account info script
│   └── spot_deploy.py        # Spot trading example
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🔧 Available Scripts

### `basic_info.py`
- **Purpose**: Fetch and display basic account information
- **Safety**: Read-only operations, no trading
- **Usage**: Test your setup and view account data

```bash
python examples/basic_info.py
```

### `spot_deploy.py`
- **Purpose**: Comprehensive spot trading example
- **Features**: 
  - Spot token management
  - Order creation and cancellation
  - Balance checking
  - Market data retrieval
- **Safety**: Demo mode by default (actual trading commented out)

```bash
python examples/spot_deploy.py
```

## 🛡️ Safety Guidelines

### ⚠️ **IMPORTANT SAFETY NOTES**

1. **Start with Testnet**: Always test on Hyperliquid Testnet first
2. **Small Amounts**: Start with very small amounts when testing
3. **Review Code**: Understand what each script does before running
4. **Demo Mode**: Most scripts run in demo mode by default
5. **Private Keys**: Never share your private keys or commit them to version control

### Testnet vs Mainnet

- **Testnet** (recommended for learning): Use test tokens, no real money at risk
- **Mainnet** (production): Real money, real consequences

The scripts default to Testnet for safety. To use Mainnet, modify the `use_testnet` parameter in the scripts.

## 🔑 Getting API Credentials

### Option 1: Use Your Main Wallet
1. Use your existing Hyperliquid wallet address as `account_address`
2. Use your wallet's private key as `secret_key`

### Option 2: Create API Wallet (Recommended)
1. Go to [Hyperliquid API](https://app.hyperliquid.xyz/API)
2. Generate a new API private key
3. Set the API wallet's private key as `secret_key`
4. **Important**: Still use your main wallet's address as `account_address`

## 📚 SDK Documentation

This repository uses the official Hyperliquid Python SDK:
- **GitHub**: [hyperliquid-dex/hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)
- **PyPI**: [hyperliquid-python-sdk](https://pypi.org/project/hyperliquid-python-sdk/)

## 🔄 Common Operations

### Getting Account Information
```python
from hyperliquid.info import Info
from hyperliquid.utils import constants

info = Info(constants.TESTNET_API_URL, skip_ws=True)
user_state = info.user_state("your_address")
```

### Creating Spot Orders
```python
from hyperliquid.exchange import Exchange

exchange = Exchange(account_address, secret_key, constants.TESTNET_API_URL)
order_result = exchange.order({
    "coin": "PURR",
    "is_buy": True,
    "sz": "1",
    "limit_px": "0.1",
    "order_type": {"limit": {"tif": "Gtc"}},
    "reduce_only": False
}, spot=True)
```

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure virtual environment is activated
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configuration Error**: Check your `config.json` file
   - Ensure `account_address` and `secret_key` are correctly set
   - Remove placeholder values like "0x..."

3. **Network Issues**: Check if you're using the right network
   - Testnet addresses work only on testnet
   - Mainnet addresses work only on mainnet

4. **Insufficient Balance**: Make sure your account has tokens
   - For Testnet: Get test tokens from Hyperliquid testnet faucet
   - For Mainnet: Deposit real tokens

### Getting Help

- Check the [Hyperliquid Documentation](https://hyperliquid.gitbook.io/)
- Review the [SDK Examples](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/tree/master/examples)
- Join the [Hyperliquid Discord](https://discord.gg/hyperliquid)

## ⚖️ License & Disclaimer

### License
MIT License - feel free to use and modify.

### Disclaimer
- This software is for educational purposes
- Trading cryptocurrencies involves significant risk
- You are responsible for your own trading decisions
- The authors are not responsible for any financial losses
- Always do your own research (DYOR)

### Risk Warning
- **Never invest more than you can afford to lose**
- **Cryptocurrency trading is highly volatile**
- **Past performance does not guarantee future results**
- **Use testnet for learning and experimentation**

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest improvements
- Add new example scripts
- Improve documentation

## 📞 Support

For issues with this repository, please create an issue.
For Hyperliquid platform support, contact their official channels.

---

**Happy Trading! 🚀** (But please be safe! 🛡️) 
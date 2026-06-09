# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders through a command-line interface (CLI).

The application includes:

* MARKET order placement
* LIMIT order placement
* BUY and SELL support
* Input validation
* Structured logging
* Error handling for API, validation, and network errors
* Environment-based API credential management

---

## Project Structure

trading_bot/

├── bot/

│   ├── **init**.py

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

├── logs/

│   └── trading.log

├── cli.py

├── .env

├── requirements.txt

└── README.md

---

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Credentials

Create a `.env` file in the project root:

```env
API_KEY=YOUR_API_KEY
API_SECRET=YOUR_API_SECRET
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Logging

All requests, responses, and errors are logged to:

```text
logs/trading.log
```

Example log entry:

```text
INFO | ORDER REQUEST | Symbol=BTCUSDT | Side=BUY | Type=MARKET | Qty=0.001
ERROR | BINANCE API ERROR | Code=-2015 | Message=Invalid API-key, IP, or permissions for action
```

---

## Error Handling

The application handles:

* Invalid user input
* Missing LIMIT order price
* Binance API exceptions
* Network errors
* Unexpected runtime exceptions

---

## Assumptions

* User possesses valid Binance API credentials.
* Binance Futures permissions are enabled for the API key.
* Internet connectivity is available.
* Binance Futures Testnet endpoint is accessible.

---

## Author

Submission for Python Developer Assessment – Primetrade.ai

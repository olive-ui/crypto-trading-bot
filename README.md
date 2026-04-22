# Crypto Trading Bot

A simple CLI-based trading bot built for Binance Futures Testnet.
It allows placing Market and Limit orders with proper validation, logging, and clean output.

---

## Features

* Place **Market** and **Limit** orders
* Supports both **BUY** and **SELL**
* CLI-based input using argparse
* Input validation to prevent invalid orders
* Logs all API requests, responses, and errors
* Clean and readable output in terminal

---

## Project Structure

```
crypto-trading-bot/
│
├── bot/
│   ├── client.py        # API handling and request signing
│   ├── orders.py        # Order execution logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
├── bot.log              # Sample logs
```

---

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file and add your API keys:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

## Usage

### Market Order

```
py cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

---

### Limit Order

```
py cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 79000
```

---

## Sample Output

```
Order placed successfully:
Order ID: 13061977542
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
```

---

## Logging

All activity is logged in:

```
bot.log
```

Includes:

* Request details
* API responses
* Errors

---

## Notes

* This project uses **Binance Futures Testnet**, so no real funds are used
* Orders may remain in `NEW` state due to testnet behavior

---
## Screenshots

### Market Order
<img width="1396" height="398" alt="image" src="https://github.com/user-attachments/assets/e3b7564d-5fb7-4ac6-a5b2-634bd2a02c46" />


### Limit Order
<img width="1692" height="349" alt="image" src="https://github.com/user-attachments/assets/48383419-c460-4245-b1f3-5a1c2fc4c119" />


### Error Handling
<img width="1683" height="245" alt="image" src="https://github.com/user-attachments/assets/584306f9-fee7-4fe5-86c4-dacfbe987fe4" />


## Tech Stack

* Python 3
* requests
* python-dotenv
* argparse

---

## Author

Aliviya Saha 

# crypto-trading-bot
CLI-based crypto trading bot for Binance Futures Testnet supporting Market and Limit orders with structured code, validation, logging, and API integration.
# Crypto Trading Bot

A simple CLI-based trading bot for Binance Futures Testnet.

## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Add API keys in `.env`

## Run

Market order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 60000

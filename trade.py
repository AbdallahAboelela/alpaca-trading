from config import *
import alpaca_trade_api as tradeapi
import threading
import time
import datetime

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

class LongShort:
	def __init__(self):
    self.alpaca = tradeapi.REST(API_KEY, SECRET_KEY, APCA_API_BASE_URL, 'v2')

    stockUniverse = ['DOMO', 'TLRY', 'SQ', 'MRO', 'AAPL', 'GM', 'SNAP', 'SHOP', 'SPLK', 'BA', 'AMZN', 'SUI', 'SUN', 'TSLA', 'CGC', 'SPWR', 'NIO', 'CAT', 'MSFT', 'PANW', 'OKTA', 'TWTR', 'TM', 'RTN', 'ATVI', 'GS', 'BAC', 'MS', 'TWLO', 'QCOM']

    self.long = []
    self.short = []

    self.queue_long = []
    self.queue_short = []
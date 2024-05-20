from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.trader import Trader
from datetime import datetime

API_KEY = "PKKGCTWU6361MKOTJ789"
API_SECRET = "WJrZ4Z1LQ5E0NvEeyq5pX1Qp2BSHErv43q74EKyC"
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDENTIALS = {
    "API_KEY" : API_KEY,
    "API_SECRET" : API_SECRET,
    "PAPER" : True
}

class MLTrader(Strategy):
    def initialize(self,symbol:str="SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"

    def on_trading_iteration(self):
        pass

start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)

broker = Alpaca(ALPACA_CREDENTIALS)
strategy = MLTrader(name="ml_trader", broker=broker, parameters={symbol="SPY"})

startegy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={symbol="SPY"}
)


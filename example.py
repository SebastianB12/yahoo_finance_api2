import pprint
import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

my_share = share.Share('MSFT')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          3,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          15)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(symbol_data)

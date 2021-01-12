from RealTimeStockPriceScript import Curr_Stock_Price
from Stock_threshold_alert import Curr_Price

#Real time Stock Price
print("Current price ",Curr_Stock_Price('SBIN'))

#Real time price with threshold and alert
print("Current price ",Curr_Price('RELIANCE',1950))

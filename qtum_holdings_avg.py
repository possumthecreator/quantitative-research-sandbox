import yfinance as yf

# Ticker Map: kkpny = "kpn na" | air.pa = "air fp", ato.pa = "ato fp"
# data last  manually updated 12-24-2021
# "Cash and other" holdings is listed at .45% - 1,855,135 "shares" (between ayx, bidu)
#
# The general idea is to track a publicly traded EFT fund and all of its underlying assets together yet independly, and with regard to the proportionate 
# ratio of the each share held by the ETF. The idea is to exploit potential price action discrepencies between the the ETF itself and the properly weighted
# average of each holding and observe any other interesting patterns.
#
# The static HOLDINGS constant does not provide ETF holdings data in real time and so is not expected reveal any useful patterns currently. ETFs are actively
# managed and therefore, the only reason for the static list is to experiment with the logistics of parsing so many data pointse. Access to some API that may
# provide up to date detailed ETF holding reports is crucial to make this idea as it stands truly useful.
# 
# Scraping and parsing data for ~70 tickers with conventional yfinance methods is painstaking at best.
#
# The price action differences that are collected from each underlying asset need to be converted to percentages from USD amounts.

HOLDINGS = {
	'adi':.0133, \
	'syna':.0137, \
    'amba':.0133, \
    'amd':.0144, \
    'mrvl':.0138, \
    'nvda':.0134, \
    'on':.0149, \
    'xlnx':.0138, \
    'cdns':.0146, \
    'acn':.0154, \
    'lscc':.0136, \
    'tsem':.0143, \
    '9613.t':.0141, \
    'snps':.0144, \
    '4185.t':.0144, \
    'qcom':.0143, \
    'msft':.0143, \
    'ter':.0145, \
    'klac':.0143, \
    'stm':.0142, \
    'onto':.0145, \
    'form':.0143, \
    'googl':.0142, \
    'rey.mi':.0141, \
    '6723.t':.0136, \
    'crus':.0148, \
    'mchp':.0143, \
    'nok':.0151, \
    'ifx.de':.014, \
    'nxpi':.0143, \
    'mstr':.0135, \
    'asml':.0143, \
    'amat':.0142, \
    'wit':.0155, \
    '9432.t':.0146, \
    'mu':.0157, \
    'lrcx':.014, \
    '6702.t':.0144, \
    '2454.tw':.0142, \
    'nati':.0142, \
    'noc':.015, \
    'txn':.0137, \
    '6501.t':.013, \
    'tsm':.0142, \
    'azta':.0132, \
    '6701.t':.0138, \
    '6502.t':.014, \
    'hpe':.0145, \
    'bah':.0139, \
    'splk':.0139, \
    'rtx':.0141, \
    'kkpny':.015, \
    'intc':.0142, \
    'lmt':.0146, \
    'mksi':.0146, \
    'tdc':.0144, \
    'estc':.0139, \
    '2357.tw':.0147, \
    'air.pa':.015, \
    'ibm':.0152, \
    '6503.t':.0146, \
    'oran':.0146, \
    'ayx':.0135, \
    'bidu':.0139, \
    'ato.pa':.0147, \
    'bb':.0146, \
    'baba':.0136, \
    'hon':.0144, \
    'prft':.0137, \
    'ionq':.0122
}

def qtum_price_moves():
    """Return the QTUM ETF price and daily price movement in real time for the purpose of real time comparison with a 
    weighted average the underlying securities."""

    current_price = float(yf.Ticker('qtum').info['previousClose']) #Using the 'previousClose' parameter as a placeholder for testing while market is closed
    open_price = float(yf.Ticker('qtum').info['open'])
    price_change = [(current_price - open_price)]

    try:
	    return price_change
    except ValueError:
        print("ERROR with qtum_price_moves")


def qtum_underly_price_moves():
    """Return a list of weighted price differences for each underlying asset in the
    Defiant QTUM ETF (from market open to current). When ran, the function takes the price change
    difference and calculates that against the percentage occupied of the QTUM ETF (added manually 
    so almost certainly dated). TODO: convert differences to percentages"""
    
    #Create dictionary containing each holding as keys and its percentage of QTUM as values
    global HOLDINGS
    price_change_weight = []
    
    # Note that for "current_price" I am using "previousClose" in order to test this while the market is closed
    for k, v in HOLDINGS.items():
        current_price = float(yf.Ticker(k).info['previousClose']) #Using the 'previousClose' parameter as a placeholder for testing while market is closed
        open_price = float(yf.Ticker(k).info['open'])
        price_change_weight += [(current_price - open_price) * v] # A list market price movement weighted by percentage held in QTUM
    
    try:
        return price_change_weight
    except ValueError:
        print("ERROR with qtum_underly_price_moves")


def calc_weighted_avg(price_moves=[]):
    """Takes an array of data and compiles into average."""

    avg_price_move = float(0)
    c = float(0)

    for i in price_moves:
        c = c + 1
        avg_price_move = ((avg_price_move + i) / c)

    try:
        return avg_price_move
    except ValueError:
        print("ERROR with calc_weighted_avg")


def main():
    qtum_moves = qtum_price_moves()
    price_moves = qtum_underly_price_moves()
    avg_price_moves = calc_weighted_avg(price_moves)

    print("\n******************************************************************************************************")
    print("\n", "QTUM Price Difference: \t\t\t\t", qtum_moves)
    print("\nQTUM Underlying Assets Weighted Movements Combined Average Difference: \t", avg_price_moves)
    print("\n******************************************************************************************************\n")


if __name__ == "__main__":
    main()

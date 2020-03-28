
from urllib.request import urlopen
import json

def get_jsonparsed_data(url):
    
    response = urlopen(url)
    data = response.read().decode('utf-8')
    return json.loads(data)

def get_EV_statement(ticker, period = 'annual'):
   
    if period == 'annual':
        url = 'https://financialmodelingprep.com/api/v3/enterprise-value/{}'.format(ticker)
    elif period == 'quarter':
        url = 'https://financialmodelingprep.com/api/v3/enterprise-value/{}?period=quarter'.format(ticker)
    return get_jsonparsed_data(url)


def get_income_statement(ticker, period = 'annual'):
    
    if period == 'annual':
        url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/{}'.format(ticker)
    elif period == 'quarter':
        url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/{}?period=quarter'.format(ticker)
    else:
        raise ValueError("in get_income_statement: invalid period")    

    return get_jsonparsed_data(url)


def get_cashflow_statement(ticker, period = 'annual'):
   
    if period == 'annual':
        url = 'https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/{}'.format(ticker)
    elif period == 'quarter':
        url = 'https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/{}?period=quarter'.format(ticker)
    else:
        raise ValueError("in get_cashflow_statement: invalid period")     

    return get_jsonparsed_data(url)

def get_balance_statement(ticker, period = 'annual'):
    
    if period == 'annual':
        url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{}'.format(ticker)
    elif period == 'quarter':
        url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{}?period=quarter'.format(ticker)
    else:
        raise ValueError("in get_balancesheet_statement: invalid period")   

    return get_jsonparsed_data(url)

def get_stock_price(ticker):
    
    url = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker)
    return get_jsonparsed_data(url)

def get_batch_stock_prices(tickers):
    
    prices = {}
    for ticker in tickers:
        prices[ticker] = get_stock_price(ticker)['price']

    return prices

def get_historical_share_prices(ticker, dates):
    
    prices = {}
    for date in dates:
        date_start, date_end = date[0:8] + str(int(date[8:]) - 2), date
        url = 'https://financialmodelingprep.com/api/v3/historical-price-full/{}?from={}&to={}'.format(ticker, date_start, date_end)
        try:
            prices[date_end] = get_jsonparsed_data(url)['historical'][0]['close']
        except IndexError:
            try:
                prices[date_start] = get_jsonparsed_data(url)['historical'][0]['close']
            except IndexError:
                print(date + ' ', get_jsonparsed_data(url))

    return prices

if __name__ == '__main__':

    ticker = 'AAPL'
    data = get_cashflow_statement(ticker)
    print(data)

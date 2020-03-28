import argparse
from decimal import Decimal

from modeling.data import *

def DCF(ticker, ev_statement, income_statement, balance_statement, cashflow_statement, discount_rate, forecast, earnings_growth_rate, cap_ex_growth_rate, perpetual_growth_rate):
   
    enterprise_val = enterprise_value(income_statement,
                                        cashflow_statement,
                                        balance_statement,
                                        forecast, 
                                        discount_rate,
                                        earnings_growth_rate, 
                                        cap_ex_growth_rate, 
                                        perpetual_growth_rate)

    equity_val, share_price = equity_value(enterprise_val,
                                           ev_statement)

    print('\nEnterprise Value for {}: ${}.'.format(ticker, '%.2E' % Decimal(str(enterprise_val))), 
              '\nEquity Value for {}: ${}.'.format(ticker, '%.2E' % Decimal(str(equity_val))),
           '\nPer share value for {}: ${}.\n'.format(ticker, '%.2E' % Decimal(str(share_price))),
            '-'*60)

    return {
        'date': income_statement[0]['date'],       
        'enterprise_value': enterprise_val,
        'equity_value': equity_val,
        'share_price': share_price
    }

def historical_DCF(ticker, years, forecast, discount_rate, earnings_growth_rate, cap_ex_growth_rate, perpetual_growth_rate, interval = 'annual'):

    dcfs = {}

    income_statement = get_income_statement(ticker = ticker, period = interval)['financials'] 
    balance_statement = get_balance_statement(ticker = ticker, period = interval)['financials']
    cashflow_statement = get_cashflow_statement(ticker = ticker, period = interval)['financials']
    enterprise_value_statement = get_EV_statement(ticker = ticker, period = interval)['enterpriseValues']

    if interval == 'quarter':
        intervals = years * 4
    else:
        intervals = years

    for interval in range(0, intervals):
        try:
            dcf = DCF(ticker, 
                    enterprise_value_statement[interval],
                    income_statement[interval:interval+2],        
                    balance_statement[interval:interval+2],
                    cashflow_statement[interval:interval+2],
                    discount_rate,
                    forecast, 
                    earnings_growth_rate,  
                    cap_ex_growth_rate, 
                    perpetual_growth_rate)
        except IndexError:
            print('Interval {} unavailable, no historical statement.'.format(interval))
        dcfs[dcf['date']] = dcf 
    
    return dcfs

def ulFCF(ebit, tax_rate, non_cash_charges, cwc, cap_ex):

    return ebit * (1-tax_rate) + non_cash_charges + cwc + cap_ex



def equity_value(enterprise_value, enterprise_value_statement):

    equity_val = enterprise_value - enterprise_value_statement['+ Total Debt'] 
    equity_val += enterprise_value_statement['- Cash & Cash Equivalents']
    share_price = equity_val/float(enterprise_value_statement['Number of Shares'])

    return equity_val,  share_price

def enterprise_value(income_statement, cashflow_statement, balance_statement, period, discount_rate, earnings_growth_rate, cap_ex_growth_rate, perpetual_growth_rate):
    
    ebit = float(income_statement[0]['EBIT'])
    tax_rate = float(income_statement[0]['Income Tax Expense']) /  \
               float(income_statement[0]['Earnings before Tax'])
    non_cash_charges = float(cashflow_statement[0]['Depreciation & Amortization'])
    cwc = (float(balance_statement[0]['Total assets']) - float(balance_statement[0]['Total non-current assets'])) - \
          (float(balance_statement[1]['Total assets']) - float(balance_statement[1]['Total non-current assets']))
    cap_ex = float(cashflow_statement[0]['Capital Expenditure'])
    discount = discount_rate

    flows = []

    print('Forecasted information for {} years out, starting at {}.'.format(period, income_statement[0]['date']),
         ('\n         DFCF   |    EBIT   | '))
    for yr in range(1, period+1):    

        
        ebit = ebit * (1 + (yr * earnings_growth_rate))
        non_cash_charges = non_cash_charges * (1 + (yr * earnings_growth_rate))
        cwc = cwc * 0.7                             
        cap_ex = cap_ex * (1 + (yr * cap_ex_growth_rate))         

        #WAC 
        flow = ulFCF(ebit, tax_rate, non_cash_charges, cwc, cap_ex)
        PV_flow = flow/((1 + discount)**yr)
        flows.append(PV_flow)

        print(str(int(income_statement[0]['date'][0:4]) + yr) + '  ',
              '%.2E' % Decimal(PV_flow) + ' | ',
              '%.2E' % Decimal(ebit) + ' | ')
    NPV_FCF = sum(flows)
    final_cashflow = flows[-1] * (1 + perpetual_growth_rate)
    TV = final_cashflow/(discount - perpetual_growth_rate)
    NPV_TV = TV/(1+discount)**(1+period)

    return NPV_TV+NPV_FCF


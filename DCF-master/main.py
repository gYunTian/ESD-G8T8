import argparse

from modeling.data import *
from modeling.dcf import *


def main(args):
    if args.s > 0:
        if args.v is not None:
            if args.v == 'eg' or 'earnings_growth_rate':
                cond, dcfs = run_setup(args, variable = 'eg')
            elif args.v == 'cg' or 'cap_ex_growth_rate':
                cond, dcfs = run_setup(args, variable = 'cg')
            elif args.v == 'pg' or 'perpetual_growth_rate':
                cond, dcfs = run_setup(args, variable = 'pg')
            elif args.v == 'discount_rate' or 'discount':
                cond, dcfs = run_setup(args, variable = 'discount')
            
            else:
                raise ValueError('args.variable is invalid')
        else:
           
            raise ValueError('Invalid')
    else:
        cond, dcfs = {'Ticker': [args.t]}, {}
        dcfs[args.t] = historical_DCF(args.t, args.y, args.p, args.d, args.eg, args.cg, args.pg, args.i)

    
def run_setup(args, variable):
    dcfs, cond = {}, {args.v: []}
    
    for increment in range(1, int(args.steps) + 1):
        var = vars(args)[variable] * (1 + (args.s * increment))
        step = '{}: {}'.format(args.v, str(var)[0:4])

        cond[args.v].append(step)
        vars(args)[variable] = var
        dcfs[step] = historical_DCF(args.t, args.y, args.p, args.d, args.eg, args.cg, args.pg, args.i)

    return cond, dcfs



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--p', '--period', help = 'years to forecast', type = int, default =  5)
    parser.add_argument('--t', '--ticker', help = 'pass a single ticker to do historical DCF', type = str, default = 'AAPL')
    parser.add_argument('--y', '--years', help = 'number of years to compute DCF analysis for', type = int, default = 1)
    parser.add_argument('--i', '--interval', help = 'interval period for each calc, either "annual" or "quarter"', default = 'annual')
    parser.add_argument('--s', '--step_increase', help = 'specify step increase for EG, CG, PG to enable compari lcsons.', type = float, default = 0)
    parser.add_argument('--steps', help = 'steps to take if --s is > 0', default = 5)
    parser.add_argument('--v', '--variable', help = 'if --step_increase is specified, must specifiy variable to increase from: [earnings_growth_rate, discount_rate]', default = None)
    parser.add_argument('--d', '--discount_rate', help = 'discount rate for future cash flow to firm', default = 0.05)
    parser.add_argument('--eg', '--earnings_growth_rate', help = 'growth in revenue, YoY',  type = float, default = 0.01)
    parser.add_argument('--cg', '--cap_ex_growth_rate', help = 'growth in cap_ex, YoY', type = float, default = 0.01)
    parser.add_argument('--pg', '--perpetual_growth_rate', help = 'for perpetuity growth terminal value', type = float, default = 0.04)

    args = parser.parse_args()
    main(args)

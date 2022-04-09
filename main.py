import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', choices = ['diff', 'annuity'], help = "You can select either 'diff' or 'annuity'")
parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--interest',type=float)
parser.add_argument('--periods', type=float)

args = parser.parse_args()

def num_of_months(principal, payment, interest):
    i = interest/(12*100)
    a = payment
    p = principal  
    x = (a / (a - i * p))
    base = 1 + i
    n = math.log(x, base)
    return n
    
def annuity_payment(principal, interest, periods):
    i = interest/(12*100)
    n = periods
    p = principal   
    a = p * (i*(1+i)**n)/(((1+i)**n)-1)
    return a 

def loan_principal(payment, interest, periods):
    a = payment
    i = interest/(12*100)
    n = periods
    p = a/((i*(1+i)**n)/((1+i)**n-1))
    return p
    
def diff(principal, loan_interest, periods, m):
    i = interest/(12*100)
    n = periods
    p = principal
    d = p/n + i * (p - (p*(m-1))/n)   
    return d

if args.type == 'annuity' and args.interest != None:
    if args.periods == None:
    #loan_principal = float(input('Enter the loan principal:'))
    #payment = float(input('Enter the monthly payment:'))
    #loan_interest = float(input('Enter the loan interest:'))
        principal = args.principal
        payment = args.payment
        interest = args.interest
    
        period = math.ceil(num_of_months(principal, payment, interest))
        if period % 12 != 0:
            x,y = divmod(period,12)
            print('It will take {} years and {} months to repay this loan!'.format(x,y))
        elif period % 12 == 0:
            x = period/12
            print('It will take {} years to repay this loan!'.format(round(x)))
        
        overpayment = (period * payment) - principal
        print('Overpayment: {}'.format(overpayment))
        
    if args.payment == None:

        principal = args.principal
        periods = args.periods
        interest = args.interest
    
        ans = math.ceil(annuity_payment(principal, interest, periods)) 
        print('Your monthly payment = {}!'.format(ans))
    
    if args.principal == None:

        payment = args.payment
        periods = args.periods
        interest = args.interest
     
        loan_p = round(loan_principal(payment, interest, periods))
        print('Your loan principal = {}!'.format(loan_p))

elif args.type == 'diff' and args.payment == None and args.interest != None:
    
    principal = args.principal
    periods = args.periods
    interest = args.interest  
    m = 1
    overpayment = 0
    while periods >= m:
        diff_n = math.ceil(diff(principal, interest, periods, m))
        print('Month {}: payment is {}'.format(m, diff_n))
        overpayment = overpayment + diff_n
        m += 1
    overpayment = overpayment - principal
    print('Overpayment = {}'.format(overpayment))
    
else:
    print('Incorrect Parameters')
    

#Python Porgram to calculate simple interst
#Simple interest = (Principal Amount * Rate of Interest * Number of years) / 100

def simple_interest_calculator(p, r, n):
   simpleInterest =( p * r * n ) / 100
   return simpleInterest

p = float(input('Enter Principle Amount: '))
r = float(input('Enter Rate of Interest: '))
n = float(input('Enter Number of years: '))
si = ( p * r * n ) / 100

def total_repayment(simpleInterest):
    output = p + si
    return output

print('Simple Interest: {}'.format(simple_interest_calculator(p, r, n)))
print('In total you will pay: $ {}'.format(total_repayment(si)))



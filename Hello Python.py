# Credit card analysis

# PAYING THE MINIMUM

# Variables
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Calculations
monthlyInterestRate = annualInterestRate / 12
totalPayment = 0
currBalance = balance
for i in range(12):       
    payment = currBalance * monthlyPaymentRate
    totalPayment += payment
    unpaid = currBalance - payment
    currBalance = unpaid + (unpaid * monthlyInterestRate)
    print 'Month:', i+1
    print 'Minimum monthly payment:', round(payment,2)
    print 'Remaining balance:', round(currBalance,2)
print 'Total paid:', round(totalPayment,2)
print 'Remaining balance:', round(currBalance,2)


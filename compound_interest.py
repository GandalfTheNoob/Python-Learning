# Compound Interest Calculator v0.01
# Created by GandalfTheNoob
# Date: March 2016 - ????
# This calculator will ask the user for: initial amount, annual interest rate,
# amortization period, and how often compound interest is calculated.
# The calculator will display a summary of period-end interest earned and totals.



###### Formula and explanation:
# Annual compound interest formula
#
# The formula for annual compound interest is A = P (1 + r/n) ^ nt:
#
# Where:
#
# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per year
# t = the number of years the money is invested or borrowed for
#######

from decimal import Decimal

# declare & assign variables

annualInterest = 0.0    #annual interest to be compounded
initialAmount = 0.0     #initial amount of money to be calculated
amortPeriod = 0         #number of years to be amortized
calcPerYear = 0         #number of times per year amortization occurs

# Get user input for each variable needed
annualInterest = float(raw_input("Enter the annual interest rate: "))
initialAmount = float(raw_input("Enter the amount of starting money: "))
amortPeriod = int(raw_input("Enter the number of years to be amortized: "))
calcPerYear = int(raw_input("Enter the number of times per year the amoritization calculation occurs: "))

# Assign totalSum to the formula using the imported Decimal module
totalSum = Decimal(initialAmount * (1 + ((annualInterest/100) / calcPerYear)) ** (calcPerYear * amortPeriod))

# Print out the calculation
print "The total interest and initial amount after", amortPeriod, "years of compounding is: ", totalSum.quantize(Decimal('1.00'))

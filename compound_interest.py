# Compound Interest Calculator v0.30
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

from decimal import Decimal, getcontext

# declare & assign variables
getcontext().prec=8
annualInterest = 0.0    #annual interest to be compounded
initialAmount = 0.0     #initial amount of money to be calculated
amortPeriod = 0         #number of years to be amortized
calcPerYear = 0         #number of times per year amortization occurs

# Get user input for each variable needed
annualInterest = Decimal(raw_input("Enter the annual interest rate: "))
initialAmount = Decimal(raw_input("Enter the amount of starting money: "))
amortPeriod = Decimal(raw_input("Enter the number of years to be amortized: "))
calcPerYear = Decimal(raw_input("Enter the number of times per year the amoritization calculation occurs: "))

# Method to calculate the interest and total amount
def calc_int_earned(annInt, iniAmt, amoPer, perYear):
    
    # Assign totalSum to the formula using the imported Decimal module
    totalSum = Decimal(iniAmt * (1 + ((annInt/100) / perYear)) ** (perYear * amoPer))

    # Print out the calculation
    print "The total interest and initial amount after", amoPer, "years of compounding is: $", totalSum.quantize(Decimal('1.00'))

    #Print out the interest earned over the entire period
    print "The interest earned over {} years is ${}".format(amoPer, (totalSum - iniAmt).quantize(Decimal('1.00')))

# Call the method using user input
calc_int_earned(annualInterest, initialAmount, amortPeriod, calcPerYear)

# TO-DO v0.10
# Create a method to show a calc by calc table of beginning, interest earned,
# and ending balance.

def calc_table(annInt, iniAmt, amoPer, perYear):
    currentSum = iniAmt
    intRate = (annInt / perYear)/100
    print "passed interest: ", annInt
    print "passed amoortization period:", perYear
    print "calculted interest rate:", intRate
    intCalc = intRate * currentSum
    i = 1
    totalSum = currentSum + intCalc
    print "_________________________________"
    while i < (amoPer * perYear)+1:
        print "|", i, "|", currentSum, "|", intRate * currentSum, "|", currentSum + (intRate * currentSum), "|"
        i += 1
        currentSum += (intRate * currentSum)
    print "_________________________________"
    return currentSum

#call the calc_table method
calc_table(annualInterest, initialAmount, amortPeriod, calcPerYear)




# TO-DO v0.20
# Create a method that compares 3 user-defined interest rates to compare over time.
# This method will be a general result that displays beginning, end, and interest earned
# for each of the requested interest rates.

first_int = Decimal(raw_input("Enter the 1st rate to be compared:"))
second_int = Decimal(raw_input("Enter the 2nd rate to be compared:"))
third_int = Decimal(raw_input("Enter the 3rd rate to be compared:"))

print "The first interest rate,", first_int, "%"
calc_int_earned(first_int, initialAmount, amortPeriod, calcPerYear)
print ""
print "The second interest rate,", second_int, "%"
calc_int_earned(second_int, initialAmount, amortPeriod, calcPerYear)
print ""
print "The third interest rate,", third_int, "%"
calc_int_earned(third_int, initialAmount, amortPeriod, calcPerYear)

# TO-DO v0.30
# Create a method that displays takes a users' request for ending and starting balance and
# years of compound interest to find out what interest rate they need to get
# the end balance in the number of years entered.
# formula: final/initial ^ (1/years)-1

def ror():
    print "interest rate needed to earn a final amount after depositing an initial amount over a certain number of years."
    print ""

    final_amt = float(raw_input("How much is your final amount?"))
    begin_amt = float(raw_input("How much will you start with?"))
    years_amt = int(raw_input("How many years will this initial amount have to compound?"))
    ror = ((final_amt / begin_amt)**(1/float(years_amt))-1)*100
    print ror
    
    print "You will need: %0.2f percent to get $ %0.2f after %i years." %(ror, final_amt, years_amt)

ror()

# TO-DO v0.40
# Create a start menu to select via number which type of calculation they want to run.
# We have currently have three options:
# 1. Interest earned & Total
# 2. Compound Interest table
# 3. Interest Rate Compare
# 4. What interest rate do I need?

# TO-DO v.50
# Work on GUI

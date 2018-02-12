"""
Tax Calculations!
The country of “Syracusia” determines your tax rate from the number of dependents:
0 ➔ 30%
1 ➔ 25% 
2 ➔ 18% 
3 or more➔ 10%  
Write a program to prompt for number of dependents (0-3) and annual income.
It should then calculate your tax rate and tax bill. Format numbers properly!

"""

num_of_deps = input("Please enter the number of dependents: ")
try:
    num_of_deps = int(num_of_deps)
    annual_inc = input("Please enter you annual income: ")

    if num_of_deps == 0:
        tax_rate = .3
    elif num_of_deps == 1:
        tax_rate = .25
    elif num_of_deps == 2:
        tax_rate = .18
    else:
        tax_rate = .1

    tax_bill = float(annual_inc) * tax_rate

    print("You tax rate is {}".format(tax_rate))
    print("You tax bil: ${:.2f}".format(tax_bill))

except:
    print("Please enter a valid input: ")
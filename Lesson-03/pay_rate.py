"""
Pay Rate Example:

Write a program to prompt for inputs hourly rate and hours worked, then output total pay. Then input tax rate and output net pay.

Rewrite the program with better formatting


Problem Analysis
Inputs: hourly rate, hours worked, and tax rate

Outputs: total pay and net pay 

Algorithm: (hourly rate * hours worked) * tax rate

"""

hourly_rate = input("Please enter your hourly rate. ")
hours_worked = input("Please enter your hours worked. ")
total_pay = float(hourly_rate) * float(hours_worked)
tax_rate = input("Please enter the tax rate. ")
tax = total_pay * float(tax_rate)
netpay = total_pay - tax
print("*"*80)
print("PAY CALCULATOR")
print("*"*80)
print("Total pay: ${:.2f}".format(total_pay))
print("Tax: ${:.2f}".format(tax))
print("Netpay: ${:.2f}".format(netpay))
print("*"*80)
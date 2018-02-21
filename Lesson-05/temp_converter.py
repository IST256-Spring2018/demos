"""
Temperature Conversions as functions
Two functions f2c and c2f:
Write a program that converts between the two
T(°C) = (T(°F) - 32) × 5/9
T(°F) = T(°C) × 9/5 + 32
"""

def f2c(ftemp):
    return (ftemp - 32) * 5/9

def c2f(ctemp):
    return (ctemp * 9/5) + 32

try:
    temp = int(input("Please enter a temperature: "))
    corf = input("C/F")

    if corf == "C":
        ftem = c2f(temp)
        print("The F: {}".format(ftem))
    if corf == "F":
        ctem = f2c(temp)
        print("The celcius: {}".format(ctem))
except:
    print("Please enter a valid number ")





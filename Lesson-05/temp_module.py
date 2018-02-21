"""
Temperature Conversions as functions
Two functions f2c and c2f:
Write a program that converts between the two
T(°C) = (T(°F) - 32) × 5/9
T(°F) = T(°C) × 9/5 + 32
"""
import pytemperature as pt

pt = 5

try:
    temp = int(input("Please enter a temperature: "))
    corf = input("C/F")

    if corf == "C":
        ftem = pt.c2f(temp)
        print("The F: {}".format(ftem))
    if corf == "F":
        ctem = pt.f2c(temp)
        print("The celcius: {}".format(ctem))
except:
    print("Please enter a valid number ")
"""
Write a program that asks for you first name and last name.
And prints it our 2 ways

Example:
"Hello Nick Lyga"
"Hello Lyga, Nick"

"""

"""
Problem Analysis

Inputs:
Please enter first name
Please enter last name
Outputs:
"Hello First Name Last Name
"Hello Last Name First Name"
Algorigthm:
print the outputs
"""

# Write your code here!
firstname = input("Please Enter first name: ")
lastname = input("Please Enter last name: ")

print("Hello", firstname, lastname)
print("Hello {}, {}".format(firstname, lastname))

animal = input("Please enter an animal: ")
action = input("Please enter an action: ")

print("The {} {}".format(animal, action))


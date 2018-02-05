"""

#1: Variable assignment and call (getter and setters)
    - User input is ALWAYS a string!

#2: Everything in python is an object!
    - Using type()
    - Using id()

#3: Converting between types

#4: Expressions and Operators 

"""

name = input("Please enter your name: ")
age = input("Please enter you age: ")

# User input is always a string!
print("'name' is a", type(name))
print("'age' is a", type(age))

your_name = name
# both variables now point to the same memory address!
print("'your_name' id: ", id(your_name))
print("'name' id: ", id(name))
print("The value of 'your_name': ", your_name)
print("The value of 'name': ", name)

# But if you re-assign one it will point to a different memory address. and the other will keeps its original value
your_name = "new name!"
print("'your_name' id: ", id(your_name))
print("'name' id: ", id(name))
print("The value of 'your_name': ", your_name)
print("The value of 'name': ", name)

# Expressions!

suffix = input("Please enter a suffix: ")
retirement_age = input("Please enter your retirement age: ")

# This is an expression, using string operations
# Expression evaluate to a value, that values gets returned
# and stored in a variable.
full_name = name + " " + suffix

# We can also repeat strings
print("*" * 80)

# This is an expression using numeric operations
# But this is going to throw an error
# years_to_go = retirement_age - age

# Why? 

# How do we fix this? 
# Type conversions!
years_to_go = int(retirement_age) - int(age)

# Print is nice and coverts it for us.
print("You have", years_to_go, "until you retire")
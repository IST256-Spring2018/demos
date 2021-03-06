''' 
Create a program that calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12.

Repeatedly asks the user for the number of times to roll the dice, quitting only when the user-entered number is less than 1. Hint: Use a while loop that will execute as long as num_rolls is greater than 1.

Prints a histogram in which the total number of times the dice rolls equals each possible value is displayed by printing a character, such as *, that number of times. The following provides an example:

Example Run:

Dice roll histogram:

2s:  **
3s:  ****
4s:  ***
5s:  ********
6s:  *************
7s:  *****************
8s:  *************
9s:  *********
10s: **********
11s: *****
12s: **

'''
import random

my_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    try:
        print("Please enter how many rolls, or -1 to quit")
        rolls = int(input("How many rolls would of the dice: "))
        if rolls < 0:
            break
        for num in range(0, rolls):
            r1 = random.randint(1, 6)
            r2 = random.randint(1, 6)
            total = r1 + r2
            my_values[total - 2] += my_values[total - 2] + 1
    except:
        print("Please enter a valid value")

print("Your roll totals")
counter = 2
for val in my_values:
    print("{}s:".format(counter), "*"*val)
    counter += 1



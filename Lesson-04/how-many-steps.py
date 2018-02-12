"""
How many steps have you taken?

# 1 Enter Steps Manually

# 2 User googe fit!

"""

import google_fit

steps = input("Please enter you step count: ")
if int(steps) >= 10000:
    print("Good Job!")
elif int(steps) > 9000:
    print("Almost there!")
elif int(steps) > 5000:
    print("Half way there!")
else:
    print("Stop being lazy")

print("Program ended")
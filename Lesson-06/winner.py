"""
By: Qiwu Zou, jingwen zeng
"""

import random

two = three = four = five = six = seven = eight = nine = ten = eleven = twelve = 0
num = {2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten, 11:eleven, 12: twelve}
while (True):
    count = int(input("please enter the number of times to roll the dice"))
    if (count < 1):
        break
    while (count > 0):
        count = count - 1
        result = random.randint(1,6) + random.randint(1,6)
        num[result] = num[result] + 1
for x in num:
    print (x, 's', '*'*num[x])
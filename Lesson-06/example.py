import random
two_to_twelve = 0
roll_two = 0
roll_three = 0
roll_four = 0
roll_five = 0
roll_six = 0
roll_seven = 0
roll_eight = 0
roll_nine = 0
roll_ten = 0
roll_eleven = 0
roll_twelve = 0
while True:
    
    num_rolls = int(input('Enter number of rolls: '))
    if num_rolls >= 1:
        for i in range(num_rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            roll_total = die1 + die2        
            if roll_total == 2:
                roll_two = (roll_two + 1)
            if roll_total == 3:
                roll_three = (roll_three + 1)
            if roll_total == 4:
                roll_four = (roll_four + 1)
            if roll_total == 5:
                roll_five = (roll_five + 1)
            if roll_total == 6:
                roll_six = (roll_six + 1)
            if roll_total == 7:
                roll_seven = (roll_seven + 1)
            if roll_total == 8:
                roll_eight = (roll_eight + 1)
            if roll_total == 9:
                roll_nine = (roll_nine + 1)
            if roll_total == 10:
                roll_ten = (roll_ten + 1)
            if roll_total == 11:
                roll_eleven = (roll_eleven + 1)
            if roll_total == 12:
                roll_twelve = (roll_twelve + 1)
            print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))
        
    if num_rolls < 1:
        break
        

print('Dice roll histogram:')
print('2s:  ', ("*" * (roll_two)))
print('3s:  ', ("*" * (roll_three)))
print('4s:  ', ("*" * (roll_four)))
print('5s:  ', ("*" * (roll_five)))
print('6s:  ', ("*" * (roll_six)))
print('7s:  ', ("*" * (roll_seven)))
print('8s:  ', ("*" * (roll_eight)))
print('9s:  ', ("*" * (roll_nine)))
print('10s: ', ("*" * (roll_ten)))
print('11s: ', ("*" * (roll_eleven)))
print('12s: ', ("*" * (roll_twelve)))
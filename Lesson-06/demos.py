# list_of_items = ["yellow", "red", "black"]

# for item in range(0, 10):
#     print(item)

my_name = "Nick"
guesses = 1
while True:
    user_input = input("Please enter a name: ")
    if user_input == my_name:
        print("Good Job You guessed right!")
        break
    guesses = guesses + 1
    if guesses <= 3:
        print("WRONG!!!!!! Guess again")
    else:
        print("Too Many guesses!")
        break

print("End of program")


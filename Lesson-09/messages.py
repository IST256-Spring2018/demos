message = input("Please enter a message")

with open("messages.txt", "a") as file:
    file.write(message + "\n")

print("Done writing")

messages = []
with open("messages.txt", "r") as file:
    for line in file:
        messages.append(line.strip())


for m in messages:
    print(m)

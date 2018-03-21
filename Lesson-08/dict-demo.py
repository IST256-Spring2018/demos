# Create new Dictionary
person = {
    "first_name": "Nick Lyga",
    "age": 21
}

print(person)

# Update key/Values
person["first_name"] ="Nick"
person["last_name"] = "Lyga"
print(person)

# Loop over dictionary (items())
for key,value in person.items():
    print("{}: {}".format(key, value))

# Methods, get(), values(), keys()
print(person.keys())

person.update({
    "first_name": "bob",
    "age": 5
})
print(person)


# delete del
del person["first_name"]
print(person)

# List of Dictionaires
people = []
person = {
    "name": "Nick",
    "age": 21
}
people.append(person)
print(people)
person2 = {
    "name": "billy",
    "age": 10
}
people.append(person2)
print(people)

print(people[1]["name"])


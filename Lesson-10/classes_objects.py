"""
Create a person class
"""


# import jsonpickle

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

new_person = Person("Nick", "Lyga")
print(new_person.fullname())

another_person = Person("john", "doe")
print(another_person.fullname())
# people = []

# # Add People
# people.append(Person("Frodo", "Baggins"))
# people.append(Person("Daenerys", "Targaryen"))
# people.append(Person("Kesuke", "Miyagi"))


# jsondata = jsonpickle.encode(people)

# # Save data to file..

# # Load data from file


# people2 = jsonpickle.decode(jsondata)

# for person in people2:
#     print(person.fullname())

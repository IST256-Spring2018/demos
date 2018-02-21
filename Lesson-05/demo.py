

def full_name(first_name, last_name):
    return first_name + " " + last_name


fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")

long_name = full_name(fname, lname)

print(long_name)

fname1 = input("Someone else enter their first name: ")
lname1 = input("Someone else enter their last name: ")

long_name = full_name(fname1, lname1)

print(long_name)
user_input = input("Please enter Yes(y) or No(n)")
user_input = user_input.lower()
if user_input[0] == "y":
    print("You entered Yes")
else:
    print("You entered no")

print(user_input)

# Split 

user_grades = input("Please enter your grades separated by a comma ")

user_grade_list = user_grades.split(",")

total = 0
for grade in user_grade_list:
    grade = grade.strip()
    grade = int(grade)
    total = total + grade

print(total)
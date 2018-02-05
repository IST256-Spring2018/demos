"""
Code Challenge: Mad-Libs!

See Readme.md for instructions

http://www.madlibs.com/content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf

Problem Analysis

Inputs: 
some adjective
some verbs
some nouns

Outputs:
madlib

Algorithm (Steps in Program):
ask the user for the required inputs
generate madlib
print it out


"""

print("Mad-Lib Generator")
print("Please enter the inputs asked for, and I will generate you custom Mad-Lib.")


# adj1 = input("Please enter an adjective: ")
# adj2 = input("Please enter another adjective: ")
# adj3 = input("Please enter another adjective: ")
# noun1 = input("Please enter a noun: ")
# noun2 = input("Please enter another noun: ")
# noun3 = input("Please enter another noun: ")
# plural_noun1 = input("Please enter another plural noun: ")
# plural_noun2 = input("Please enter another plural noun: ")
# plural_noun3 = input("Please enter another plural noun: ")
# plural_noun4 = input("Please enter another plural noun: ")
# plural_noun5 = input("Please enter another plural noun: ")
# verb1_ing = input("Please enter a verb ending in 'ing': ")
# verb2_ing = input("Please enter another verb ending in 'ing': ")
# verb3_ing = input("Please enter another verb ending in 'ing': ")
# verb4_ing = input("Please enter another verb ending in 'ing': ")
# game = input("Please enter a game: ")
# plant = input("Please enter plant: ")
# body_part = input("Please enter a body part: ")
# place = input("Please enter a place: ")
# number = input("Please enter a number: ")

adj1 = ""
adj2 = "sleepy"
adj3 = "tired"
noun1 = "dog"
noun2 = "tree"
noun3 = "cat"
plural_noun1 = "fish"
plural_noun2 = "leaves"
plural_noun3 = "students"
plural_noun4 = "bears"
plural_noun5 = "cars"
verb1_ing = "running"
verb2_ing = "swimming"
verb3_ing = "walking"
verb4_ing = "climbing"
game = "monopoly"
plant = "flower"
body_part = "arm"
place = "school"
number = "50"

# print("A vacation is when you take a trip to some", adj1, "place")
# print("with your", adj2, "family. Usually you go to some place")
# print("that is near a/an", noun1, "or up on a/an", noun2, ".")
# print("A good vacation place is one where you can ride", plural_noun1)
# print("or play", game, "or go hunting for", plural_noun2, ". I like")
# print("to spend my time", verb1_ing, "or", verb2_ing, ".")
# print("When parents go on a vacation, they spend their time eating")
# print("three", plural_noun3, "a day, and fathers play golf, and mothers")
# print("sit around", verb3_ing, ". Last summer, my little brother")
# print("fell in a/an", noun3, " and got poison", plant, "all")
# print("over his", body_part, ". My family is going to go to (the)")
# print(place, "and I will practice", verb4_ing, ". Parents")
# print("need vacations more than kids because parents are always very")
# print(adj3, "and because they have to work", number)
# print("hours every day all year making enough", plural_noun5, "to pay")
# print("for the vacation.")

# madlib = """
# A vacation is when you take a trip to some {adj1} place
# with your {adj2} family. Usually you go to some place
# that is near a/an {noun1} or up on a/an {noun2}.
# A good vacation place is one where you can ride {plural_noun1}
# or play {game} or go hunting for {plural_noun2}. I like
# to spend my time {verb1_ing} or {verb2_ing}.
# When parents go on a vacation, they spend their time eating
# three {plural_noun3} a day, and fathers play golf, and mothers
# sit around {verb3_ing}. Last summer, my little brother
# fell in a/an {noun3} and got poison {plant} all
# over his {body_part}. My family is going to go to (the)
# {place}, and I will practice {verb4_ing}. Parents
# need vacations more than kids because parents are always very
# {adj3} and because they have to work {number}
# hours every day all year making enough {plural_noun5} to pay
# for the vacation.
# """

# print(madlib.format(adj1=adj1, adj2=adj2, adj3=adj3, noun1=noun1, noun2=noun2, noun3=noun3, plural_noun1=plural_noun1, plural_noun2=plural_noun2, plural_noun3=plural_noun3, plural_noun4=plural_noun4, plural_noun5=plural_noun5, verb1_ing=verb1_ing, verb2_ing=verb2_ing, verb3_ing=verb3_ing, verb4_ing=verb4_ing, game=game, plant=plant, body_part=body_part, place=place, number=number))


madlib = """
A vacation is when you take a trip to some %s place
with your %s family. Usually you go to some place
that is near a/an %s or up on a/an %s.
A good vacation place is one where you can ride %s
or play %s or go hunting for %s. I like
to spend my time %s or %s.
When parents go on a vacation, they spend their time eating
three %s a day, and fathers play golf, and mothers
sit around %s. Last summer, my little brother
fell in a/an %s and got poison %s all
over his %s. My family is going to go to (the)
%s, and I will practice %s. Parents
need vacations more than kids because parents are always very
%s and because they have to work %s
hours every day all year making enough %s to pay
for the vacation.
"""

# print(madlib % (adj1, adj2, adj3, noun1, noun2, noun3, plural_noun1, plural_noun2, plural_noun3, plural_noun4, plural_noun5, verb1_ing, verb2_ing, verb3_ing, verb4_ing, game, plant, body_part, place, number))

verb = "3"
int(verb)



"""
Questions:

What happens if someone just hits enter instead of actually entering a value?
Does the code still run and why? What would you check for to stop this?

What happens if someone enters a 3 for one of the inputs?
Does the code still run and why?

What would happen if one of you inputs ended a sentence and was followed by a period? What happens?
How would we correct this? (Experiment with this, if your code does not have an example then add one to see
what happens, DO NOT LEAVE YOUR EXPERIMENTAL CODE IN YOUR SUBMITTED SOLUTIONS)


"""
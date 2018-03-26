"""

inputs:
    file for beer info
    ask the user for a beer
output:
    the calorie for the beer
"""


"""
inputs: filename
outputs: list of beers
algorithm: open file load list of beers
"""
def get_beers(filename):
    beers = []
    with open(filename, "r") as file:
        for line in file:
            beersplits = line.split(",")
            beerdict = {
                "name": beersplits[0],
                "calorie": int(beersplits[1])
            }
            beers.append(beerdict)
    return beers

"""
inputs:
    user entered beername
    list of beers to search
outputs beer dictionary
"""
def search(beername, beers):
    for beer in beers:
        if beer["name"].lower().startswith(user_beer.lower()):
            return beer
    return None

beers = get_beers("beer-calories.txt")
while True:
    user_beer = input("What beer do you want to drink? or q to quit ")
    if user_beer == "q":
        break
    beer = search(user_beer, beers)
    if beer is None:
        print("Could not find beer ")
    else:
        print("{}: {}".format(beer["name"], beer["calorie"]))

print("Program Finished")
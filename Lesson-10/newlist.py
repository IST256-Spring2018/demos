
# class MyList():
#     myindex = 0

#     def get_my_index(self):
#         return self[self.myindex]

# new_list = MyList([1, 2, 3])
# print(new_list.get_my_index())

# new_list.myindex = 1
# print(new_list.get_my_index())


# class Tweet(str):

#     def get_mentions(self):
#         words = self.split()
#         mentions = []
#         for word in words:
#             if word.startswith("@"):
#                 mentions.append(word)
#         return mentions

# tweet = Tweet("This is my tweet @someone, @someonelse")

# print(tweet.get_mentions())


class Animal():
    
    def __init__(self, name):
        self.name = name

    def walking(self):
        print("{} is Walking".format(self.name))

class Dog(Animal):
    
    def bark(self):
        print("{} is barking".format(self.name))


class Cat(Animal):
    def meowing(self):
        print("{} is meowing".format(self.name))

dog = Dog("Lassie")
cat = Cat("Garfield")

dog.walking()
cat.walking()
cat.meowing()
dog.bark()

my_list = [10, 15]

my_list.append(50)
my_list.append(100)
print(my_list)

# looping
for item in my_list:
    print(item)

# Indexes and Slicing
print(my_list[0:3])
print(my_list[-1])

# List Mutation
my_list[0] = 500
print(my_list)

# Aggregation (Counting, sum, min, max, len)
print(sum(my_list))
print(len(my_list))
print(max(["a", "c", "b"]))
my_list = ["a", "z", "l"]
my_list.sort()

print(my_list)

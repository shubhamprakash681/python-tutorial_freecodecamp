# Note:- Tuples in Python are innumerable.
# ie, they can't be changed once declared

coordinates = (4, 5)
print(coordinates)
print(coordinates[-2])

# coordinates[0] = 45 # error -> tuples can't be assigned(modified)

# list of tuples
tup_list = [(1, 2), (3, 4), (5, 6), (36, 43)]
print(tup_list)
print(tup_list[3])
# tup_list[2][0] = 7  # error
tup_list[2] = (56, 996)
print(tup_list)

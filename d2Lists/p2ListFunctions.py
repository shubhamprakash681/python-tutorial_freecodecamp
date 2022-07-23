lucky_numbers = [1, 2, 3, 445, 434, 5, 234]
friends = ['Rahul', 'Shubham', 'Bunny', 'Dhanny', 'Saurav', 'Sameer']

print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append('Jeetu')
print(friends)

friends.insert(0, 'Hunny')
print(friends)

friends.remove(2)
print(friends)

friends.pop()
print(friends)

print(friends.index('Shubham'))

friends.append('Shubham')
print(friends.count('Shubham'))

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

print()
new_list = lucky_numbers.copy()
print(new_list)

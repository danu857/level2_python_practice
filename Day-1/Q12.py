numbers = [10, 20, 30, 40, 50]

print("Original List :", numbers)

# append()
numbers.append(60)
print("After append() :", numbers)

# insert()
numbers.insert(2, 25)
print("After insert() :", numbers)

# extend()
numbers.extend([70, 80])
print("After extend() :", numbers)

# remove()
numbers.remove(25)
print("After remove() :", numbers)

# pop()
removed_value = numbers.pop()
print("Removed value :", removed_value)
print("After pop() :", numbers)

# count()
print("Count of 20 :", numbers.count(20))

# index()
print("Index of 30 :", numbers.index(30))

# copy()
copied_list = numbers.copy()
print("Copied List :", copied_list)

# sort()
numbers.sort()
print("After sort() :", numbers)

# reverse()
numbers.reverse()
print("After reverse() :", numbers)

# Membership
print("30 in list :", 30 in numbers)

# Length
print("Length :", len(numbers))

# Clear
numbers.clear()
print("After clear() :", numbers)
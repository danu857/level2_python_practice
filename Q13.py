numbers = {10, 20, 30, 40}

print("Original Set :", numbers)

# add()
numbers.add(50)
print("After add() :", numbers)

# update()
numbers.update([60, 70])
print("After update() :", numbers)

# remove()
numbers.remove(70)
print("After remove() :", numbers)

# discard()
numbers.discard(100)
print("After discard() :", numbers)

# pop()
removed_value = numbers.pop()
print("Removed value :", removed_value)
print("After pop() :", numbers)

# Add values again
numbers.update([70, 80, 90])

# Another set
other_numbers = {30, 40, 80, 100}

print("\nFirst Set :", numbers)
print("Second Set:", other_numbers)

# union()
print("Union :", numbers.union(other_numbers))

# intersection()
print("Intersection :", numbers.intersection(other_numbers))

# difference()
print("Difference :", numbers.difference(other_numbers))

# symmetric difference()
print(
    "Symmetric Difference :",
    numbers.symmetric_difference(other_numbers)
)

# Membership
print("30 in set :", 30 in numbers)

# Length
print("Length :", len(numbers))

# copy()
copied_set = numbers.copy()
print("Copied Set :", copied_set)

# clear()
numbers.clear()
print("After clear() :", numbers)
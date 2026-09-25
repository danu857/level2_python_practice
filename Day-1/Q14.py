student = {
    "name": "Arun",
    "age": 21,
    "mark": 85,
    "department": "AIML"
}

print("Original Dictionary :", student)

# Access value
print("Student Name :", student["name"])

# get()
print("Age :", student.get("age"))

# keys()
print("Keys :", student.keys())

# values()
print("Values :", student.values())

# items()
print("Items :", student.items())

# update()
student.update({"mark": 90})
print("After update() :", student)

# Add new key-value pair
student["city"] = "Coimbatore"
print("After adding city :", student)

# pop()
removed_value = student.pop("city")
print("Removed value :", removed_value)
print("After pop() :", student)

# popitem()
removed_item = student.popitem()
print("Removed item :", removed_item)
print("After popitem() :", student)

# copy()
copied_student = student.copy()
print("Copied Dictionary :", copied_student)

# Membership
print("name in dictionary :", "name" in student)

# Length
print("Length :", len(student))

# Iterate keys
print("\nKeys:")
for key in student:
    print(key)

# Iterate values
print("\nValues:")
for value in student.values():
    print(value)

# Iterate key and value
print("\nKey and Value:")
for key, value in student.items():
    print(key, ":", value)

# clear()
student.clear()
print("\nAfter clear() :", student)
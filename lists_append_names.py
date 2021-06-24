"""
Activity: Loop with a range that asks for names and appends to list names
"""

list_names = []

for name in range(3):
    user_name = input("What is your name")
    list_names.append(user_name)
    print(list_names)

list_name_lower = []
for user in list_names:
    list_name_lower.append(user.lower())

print(list_name_lower)

for person in list_name_lower:
    if len(person)%2 == 0:
        print(f"{person}: Your name has even values")
    else:
        print(f"{person}: Your name does have not even values")


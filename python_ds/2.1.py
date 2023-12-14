# Sample list of records (list of dictionaries)
people = [
    {'name': 'Alice', 'age': 25, 'city': 'San Francisco'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 28, 'city': 'Chicago'},
]

# Adding an index field to each record using enumerate
for index, person in enumerate(people, start=1):
    person['index'] = index

# Displaying the updated list of records
print("People's Information with Index:")
for person in people:
    print(f"Index: {person['index']}, Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

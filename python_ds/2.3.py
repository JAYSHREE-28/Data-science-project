# Sample list of records (list of dictionaries) with categorical field values
people = [
    {'name': 'Alice', 'age': 25, 'city': 'San Francisco', 'gender': 'Female'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles', 'gender': 'Male'},
    {'name': 'Charlie', 'age': 28, 'city': 'Chicago', 'gender': 'Unknown'},
]

# Mapping for re-expressing 'gender' values
gender_mapping = {'Female': 0, 'Male': 1, 'Unknown': 2}

# Re-expressing 'gender' values using the mapping
for person in people:
    person['gender_reexpressed'] = gender_mapping.get(person['gender'], -1)

# Displaying the updated list of records
print("People's Information with Re-expressed Gender:")
for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}, Gender: {person['gender_reexpressed']}")

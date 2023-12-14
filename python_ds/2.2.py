
# Sample list of records (list of dictionaries) with misleading field values
people = [
    {'name': 'Alice', 'age': 25, 'city': 'San Francisco', 'gender': 'F'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles', 'gender': 'M'},
    {'name': 'Charlie', 'age': 28, 'city': 'Chicago', 'gender': 'Unknown'},
]

# Correcting misleading 'gender' values
for person in people:
    if person['gender'] == 'F':
        person['gender'] = 'Female'
    elif person['gender'] == 'M':
        person['gender'] = 'Male'
    else:
        person['gender'] = 'Not Specified'

# Displaying the updated list of records
print("People's Information with Corrected Gender:")
for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}, Gender: {person['gender']}")

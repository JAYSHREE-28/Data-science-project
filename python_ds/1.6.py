# 1.6. Accessing Records and Variables Python
# Creating a dictionary as a record
person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
}

# Accessing and printing values from the dictionary
print("Person's Information:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}\n")

# Creating a list of records (list of dictionaries)
people = [
    {'name': 'Alice', 'age': 25, 'city': 'San Francisco'},
    {'name': 'Bob', 'age': 35, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 28, 'city': 'Chicago'},
]

# Accessing and printing values from the list of records
print("People's Information:")
for p in people:
    print(f"Name: {p['name']}, Age: {p['age']}, City: {p['city']}")

# Creating variables
variable1 = 42
variable2 = 'Hello, World!'
variable3 = True

# Accessing and printing values of variables
print("\nVariables:")
print(f"Variable 1: {variable1}")
print(f"Variable 2: {variable2}")
print(f"Variable 3: {variable3}")

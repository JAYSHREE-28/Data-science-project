# Sample list of records (list of dictionaries) with numeric fields
people = [
    {'name': 'Alice', 'age': 25, 'height': 160, 'weight': 55},
    {'name': 'Bob', 'age': 35, 'height': 175, 'weight': 70},
    {'name': 'Charlie', 'age': 28, 'height': 168, 'weight': 65},
]

# Numeric fields to standardize
numeric_fields = ['age', 'height', 'weight']

# Standardizing numeric fields using z-score normalization
for field in numeric_fields:
    values = [person[field] for person in people]
    mean_value = sum(values) / len(values)
    std_deviation = (sum((x - mean_value) ** 2 for x in values) / len(values)) ** 0.5

    for person in people:
        person[field + '_standardized'] = (person[field] - mean_value) / std_deviation

# Displaying the updated list of records with standardized numeric fields
print("People's Information with Standardized Numeric Fields:")
for person in people:
    print(f"Name: {person['name']}, Age: {person['age_standardized']:.2f}, Height: {person['height_standardized']:.2f}, Weight: {person['weight_standardized']:.2f}")

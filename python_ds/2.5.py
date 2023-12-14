import numpy as np

# Sample list of records (list of dictionaries) with a numeric field
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 28},
    {'name': 'David', 'age': 45},
    {'name': 'Eve', 'age': 22},
]

# Numeric field to check for outliers
numeric_field = 'age'

# Extracting the values of the numeric field
values = [person[numeric_field] for person in people]

# Calculating the interquartile range (IQR)
q1 = np.percentile(values, 25)
q3 = np.percentile(values, 75)
iqr = q3 - q1

# Determining the lower and upper bounds for outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identifying outliers
outliers = [person for person in people if person[numeric_field] < lower_bound or person[numeric_field] > upper_bound]

# Displaying the identified outliers
print("Identified Outliers:")
for outlier in outliers:
    print(f"Name: {outlier['name']}, {numeric_field}: {outlier[numeric_field]}")

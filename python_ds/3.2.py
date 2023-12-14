import pandas as pd

# Sample data for two categorical variables
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Smoker': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes'],
    'Count': [10, 20, 15, 25, 30, 40, 35, 45]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Constructing a contingency table using the crosstab function
contingency_table = pd.crosstab(df['Gender'], df['Smoker'], values=df['Count'], aggfunc='sum', margins=True, margins_name='Total')

# Displaying the contingency table
print("Contingency Table:")
print(contingency_table)

import pandas as pd
import numpy as np

# Sample data for a continuous variable
data = {
    'Scores': [75, 82, 93, 60, 45, 88, 72, 95, 68, 80]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Defining bin edges based on percentiles
bin_edges = [0, 25, 50, 75, 100]

# Performing binning using the cut function
df['Binned_Scores'] = pd.cut(df['Scores'], bins=bin_edges, labels=['Low', 'Medium-Low', 'Medium-High', 'High'])

# Displaying the DataFrame with the binned scores
print("Original DataFrame:")
print(df[['Scores']])

print("\nDataFrame with Binned Scores:")
print(df[['Scores', 'Binned_Scores']])

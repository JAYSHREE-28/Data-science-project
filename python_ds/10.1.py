import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the Boston Housing dataset
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=['target'])

# Split the data into training and testing sets
X_train, X_test, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model to calculate VIF
model = LinearRegression()
model.fit(X_train, y)

# Calculate the Variance Inflation Factor (VIF) for each feature
vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Display the VIF values
print("VIF Values:")
print(vif_data)

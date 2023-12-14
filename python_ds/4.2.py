import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from collections import Counter

# Generating a synthetic imbalanced dataset (you can replace this with your dataset)
X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
                           n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=42)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Displaying the class distribution before balancing
print("Class distribution before balancing:", Counter(y_train))

# Balancing the training set using SMOTE
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Displaying the class distribution after balancing
print("Class distribution after balancing:", Counter(y_resampled))


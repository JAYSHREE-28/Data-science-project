from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Load the Iris dataset as an example
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create a DecisionTreeClassifier
tree_classifier = DecisionTreeClassifier(random_state=42)

# Train the classifier on the training data
tree_classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = tree_classifier.predict(X_test)

# Display the accuracy on the test set
accuracy = (predictions == y_test).mean()
print(f"Accuracy on the test set: {accuracy:.2f}")

# Display the learned decision tree
tree_rules = export_text(tree_classifier, feature_names=iris.feature_names)
print("Learned Decision Tree:")
print(tree_rules)

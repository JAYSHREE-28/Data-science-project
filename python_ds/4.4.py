from C50 import C50
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset as an example
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create a C5.0 decision tree classifier
tree_classifier = C50()

# Train the classifier on the training data
tree_classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = tree_classifier.predict(X_test)

# Display the accuracy on the test set
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy on the test set: {accuracy:.2f}")

# Display the learned decision tree rules
tree_rules = tree_classifier.print_model()
print("Learned Decision Tree:")
print(tree_rules)

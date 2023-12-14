from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve, accuracy_score
import matplotlib.pyplot as plt

# Load the Iris dataset as an example
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create a Random Forest classifier
random_forest_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training data
random_forest_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_scores = random_forest_classifier.predict_proba(X_test)[:, 1]

# Define error costs
false_positive_cost = 1  # Cost of a false positive
false_negative_cost = 5  # Cost of a false negative

# Calculate the cost-sensitive threshold
threshold = (false_positive_cost / false_negative_cost) / (1 + false_positive_cost / false_negative_cost)

# Apply the threshold to make predictions
predictions = (y_scores > threshold).astype(int)

# Evaluate the model with the adjusted threshold
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy with adjusted threshold: {accuracy:.2f}")

# Display classification report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Display confusion matrix
conf_matrix = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:")
print(conf_matrix)

# Calculate ROC-AUC score
roc_auc = roc_auc_score(y_test, y_scores)
print(f"\nROC-AUC Score: {roc_auc:.2f}")

# Plot ROC curve
fpr, tpr, _ = roc_curve(y_test, y_scores)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

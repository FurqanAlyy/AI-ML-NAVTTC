import matplotlib.pyplot as plt
from sklearn.datasets import load_digits, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, classification_report, ConfusionMatrixDisplay,
    RocCurveDisplay, roc_auc_score,
)

digits = load_digits()
train_x, test_x, train_y, test_y = train_test_split(
    digits.data, digits.target, stratify=digits.target,
    test_size=0.25, random_state=52,
)
recognizer = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
recognizer.fit(train_x, train_y)
predicted = recognizer.predict(test_x)
print("Digits accuracy:", accuracy_score(test_y, predicted))
print(classification_report(test_y, predicted, zero_division=0))
ConfusionMatrixDisplay.from_predictions(test_y, predicted)
plt.title("Handwritten digits")
plt.show()
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for position, axis in enumerate(axes):
    axis.imshow(test_x[position].reshape(8, 8), cmap="gray")
    axis.set_title(f"Predicted {predicted[position]}")
    axis.axis("off")
plt.tight_layout()
plt.show()

features, labels = make_classification(
    n_samples=800, n_features=7, n_informative=5, random_state=52
)
train_x, test_x, train_y, test_y = train_test_split(
    features, labels, stratify=labels, test_size=0.25, random_state=52
)
classifier = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
classifier.fit(train_x, train_y)
predicted = classifier.predict(test_x)
probabilities = classifier.predict_proba(test_x)[:, 1]
print(classification_report(test_y, predicted, zero_division=0))
print("ROC AUC:", roc_auc_score(test_y, probabilities))
ConfusionMatrixDisplay.from_predictions(test_y, predicted)
plt.show()
RocCurveDisplay.from_predictions(test_y, probabilities)
plt.show()

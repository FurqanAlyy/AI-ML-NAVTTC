import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

data = load_wine()
train_x, test_x, train_y, test_y = train_test_split(
    data.data, data.target, stratify=data.target, test_size=0.3, random_state=53
)

for title, model in [
    ("Unrestricted", DecisionTreeClassifier(random_state=53)),
    ("Depth limited", DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=53)),
]:
    model.fit(train_x, train_y)
    predicted = model.predict(test_x)
    print(title, "accuracy:", accuracy_score(test_y, predicted))
    print(classification_report(test_y, predicted, target_names=data.target_names, zero_division=0))
    ConfusionMatrixDisplay.from_predictions(test_y, predicted)
    plt.title(title)
    plt.show()
    plt.figure(figsize=(16, 8))
    plot_tree(model, feature_names=data.feature_names, class_names=list(data.target_names), filled=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()

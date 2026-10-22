import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

features, labels = make_moons(n_samples=600, noise=0.2, random_state=54)
train_x, test_x, train_y, test_y = train_test_split(
    features, labels, stratify=labels, test_size=0.25, random_state=54
)

for kernel in ["linear", "poly", "rbf", "sigmoid"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel, C=1.0, gamma="scale"))
    model.fit(train_x, train_y)
    predicted = model.predict(test_x)
    print(kernel, "accuracy:", accuracy_score(test_y, predicted))
    print(classification_report(test_y, predicted, zero_division=0))
    ConfusionMatrixDisplay.from_predictions(test_y, predicted)
    plt.title(f"SVM: {kernel}")
    plt.show()

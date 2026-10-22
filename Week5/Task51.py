import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

rng = np.random.default_rng(51)
hours = rng.uniform(1, 9, 100)
practice = rng.uniform(0, 5, 100)
scores = 8 * hours + 3 * practice + 5 + rng.normal(0, 4, 100)
students = pd.DataFrame({"Hours": hours, "Practice": practice, "Score": scores})
print(students.head())
print(students.shape)
print(students.describe())
print(students.corr())

for columns in [["Hours"], ["Hours", "Practice"]]:
    train_x, test_x, train_y, test_y = train_test_split(
        students[columns], students["Score"], test_size=0.25, random_state=51
    )
    model = LinearRegression().fit(train_x, train_y)
    estimates = model.predict(test_x)
    print("Features:", columns)
    print("Intercept:", model.intercept_)
    print("Coefficients:", dict(zip(columns, model.coef_)))
    print(pd.DataFrame({"Actual": test_y, "Predicted": estimates}).head())
    print("MAE:", mean_absolute_error(test_y, estimates))
    print("RMSE:", np.sqrt(mean_squared_error(test_y, estimates)))
    print("R squared:", r2_score(test_y, estimates))
    if len(columns) == 1:
        grid = pd.DataFrame({"Hours": np.linspace(1, 9, 100)})
        plt.scatter(test_x["Hours"], test_y, label="Test samples")
        plt.plot(grid["Hours"], model.predict(grid), color="red", label="Fit")
        plt.xlabel("Study hours")
        plt.ylabel("Score")
        plt.legend()
        plt.show()
    else:
        example = pd.DataFrame({"Hours": [6.0], "Practice": [2.0]})
        print("Prediction for a new student:", model.predict(example))

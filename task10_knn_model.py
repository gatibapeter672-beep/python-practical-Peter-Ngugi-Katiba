# task10_knn_model.py
"""
KNN Model with Visualization
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd


# LOAD DATASET
iris = load_iris()

X = iris.data
y = iris.target


# DISPLAY DATASET (CLEAN)
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

# Add species names (optional but professional)
df['species'] = df['target'].map({
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
})

print("\n========== IRIS DATASET (FIRST 5 ROWS) ==========\n")
print(df.head().to_string(index=False))

print("\n========== DATASET SUMMARY ==========\n")
print(df.describe().to_string())


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# CREATE & TRAIN MODEL
model = KNeighborsClassifier(n_neighbors=3)

print("\nTraining KNN model...")
model.fit(X_train, y_train)   # 🔥 MODEL TRAINING
print("KNN training complete!")


# PREDICTIONS
predictions = model.predict(X_test)


# EVALUATION
accuracy = accuracy_score(y_test, predictions)
print("\nKNN Accuracy:", accuracy)


# PLOT GRAPH
plt.figure()
plt.title("KNN: Predictions vs Actual")

plt.plot(y_test, label="Actual")
plt.plot(predictions, label="Predicted")

plt.xlabel("Sample Index")
plt.ylabel("Class")
plt.legend()

plt.show()
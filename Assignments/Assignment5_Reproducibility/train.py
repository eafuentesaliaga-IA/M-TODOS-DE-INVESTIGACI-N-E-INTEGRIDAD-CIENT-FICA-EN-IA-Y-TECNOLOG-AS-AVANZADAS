# Paso 2: Entrenamiento inicial del modelo

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset
df = pd.read_csv("breast_cancer.csv")

# Separar características y variable objetivo
X = df.drop(columns=["target"])
y = df["target"]

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Crear un pipeline para evitar data leakage
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, random_state=42))
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Evaluar el modelo
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Entrenamiento completado")
print(f"Accuracy: {accuracy:.4f}")

# Assignment 5 - Reproducibility in Machine Learning
# Entrenamiento reproducible con cinco semillas y MLflow

from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Ubicar los archivos del proyecto
PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "breast_cancer.csv"
RESULTS_FILE = PROJECT_DIR / "results.csv"
MLFLOW_DB = PROJECT_DIR / "mlflow.db"

# 2. Configurar MLflow
mlflow.set_tracking_uri(f"sqlite:///{MLFLOW_DB.as_posix()}")
mlflow.set_experiment("Breast_Cancer_Reproducibility")

# 3. Cargar los datos
df = pd.read_csv(DATA_FILE)

X = df.drop(columns=["target"])
y = df["target"]

# 4. Definir las cinco semillas
seeds = [0, 12, 21, 42, 123]
resultados = []

# 5. Entrenar y evaluar con cada semilla
for seed in seeds:

    np.random.seed(seed)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=seed,
        stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            max_iter=1000,
            random_state=seed
        ))
    ])

    pipeline.fit(X_train, y_train)

    predicciones = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predicciones)

    resultados.append({
        "seed": seed,
        "accuracy": accuracy
    })

    # Registrar la ejecución en MLflow
    with mlflow.start_run(run_name=f"train_seed_{seed}"):

        mlflow.log_param("seed", seed)
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("scaler", "StandardScaler")
        mlflow.log_param("test_size", 0.20)
        mlflow.log_param("max_iter", 1000)

        mlflow.log_metric("accuracy", float(accuracy))

# 6. Calcular las estadísticas
resultados_df = pd.DataFrame(resultados)

media = resultados_df["accuracy"].mean()
desviacion = resultados_df["accuracy"].std()

# 7. Guardar los resultados
resultados_df.to_csv(RESULTS_FILE, index=False)

# 8. Registrar el resumen en MLflow
with mlflow.start_run(run_name="train_summary_5_seeds"):

    mlflow.log_metric("accuracy_mean", float(media))
    mlflow.log_metric("accuracy_std", float(desviacion))
    mlflow.log_param("number_of_seeds", len(seeds))

# 9. Mostrar resultados
print("RESULTADOS DE LAS 5 SEMILLAS")
print(resultados_df.to_string(index=False))

print(f"\nAccuracy promedio: {media:.4f}")
print(f"Desviación estándar: {desviacion:.4f}")

print("\nArchivo results.csv actualizado.")
print("Experimentos registrados en MLflow.")

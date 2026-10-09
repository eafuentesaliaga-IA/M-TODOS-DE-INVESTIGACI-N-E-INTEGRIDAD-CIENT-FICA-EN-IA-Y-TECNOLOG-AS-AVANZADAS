# Assignment 5 - Reproducibility in Machine Learning

## Objetivo

Construir un experimento reproducible de clasificación con
Machine Learning, utilizando múltiples semillas, control de
versiones, prevención de data leakage y registro en MLflow.

## Dataset

- Nombre: Breast Cancer Wisconsin Diagnostic
- Fuente: Dataset disponible en scikit-learn
- Archivo: breast_cancer.csv
- Registros: 569
- Variables predictoras: 30
- Variable objetivo: target
- SHA-256: 75a1d74a59df9cb0a78ecc0a36085bf8a85239557f178d3b8d758e88b26416e1

## Modelo

- Algoritmo: LogisticRegression
- Preprocesamiento: StandardScaler
- División: 80% entrenamiento y 20% prueba
- División estratificada: Sí
- Semillas: 0, 12, 21, 42, 123
- max_iter: 1000

El preprocesamiento se realiza dentro de un Pipeline.
De esta forma, StandardScaler se ajusta solamente con
los datos de entrenamiento para evitar data leakage.

## Resultados

Se realizaron cinco ejecuciones con distintas semillas.

- Accuracy promedio: aproximadamente 0.9842 (98.42%)
- Desviación estándar: aproximadamente 0.0073

Los resultados individuales están en results.csv.

## Entorno

- Python: 3.13.16
- Librerías: consultar requirements.txt
- Registro de experimentos: MLflow

## Cómo reproducir el experimento

1. Descargar los archivos de este proyecto.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Instalar las dependencias:

    pip install -r requirements.txt

4. Ejecutar el entrenamiento:

    python train.py

5. Revisar los resultados generados en results.csv.
6. Consultar los experimentos registrados en mlflow.db.

## Archivos principales

- breast_cancer.csv: dataset utilizado.
- train.py: entrenamiento con cinco semillas y MLflow.
- results.csv: resultados de las cinco ejecuciones.
- mlflow.db: historial de experimentos registrado.
- requirements.txt: versiones exactas de las librerías.
- README.md: documentación del proyecto.
- Notebook .ipynb: desarrollo paso a paso en Colab.

## Reproducibilidad

El proyecto utiliza semillas controladas, un Pipeline
para evitar data leakage, resultados estadísticos,
registro de ejecuciones y versiones de librerías.

Este experimento tiene fines académicos y no constituye
una herramienta de diagnóstico médico.

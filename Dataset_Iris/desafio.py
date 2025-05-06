# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn import datasets

# Carregando o dataset Iris
iris = datasets.load_iris()

# Extraindo os dados e criando um DataFrame
X = iris.data  # Características (features)
y = iris.target  # Classes (target)
feature_names = iris.feature_names
target_names = iris.target_names

# Criando um DataFrame para melhor visualização
df = pd.DataFrame(X, columns=feature_names)
df['species'] = [target_names[i] for i in y]

# Visualizando as primeiras linhas do dataset
print("Primeiras linhas do dataset Iris:")
print(df.head())

# Ver algumas estatísticas básicas (mínimo, máximo, média, etc.)
print("\nEstatísticas básicas do dataset:")
print(df.describe())

# Ver quantas amostras tem de cada tipo de flor
print("\nQuantas amostras tem de cada espécie:")
print(df['species'].value_counts())

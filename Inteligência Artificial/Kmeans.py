import numpy as np

from sklearn.datasets import make_blobs

import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import dendrogram, linkage

from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=100, n_features=2, random_state=0)

plt.scatter(X[:, 0], X[:, 1])
plt.title('Conjunto de Dados Original')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

Z = linkage(X, method='complete')

plt.figure(figsize=(10, 7))

plt.title('Dendrograma de Clustering Hierárquico - Análise da Estrutura dos Clusters')
dendrogram(Z)
plt.xlabel('Amostras')
plt.ylabel('Distância Euclidiana')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0)

kmeans.fit(X)


plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X', label='Centróides')
plt.title('Clusters Encontrados pelo K-means com Centróides - Visualização dos Grupos e seus Centros')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
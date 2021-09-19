import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np

def load_data():
    x, y = make_blobs(n_samples=1000, centers=10, n_features=2, random_state=101)
    plt.scatter(x[:,0], x[:,1], c=y)
    plt.show()
    return x, y

def set_k(x, y):
    kmeans = KMeans(n_clusters=10)
    kmeans.fit(x)

    y_test = kmeans.predict(x)
    cents = kmeans.cluster_centers_

    plt.scatter(x[:,0], x[:,1], c=y_test)
    plt.scatter(cents[:,0], cents[:,1], marker='o', c='r')
    plt.show()

def elbow(x, y):
    distorsions = []
    for k in range(2,20):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(x)
        distorsions.append(kmeans.inertia_)

    fig = plt.figure(figsize=(15,5))
    plt.plot(range(2,20), distorsions)
    plt.grid(True)
    plt.title('elbow curve')
    plt.show()

x, y = load_data()
set_k(x,y)
elbow(x,y)

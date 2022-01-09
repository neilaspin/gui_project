# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
#     x = Complex(3.0, -4.5)
# !/usr/bin/env python
class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name


def createClusteredData(N, k):
    random.seed(10)
    pointsForCluster = float(N) / k
    x = []
    for i in range(k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentrold = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 1000.00), np.random.normal(ageCentroid, 2.0)])
        X = np.array(X)
        return X
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    from sklearn.preprocesing import scale
    data = createClusteredData(100, 5)
    model = KMeans(n_clusters=5)
    model = model.fit(scale(data))
    print model.labels_

    plt.figure(figsize=(8, 6))
    plt.scatter(data[:,0], data[:,1], c=model.label.astype(np.float))
    plt.show()

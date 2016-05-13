import math
from sklearn.cluster import AffinityPropagation
import numpy as np


class Cluster(object):
    X = []
    labels = 0
    n_clusters_ = 0
    cluster_centers_indices = 0
    Last_Transaction_Distance = 0
    Maximum_Distance = 0
    Last_Transaction_Cluster_Centroid = 0


    def __init__(self, transaction):
        self.X = (transaction)
        self.npArray=np.asarray(transaction, dtype=float)

    def makeCluster(self):
        af = AffinityPropagation(preference=-50).fit(self.X)
        self.cluster_centers_indices = af.cluster_centers_indices_
        self.labels = af.labels_
        self.n_clusters_ = len(self.cluster_centers_indices)

    def finder(self, labels=None, pointIndex=None):
        return labels[pointIndex]

    def setDistances(self,Last_Transaction_Distance, Maximum_Distance, Last_Transaction_Cluster_Centroid):
        self.Last_Transaction_Distance, self.Maximum_Distance, self.Last_Transaction_Cluster_Centroid =float (Last_Transaction_Distance), float(Maximum_Distance), Last_Transaction_Cluster_Centroid



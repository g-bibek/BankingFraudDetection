import math
import matplotlib.pyplot as plot
from itertools import cycle
class Plot(object):

    def __init__(self):
        self.plt=plot
        self.n=1
        self.title=""
        
    def plotClusters(self, n_clusters_, labels, X, cluster_belong, cluster_centers_indices):
        #self.plt.close('all')
        self.plt.figure(self.n, figsize=(5,5))
        self.plt.clf()
        Maximum_Distance = 0
        Last_Transaction_Distance = 0
        Last_Transaction_Cluster_Centroid = 0
        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            class_members = labels == k
            cluster_center = X[cluster_centers_indices[k]]
            self.plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
            if k == cluster_belong:
                Last_Transaction_Cluster_Centroid = cluster_center
                Last_Transaction_Cluster=cluster_belong
                self.plt.plot()
                Last_Transaction_Distance = self.calculateDistance(cluster_center[0], cluster_center[1], X[-1][0], X[-1][1])
                Maximum_Distance = self.maxDist(X[class_members], cluster_center)
                #self.plt.Circle((cluster_center,cluster_center[1]), radius=Maximum_Distance, color='g', fill=False)
                self.plt.plot(X[class_members, 0][-1], X[class_members, 1][-1], 'r' + 'x', markersize=20)
            self.plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=10)
            for x in X[class_members]:
                self.plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

        self.plt.title(self.title)
        self.n+=1
        return Last_Transaction_Distance, Maximum_Distance, Last_Transaction_Cluster_Centroid

    def calculateDistance(self,x1,y1,x2,y2):
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist


    def maxDist(self,points=None, center=None):
        maxD = 0
        for eachPoint in points:
            dist = self.calculateDistance(center[0], center[1], eachPoint[0], eachPoint[1])
            if dist > maxD:
                maxD = dist
        return maxD
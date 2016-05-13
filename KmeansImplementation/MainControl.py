#############################
# Bibek Gautam              #
# K-Means Clustering        #
# CMPS:470                  #
############################

# Upper bound of max iteration taken from http://cseweb.ucsd.edu/~avattani/papers/kmeans.pdf
# http://www.saedsayad.com/clustering_kmeans.htm

from itertools import islice

import numpy as Numpy
from PreprocessDataForClustering import GetData

from KmeansImplementation.KMeansCluster import Cluster as ClusterClass


# Kmeans algorithm
def RunKMeansAlgorithm(dataSet, NumExamples,NumClusters, max_iteration):
    data_Set=dataSet
    Num_Examples= NumExamples
    Num_Clusters=NumClusters
    maxiteration=max_iteration
    initialPoint = list(islice(data_Set.keys(),Num_Clusters))
    clusters = [ClusterClass([p]) for p in initialPoint]# initialize the clusters
    check=True
    maxiterationcheck = 0
    while check == True:
        for cluster in clusters:
                cluster.reset()
        for attributeName in data_Set:
            min = clusters[0].getdistancefromcentroid((attributeName))
            belongsToCluster = clusters[0]
            for cluster in clusters[1:]:
                dist_Centroid = cluster.getdistancefromcentroid((attributeName))# get distance from current centroid
                if(dist_Centroid < min):# assign the data to nearest cluster
                    belongsToCluster = cluster
                    min = dist_Centroid
            belongsToCluster.addname((attributeName))
        unchangedClusters = 0
        for cluster in clusters:#check centroid position with old one
           shift = cluster.update()
           if shift <= .0001:
               unchangedClusters += 1
        if(unchangedClusters==Num_Clusters):#check centroid position with old one
            check=False
        maxiterationcheck+=1
        if( maxiterationcheck >= maxiteration):# check max iteration
            check=False
        return clusters, maxiterationcheck



#read the input file
test=GetData()
data_Set, numExamples, numClusters, maxIter=test.input()
ClusterClass.data_set = data_Set
clusters, maxiterationcheck=RunKMeansAlgorithm(data_Set,numExamples,numClusters,maxIter)


#print the result and write it to out.txt
test.output(clusters, maxiterationcheck)

def getCluster():
    for cluster in clusters:
        for attributeName in cluster.attributeNames:
         if int(attributeName)== int(numExamples):
            print (numExamples)
            distance=Numpy.linalg.norm(Numpy.array(cluster.centroid, dtype=float) - Numpy.array(data_Set[attributeName], dtype=float))
            return (cluster), data_Set[attributeName],distance

cluster, currentAttribute,distance=getCluster()

maxs=0;
for attributeName in cluster.attributeNames:
    if int(attributeName) != int(numExamples):
        currentDistance=Numpy.linalg.norm(Numpy.array(cluster.centroid, dtype=float) - Numpy.array(data_Set[attributeName], dtype=float))
        if(currentDistance>=maxs):
            maxs=currentDistance
cluster.max_Distance_LastPointClusterCentroid=maxs
cluster.distanceofRequiredPoint=distance
cluster.coordinatesOfRequiredPoint=data_Set[numExamples]
print (cluster)
print (currentAttribute)
print (distance)
print (maxs)

import numpy as Numpy
import math


class Cluster(object):
    data_set = {}
    max_Distance_LastPointClusterCentroid=0
    distanceofRequiredPoint=0
    coordinatesOfRequiredPoint=0

    def __init__(self, attributenames):
        self.attributeNames=attributenames
        self.attributes=[self.data_set.get(p) for p in attributenames]
        self.centroid=self.attributes[0]

    def calculatecentroid(self):
        numExamples = len(self.attributes)
        unzipped = zip(*self.attributes)
        centroid_coords = [math.fsum(dList) / numExamples for dList in unzipped]
        return centroid_coords

    def reset(self):
        self.attributeNames = []
        self.attributes =[]

    def addname(self, attributename):
        self.attributeNames.append(attributename)

    def update(self):
        old_centroid = self.centroid
        self.attributes=[self.data_set.get(p) for p in self.attributeNames]
        self.centroid = self.calculatecentroid()
        return Numpy.linalg.norm(Numpy.array(old_centroid, dtype=float)-Numpy.array(self.centroid, dtype=float))

    def getdistancefromcentroid(self, attributename):# euclidean distance using numpy
        return Numpy.linalg.norm(Numpy.array(self.centroid, dtype=float) - Numpy.array(self.data_set.get(attributename),dtype=float))



from Cluster import Cluster as cluster
from Plot import Plot as plot
import  numpy as np
from DatabaseOperation import Database as database
import datetime

#print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

p1 = plot()

def Cluster_Plot_Result(CurrentCluster):

    # n_clusters_, labels, X, cluster_belong, cluster_centers_indices
    cluster_belong = CurrentCluster.finder(CurrentCluster.labels, len(CurrentCluster.X)-1)
    Last_Transaction_Distance, Maximum_Distance, Last_Transaction_Cluster_Centroid = p1.plotClusters(CurrentCluster.n_clusters_, CurrentCluster.labels, CurrentCluster.X, cluster_belong, CurrentCluster.cluster_centers_indices)
    CurrentCluster.setDistances(Last_Transaction_Distance, Maximum_Distance, Last_Transaction_Cluster_Centroid)
    print(CurrentCluster.Last_Transaction_Distance)

def createClusters(data, title):
    p1.title=title
    temp_Cluster=cluster(np.asarray(data, dtype=float))
    temp_Cluster.makeCluster()
    Cluster_Plot_Result(temp_Cluster)
    return temp_Cluster

def calculateError(cluster):
    if int( cluster.Maximum_Distance) == 0 & int (cluster.Last_Transaction_Distance == 0.0):
        error = "F"
    elif cluster.Maximum_Distance > cluster.Last_Transaction_Distance:
        error = "L"
    elif cluster.Maximum_Distance < cluster.Last_Transaction_Distance:
        error = "H"
    elif cluster.Maximum_Distance == cluster.Last_Transaction_Distance:
        error = "H"
    return error

databaseInstance=database()
#databaseInstance.runQuery()
#databaseInstance.deleteTableData()
#databaseInstance.insertData()

#Cluster_Plot_Result(np.asarray(Amount_Type_Data, dtype=float))
Amount_Category_Data=databaseInstance.get_Data_By("amount", "category")
Amount_Type_Data=databaseInstance.get_Data_By("amount", "type")
Amount_Zipcode_Data=databaseInstance.get_Data_By("amount", "zipcode")
Id_Category_Data=databaseInstance.get_Data_By("rowid", "Category")


#data=np.asarray(Amount_Category_Data, dtype=float)
c1 = createClusters(Amount_Category_Data, "Amount - Category")
c2 = createClusters(Amount_Type_Data, "Amount - Transaction Type")
c3 = createClusters(Amount_Zipcode_Data, "Amount - Zipcode Graph")
c4 = createClusters(Id_Category_Data,"Transaction - Category")



print ("Personalized Cluster Result =>  {}, {}, {}, {}".format(calculateError(c1),calculateError(c2), calculateError(c3), calculateError(c4)))
p1.plt.show()
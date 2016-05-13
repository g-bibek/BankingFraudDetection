
import sqlite3 as sql

from sklearn.datasets.samples_generator import make_blobs
class GetData(object):
    Num_Examples=0
    Num_Attributes=2
    Num_Clusters=5
    Data_Set = {}


    def __init__(self):
        pass
    #data_set, Num_Examples, Num_Attributes, Num_Clusters, maxiteration

    tableName ="Transaction"
    Num_ExamplesQuery=' SELECT max(rowid) FROM  "%s"' %tableName
    AmountAndTypeQuery=' SELECT rowid,Amount, Type  FROM "%s"' %tableName
    deleteQuery=' DELETE FROM "%s" where Amount = 0' %tableName
    selectAmountQuery=' SELECT AMOUNT FROM "%s"' %tableName
    conn = sql.connect('History')
    #print("connection successful")
    c = conn.cursor()

    def input(self):
        amount=list()

        Num_Examples=self.c.execute(self.Num_ExamplesQuery)
        maxiteration = self.Num_Clusters * self.Num_Attributes
        maxiteration = self.Num_Attributes ** maxiteration
        for data in Num_Examples:
            self.Num_Examples=data[0]
        print (self.Num_Examples)


        for row in (self.c.execute(self.AmountAndTypeQuery)):
            amount.append((row))

        for row in amount:
            #print(row[0])
            self.Data_Set[row[0]]= row[1],row[2]
            print("RowId: {0}     Data: {1} ".format(row[0],self.Data_Set[row[0]]))
        return self.Data_Set, self.Num_Examples,self.Num_Clusters, maxiteration


    def output(self, clusters, totaliteration):
        x = 1
        with open("out.txt", "w+") as f:
            f.write("File Name:  {0}\n".format("test"))
            f.write(("Total Iteration: {0}\n\n".format(totaliteration)))
            f.write(
                "================================================================================================================\n")
            for cluster in clusters:
                f.write("CLUSTER NUMBER:{0}\n".format(x))
                f.write("TOTAL MEMBERS:{0}\n".format(len(cluster.attributeNames)))
                f.write("Attribute NAMES: {0}\n".format(cluster.attributeNames))
                f.write("ATTRIBUTE CORDINATES:{0}\n ".format(cluster.attributes))
                f.write("CENTROID COORDINATES: {0}\n".format(cluster.centroid))
                f.write(
                    "================================================================================================================\n")
                #print
               # "================================================================================================================"
              #  print("Filename: {0}\n Max iteration:{1}\n".format("test", totaliteration))
               # print
               # "CLUSTER NUMBER:\t\t\t", x
               # print
               # "TOTAL MEMBERS= \t\t\t", len(cluster.attributeNames)
               # print
               # "ATTRIBUTE NAMES:\t  ", cluster.attributeNames
               # print
               # "CORDINATES_ATTRIBUTE: ", cluster.attributes
               # print
               # "COORDINATES_CENTROID: ", cluster.centroid
               # print
                ""
                x += 1
      #  print
      #  "================================================================================================================"

from random import  randint as ran
import sqlite3 as sql
from datetime import datetime as dt
from sklearn import cluster,datasets
import matplotlib.pyplot as plt
import numpy
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.datasets.samples_generator import make_blobs


tablep ="Transaction"
countQuery=' SELECT rowid, * FROM "%s"' %tablep
deleteQuery=' DELETE FROM "%s" where Amount = 0' %tablep
selectAmountQuery=' SELECT AMOUNT FROM "%s"' %tablep
conn = sql.connect('History')
print("connection successful")
c = conn.cursor()


#c.execute(countQuery)
users = list()
for x in range(0, 10, 1):
    users.append((0, ran(210, 240), "", ran(70401, 70406), "", ""))
#c.executemany('INSERT INTO "%s" (Type, Amount, Category,zipcode, date,time) VALUES(?,?,?,?,?,?)'%tablep, users)
conn.commit()

def insert(type, amount, category, zipcode, date, time):
    c.execute('INSERT INTO "Transaction" (Type, Amount, Category,zipcode, date,time) VALUES(?,?,?,?,?,?)', type, amount, category, zipcode, date, time)



amount=list()
for row in c.execute(countQuery):
    print (row),
    amount.append(float(row[0]))


X=StandardScaler().fit_transform(amount)
q = DBSCAN(eps=30, min_samples=5).fit(X,y=None,sample_weight=None)
#print (db.fit_predict(amount))
print (q.labels_)


##############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

X = StandardScaler().fit_transform(X)

##############################################################################


'''k_means= cluster.KMeans(n_clusters=9)
k_means.fit(X_iris)
print(k_means.labels_[::10])
print(y_iris[::10])
plt.plot(k_means.n_clusters)'''

'''

# type, amount, category, datetime, zipcode
_'''





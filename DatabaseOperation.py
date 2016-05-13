import sqlite3 as sql
from random import  randint as ran
from random import randrange
from datetime import timedelta
import  datetime






from sklearn.datasets.samples_generator import make_blobs
class Database(object):
    Num_Examples=0
    Num_Attributes=2
    Num_Clusters=5
    Data_Set = {}

    def random_date(self):
        """
        This function will return a random datetime between two datetime
        objects.
        """

        start = datetime.datetime.strptime('1/1/2014 1:30 PM', '%m/%d/%Y %I:%M %p')
        end = datetime.datetime.strptime('1/1/2016 4:50 AM', '%m/%d/%Y %I:%M %p')
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    ' SELECT max(rowid) FROM  "%s"' % "Transaction"
    def __init__(self):
        self.tableName ="Transaction"
        self.Num_ExamplesQuery=' SELECT max(rowid) FROM  "%s"' %self.tableName
        self.AmountAndZipQuery=' SELECT Amount, zipcode  FROM "%s"' %self.tableName
        self.AmountAndTypeQuery=' SELECT Amount, type  FROM "%s"' %self.tableName
        self.AmountAndCategoryQuery=' SELECT %s, category  FROM "%s"' %("amount",self.tableName)
        self.deleteQuery=' DELETE FROM "%s" ' %self.tableName
        self.selectAmountQuery=' SELECT AMOUNT FROM "%s"' %self.tableName
        self.conn = sql.connect('History')
        #print("connection successful")
        self.c = self.conn.cursor()


    def get_Data_By(self, column1, column2):
        query= ' SELECT %s, %s  FROM "%s"' %(column1,column2,self.tableName)
        amount=list()
        for row in (self.c.execute(query)):
            amount.append((row))
        return amount

    def insertData(self):
        users = list()
        for x in range(0, 50, 1):
            users.append((ran(1,5), ran(40, 60), ran(5,10), ran(70401, 70406), self.random_date()))
            users.append((ran(1,5), ran(0, 20), ran(5,10), ran(70406, 70410), self.random_date()))
            users.append((ran(1,5), ran(80, 90), ran(5,10), ran(70410, 70415), self.random_date()))


        self.c.executemany('INSERT INTO "%s" (Type, Amount, Category,zipcode, datetime) VALUES(?,?,?,?, ?)'%self.tableName, users)
        self.conn.commit()
        return "success"

    def deleteTableData(self):
        self.c.execute(self.deleteQuery)

    def setTable(self,tableName):
        self.tableName=tableName

    def runQuery(self,query):
        self.c.execute(query)

    '''def getAmountCategory(self):
        amount = list()
        for row in (self.c.execute(self.AmountAndCategoryQuery)):
            amount.append((row))
        return amount

    def getAmountType(self):
        amount = list()
        for row in (self.c.execute(self.AmountAndTypeQuery)):
            amount.append((row))
        return amount'''

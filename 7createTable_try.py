#by Hariom Yadav
#Date : 17th Feb '16


import sqlite3

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

def createDB():
    c.execute("CREATE TABLE wordVals (word TEXT, value REAL)")
createDB()

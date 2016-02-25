import sqlite3
import time

conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str
c = conn.cursor()

positive_word = []
negative_word = []

sql = "SELECT * from wordVals WHERE value = ?"

def loadWordIntoList():
    for posRow in c.execute(sql,[(+1)]):
        positive_word.append(posRow[0])
    print "all positive word loaded into list"

    for negRow in c.execute(sql,[(-1)]):
        negative_word.append(negRow[0])
    print "all negative word loaded into list"

loadWordIntoList()
print "print negative word from db	:	", negative_word
print "print positive word from db	:	", positive_word

#access table data that we are saved in last program 
import nltk
import re
import time
import sqlite3
import datetime

conn = sqlite3.connect('knowledgeBase.db')#create db if not avail
conn.text_factory = str # this line makes remove 'u' from u'Food' and makes as 'Food'
c = conn.cursor()

wordUsed = 'Food'
sql = "SELECT * FROM knowledgeBase WHERE namedEntity = ?"

for row in c.execute(sql,[(wordUsed)]):
    print row

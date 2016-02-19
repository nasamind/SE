
#connecting or creating to dababase, && saving data into table knowledgeBase.. here in this program db name and table name are same..it may be diff also

import nltk
import re
import time
import sqlite3
import datetime

conn = sqlite3.connect('knowledgeBase.db')#create db if not avail
c = conn.cursor()

sampleArray = ['Food qualtity is average.','Staff member of this Hotel is nice']

def processLanguage():
    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print "word		:	",item
            print "tagged	:	",tagged
            nameEnt = nltk.ne_chunk(tagged,binary=True)#if binary is not true then it will show GPE entity
            
            nameEnt.draw()#drawing name entity
            entities = re.findall(r'NE\s(.*?)/',str(nameEnt))#extracting name entity from nameEnt
            print "name entity	:	",entities#printing name entity

            # ('nice', 'JJ')
            descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))# extracting nice from above tagged version of token i.e. input : ('nice', 'JJ') output : nice , or ('worst', 'JJS') output : worst
            print "descritive	:	",descriptives

            currentTime = time.time()
            dateStamp = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H:%M:%S')
            namedEntity = entities[0]
            relatedWord = descriptives[0]
            c.execute("INSERT INTO knowledgeBase (unix, datestamp, namedEntity, relatedWord) VALUES (?,?,?,?)",(currentTime, dateStamp,namedEntity, relatedWord))#saving data into table knowledgeBase
            conn.commit()

            time.sleep(1)

    except Exception as e:
        print str(e)
processLanguage()

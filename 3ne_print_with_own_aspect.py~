#by Hariom Yadav
#Date : 25th Feb '16

#name entity recognition

import nltk
import re
import time

sampleArray = ["Food and staff member Of this hotel is nice","Every day was a treat to our senses","No surprise that most guests we met there, were repeat visitors"]#here we are talking about Food and Staff

def processLanguage():

    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print "tagged	:	",tagged

            propernouns = [word for word,pos in tagged if pos == 'NNP']#extracting NNP
            nouns = [word for word,pos in tagged if pos == 'NN']#extracting NN
  
            nameEnt = nltk.ne_chunk(tagged,binary=True)#if binary is not true then it will show GPE entity            
            #nameEnt.draw()#drawing name entity
            entities = re.findall(r'NE\s(.*?)/',str(nameEnt))#extracting name entity from nameEnt

            print "my name entity list	:	",propernouns, nouns
            print "nltk name entities	:	",entities#printing name entity

            time.sleep(1)
    except Exception as e:
        print str(e)
processLanguage()

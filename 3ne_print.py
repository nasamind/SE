#name entity recognition
# who we are taking about
#printing name entity
import nltk
import re
import time

sampleArray = ['Food and Staff member of this Hotel is nice']#here we are talking about Food and Staff

def processLanguage():

    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print tagged
            nameEnt = nltk.ne_chunk(tagged,binary=True)#if binary is not true then it will show GPE entity
            
            nameEnt.draw()#drawing name entity
            entities = re.findall(r'NE\s(.*?)/',str(nameEnt))#extracting name entity from nameEnt
            print entities#printing name entity
            time.sleep(1)

    except Exception as e:
        print str(e)
processLanguage()

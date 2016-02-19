#name entity recognition
# who we are taking about
import nltk
import re
import time

sampleArray = ['the incredibly intimidating NLP scares people away who are sissies.']#here we are talking about NLP

def processLanguage():

    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print tagged
            nameEnt = nltk.ne_chunk(tagged,binary=True)#if binary is not true then it will show GPE entity
            
            nameEnt.draw()

            time.sleep(1)

    except Exception as e:
        print str(e)
processLanguage()

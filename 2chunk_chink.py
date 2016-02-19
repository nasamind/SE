#by Hariom Yadav
#Date : 15th Feb '16


import nltk
import re
import time
#chunk : {}
#chink : }{

sampleArray = ['the incredibly intimidating NLP scares people away who are sissies.']

def processLanguage():

    try:
        for item in sampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            print tagged
            chunkGram = r"""
Chunk: 
{<.*>}
}<RB|NNS>{
"""
#in chink we are emoving RB:adverb or NNS:noun plural

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print chunked
            chunked.draw()
            time.sleep(1)

    except Exception as e:
        print str(e)


processLanguage()

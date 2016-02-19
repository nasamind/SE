#by Hariom Yadav
#Date : 15th Feb '16


#chunking NN from input
import nltk
import time
import re

arry = ['NLP is good', 'Food and staff both are nice']

def processLang():
    try:
        for item in arry:
            tokenized = nltk.word_tokenize(item) # output : ['Hotel', 'is', 'good']
            print "tokenized	:	",tokenized

            tagged = nltk.pos_tag(tokenized)# output : [('Hotel', 'NN'), ('is', 'VBZ'), ('good', 'JJ')]
            print "tagged	:	",tagged

            chunkGram = r"""Chunk:{<NN\w?>}""" #chunking NN or NN with any character like NNS
            print "chunkgram	:	",chunkGram # output : Chunk:{<NNP>}
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked  = chunkParser.parse(tagged)
            print "chunked	:	",chunked
            chunked.draw()
            
    except Exception as e:
        print str(e)

processLang()

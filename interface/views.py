from django.shortcuts import render
from django.http import HttpResponse
import nltk
import os
import nltk.corpus
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import blankline_tokenize
from nltk import bigrams,ngrams,trigrams
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
punctuation = re.compile(r'[-.?!,:;()|0-9]')
from nltk import ne_chunk
from textblob import TextBlob

 
# we can pull data from DB.
# we can Transform data or send emails etc.
 
def say_hello(request):
        data = request.POST.get('input')
        if(request.GET):
                data ="None"
        # print(data)
        if bool(data):
                data = data
        else:	
                data = "None"
        
        
        result = TextBlob(data)
        data_token = word_tokenize(data)
        post_punctuation = []
        for words in data_token:
                word=punctuation.sub("",words)
                if len(word)>0:
                        post_punctuation.append(word)
        
        
        Ne_token = word_tokenize(data)
        NE_TAGS = nltk.pos_tag(Ne_token)
        NE_NER = ne_chunk(NE_TAGS)
        return render(request,'index.html',{'Data':data,'Result':result.sentiment,'data_tokens':post_punctuation,'Subject_Detection':NE_NER,'POS':NE_TAGS})        
	
 
         
       
        # return render(request,'index.html',{'Data':data})
        # return render(request,'index.html',{'Data':data,'Result':result.sentiment,'data_tokens':data_token})
        # return HttpResponse('Hello World')

# to map the url http://127.0.0.1:8000/interface/hello we will return the 'Hello World' as an output
# we will use a urls.py file to perform mapping of url in this directory and also in the root urls.py directory

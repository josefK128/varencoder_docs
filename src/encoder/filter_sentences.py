# filter_sentences.py
# obtains the docs dictionary from corpus2sentences
# for each sentence in docs filters out punctuation, stopwords
# tokenizes each sentence to a list of its words
# stems the words and re-joins the word-lists to sentence-strings in _docs
# returns the modified _docs dictionary (leading underscore => preprocessed) 


import string
#import re
#import unicodedata
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
#import os,sys,inspect
#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir)       #include parent dir in sys.path - unneeded 
import corpus2sentences as c2s


def action(diagnostics=False):
    if diagnostics == True:
        docs = c2s.action(True)
    else:
        docs = c2s.action()
 
    print('\n\n+++++++++++ filter_sentences +++++++++++++++++++++')
    print('number of paragraphs = ' + str(len(docs.values())))


    #dictionary for filtered sentences
    _docs = {}


    #[1] filter out punctuation
    #NOTE: regular expression - works but SLOWER!
#    print('punctuation removed')
#    for paragraph in docs.values():
#        for sentence in paragraph:
#            sentence = re.sub(r'[^\w\s]','',sentence)
#            if diagnostics == True:
#                print('\n' + sentence)
 
    #NOTE: string.punctuation for punctuation in sentence.translate WORKS! 
    punctuation = str.maketrans({key: None for key in string.punctuation})
    for k,paragraph in docs.items():
        paragraph = [sentence.translate(punctuation) for sentence in paragraph]
        _docs[k] = paragraph
        if diagnostics == True:
            print('\n')
            print('_docs[' + str(k) + ']:')
            print(_docs[k])

    print('punctuation removed')


    #[2]tokenize each sentence to a temporary word list for [3],[4]
    #load stopwords
    print('sentences tokenized')
    print('stopwords removed')
    print('words stemmed')
    print('_docs is dictionary of paragraphs - values are arrays of tokens')
    stop_words = stopwords.words('english')
    for k,paragraph in _docs.items():
        a = []
        for sentence in paragraph:
            sentence += sentence.lower()          #lower case
            wordlist = word_tokenize(sentence)
 
            #[3]filter out stopwords
            wordlist = [word for word in wordlist if word not in stop_words]
            if diagnostics == True:
                print('\n' + str(wordlist))
 
            #[4]stem each word in each word list
            porter = PorterStemmer()
            wordlist = [porter.stem(word) for word in wordlist]
            a.append(wordlist)
            if diagnostics == True:
                print('\n' + str(wordlist))            
            
        #store in _docs
        _docs[k] = a
        if diagnostics == True:
            print('\n')
            print('_docs[' + str(k) + ']:')
            print(_docs[k])


    #[5]re-join word lists to dictionary _docs {doc_index:[doc_sentences]}
    for k,v in _docs.items():
        a = []
        for wl in v:
            a.append(' '.join(wl))
        _docs[k] = a
        if diagnostics == True:
            print('\n')
            print('_docs[' + str(k) + ']:')
            print(_docs[k])
    
    print('wordlist arrays of tokens re-joined into sentences')
    if diagnostics == True:
        print('\n')
        print('_docs:')
        print(_docs)
 

    return _docs, docs
   

if __name__ == "__main__": 
    print("filter_sentences module running in diagnostics mode as __main__")
    action(True)
else:
    print("filter_sentences module imported")

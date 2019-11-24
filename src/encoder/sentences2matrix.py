# sentences2matrix.py
# obtains the _docs dictionary and original docs dictionary from 
# filter_sentences.py
# build a document-term matrix A where documents are the sentences in the corpus
# and terms are the Tf-Idf (term-frequency-inverse document frequency) of
# all stemmed and filtered words in the sentences.
# returns A and the original docs dictionary to encoder.py 


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import filter_sentences as fs


def action(diagnostics=False):
    if diagnostics == True:
        _docs, docs = fs.action(True)
    else:
        _docs, docs = fs.action()

    print('\n\n+++++++++++ sentences2matrix +++++++++++++++++++++')
    print('_docs:')
    print(_docs)

    #create dictionary of all sentences in all paragraphs for all _docs
    sentences = {}
    index = 0
    for paragraph in _docs.values():
        for sentence in paragraph:
            sentences[str(index)] = [sentence]
            index += 1
 
    if diagnostics == True:
        print('\n\nsentences:')
        print(sentences)


    print('\n\n')
    words = []
    for k,v in sentences.items():
        #next line used if paragraphs are arrays of arrays of word-tokens
        #for w in v:
        #these two lines used if paragraphs are arrays of sentence-strings
        a = v[0].split(' ')
        for w in a:
            if not w in words:
                words.append(w) 
        print('sentence ' + str(k) + ' is:')
        print(v[0])
        print('\n')

    if diagnostics == True:
        index = 0
        for word in words:
            print('word[' + str(index) + '] = ' + str(words[index]))
            index += 1


    #report number of words
    print('\n\n`words.length = ' + str(len(words)))


    #create dataframe
    df1 = pd.DataFrame(sentences)
    if diagnostics == True:
        print('\n\n df1:')
        print(df1)
     
    # Initialize TfidfVectorizer - create sentence-token matrix
    vectorizer = TfidfVectorizer()
    doc_vec = vectorizer.fit_transform(df1.iloc[0])
    df2 = pd.DataFrame(doc_vec.toarray().transpose(),
            index=vectorizer.get_feature_names())
    df2.columns = df1.columns

    if diagnostics == True:
        print('\n\n df2:')
        print(df2)


    #create matrix A, token-sentence matrix
    A = df2.to_numpy()
    print('\n\nA.transpose() is the desired sentence-token matrix'); 
    print('A is thus a token-sentence matrix - better for viewing.')
    print('matrix2d.shape is given by (rows, columns)')
    print('A.transpose().shape is ' + str(A.transpose().shape) + ':\n');
    print('A.shape is ' + str(A.shape) + ':\n');
    print(A)

    return A.transpose(), docs


if __name__ == "__main__": 
    print("sentences2matrix module running in diagnostics mode as __main__")
    action(True)
else:
    print("sentences2matrix module imported")

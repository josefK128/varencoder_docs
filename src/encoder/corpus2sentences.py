# corpus2sentences.py
# reads corpus and builds dictionary {doc-index:[doc-sentences],...} 
# returns dictionary docs 


import os
#import json


#closure vars for action() - free vars in action()
dbasepath = '../corpus/'  #location of corpus file(s) for diagnostics
vbasepath = './corpus/'   #location of corpus file(s) for vae run
corpusname = 'corpus0'    #default corpus0
docs = {}                 #dictionary of documents from corpus



def corpus(corpusnm = 'corpus0'):
    #identify corpusname as closure var, not local
    global corpusname
    print('\ncorpus2sentences.corpus(): setting corpusname to ' + corpusnm)
    corpusname = corpusnm


def action(diagnostics=False):
    #relative location of corpus relative to main file 
    if diagnostics == True:
        basepath = dbasepath + corpusname +'/'   #relative to /encoder
    else:
        basepath = vbasepath + corpusname + '/'   #relative to vae.py
    print('\ncorpus2sentences: basepath = ' + basepath)


    index = 0                #document ordinal identifier - key of dict docs
    for root, dirs, filenames in os.walk(basepath):
        for fn in filenames:
            if fn.endswith(".txt"): 
                if diagnostics: print('\n\n' + fn)
                with open(basepath+fn, "r") as f:
                    s = ''   #string representation of file f
                    for line in f:
                        if not line.startswith('$'):
                            s += line.replace("\n"," ").lstrip()
    
                    #split the file-string on '***' to form docs
                    a = s.split('***')
                    if diagnostics: print(str(len(a)) + ' documents')
                    for doc in a:
                        doc_sentences = []  #sentences associated with docs[doc] 
                        sentences = doc.split('.')  #sections of split doc string
                        if diagnostics: print(str(len(sentences)-1) + ' sentences')
                        for sentence in sentences:
                            sentence = sentence.strip()
                            if(len(sentence) >0):   #skip empty sentences exp last
                                if diagnostics: print(sentence)
                                doc_sentences.append(sentence) #add non-empty sent.
                        docs[index] = doc_sentences #sentence-list val for key index
                        index += 1

#    docsj = json.dumps(docs)
#    f = open(basepath + 'corpus0.json','w')
#    f.write(docsj)
#    f.close()                                 
#    print('wrote docs to ' + basepath + 'corpus0.json')


    if diagnostics == True:    
        print('\n\n\n********************************************')
        for index in docs:
            print('%%%%%%%%%')
            print('docs ' + str(index) + ' is ' + str(docs[index]))

    
    print('\n\n+++++++++++ corpus2sentences +++++++++++++++++++++')
    print('number of paragraphs extracted = ' + str(len(docs.values())))
    for k,v in docs.items():
        print('paragraph ' + str(k) + ' has ' + str(len(v)) + ' sentences')

    return(docs)


if __name__ == "__main__": 
    print("corpus2sentences module running in diagnostics mode as __main__")
    action(True)
else:
    print("corpus2sentences module imported")

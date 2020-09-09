# corpus2sentences.py
# reads corpus and builds Dict[int,List[str]] - {doc-index:[doc-sentences],...} 
# filters unnecessary and error-causing period expressions such as:
# i.e, e.g, A. Taylor (A.)
# returns dictionary docs to filter_sentences.py 


import os
import re
#import msg2sentences
from typing import Dict, List, Pattern



#closure vars for action() - free vars in action()
dbasepath = '../corpus/'  #location of corpus file(s) for diagnostics
vbasepath = './corpus/'   #location of corpus file(s) for vae run
corpusname = 'corpus0'    #default corpus0
docs:Dict[int,List[str]] = {}    #dictionary of documents from corpus



def corpus(corpusnm:str = 'corpus0') -> None:
    #identify corpusname as closure var, not local
    global corpusname
    corpusname = corpusnm


def filter(regex:Pattern, replace:str, s_pf:str, diagnostics:bool=False) -> str:
    #filter each text - eliminate i.e, e.g., A. Taylor
    s:str = re.sub(regex, replace, s_pf)  #filter by regex
    result = re.subn(regex, replace, s_pf)  #filter by regex

    if diagnostics:
        print('filtering detected ' + str(result[1]) + ' anomaly(ies)!!\n')
        if s != s_pf:
            print(s_pf + '\n\nreplaced by:\n\n' + s)
    return s


def action(diagnostics:bool=False) -> Dict[int, List[str]]:
    #relative location of corpus relative to main file 
    if diagnostics == True:
        basepath = dbasepath + corpusname +'/'   #relative to /encoder
    else:
        basepath = vbasepath + corpusname + '/'   #relative to vae.py
    

    print('\n\n+++++++++++ corpus2sentences +++++++++++++++++++++')
    print('corpus2sentences: basepath = ' + basepath)


    index = 0                #document ordinal identifier - key of dict docs
    for root, dirs, filenames in os.walk(basepath):
        for fn in filenames:
            if fn.endswith(".txt"): 
                with open(basepath+fn, "r") as f:
                    s = ''   #string representation of file f
                    for line in f:
                        if not line.startswith('$'):
                            s += line.replace("\n"," ").lstrip()


                    #filter each doc: 
                    print('\nfiltering text ' + fn )

                    #[1] eliminate i.e, e.g., A. Taylor
                    rs = '\s([a-z,A-Z]\.)+,*'
                    regex = re.compile(rs)
                    s_pf = s
                    s = filter(regex, '', s_pf, diagnostics)
                    
                    #[1] eliminate citations of form [34] for example
                    rs = '\[\d+\]'
                    regex = re.compile(rs)
                    s_pf = s
                    s = filter(regex, '', s_pf, diagnostics)

    
                    #split the file-string on '***' to form docs
                    a = s.split('***')
                    if diagnostics: print(str(len(a)) + ' documents')

                    for doc in a:
                        doc_sentences = []  #sentences associated with docs[doc] 

                        # break doc into sentences - store in sentences str[]
                        #sentences = msg2sentences.split_into_sentences(doc)
                        sentences = doc.split('.')  #sections of split doc string

                        if diagnostics: 
                            print('\n\ndoc ' + str(index))
                            print(str(len(sentences)-1) + ' sentences:')
                        for sentence in sentences:
                            # strip whitespace
                            sentence = sentence.strip()
                            print(f'sentence = {sentence}')

                            if(len(sentence) >0):   #skip empty sentences exp last
                                if diagnostics: print(sentence +'\n')
                                doc_sentences.append(sentence) #add non-empty sent.
                        docs[index] = doc_sentences #sentence-list val for key index
                        index += 1


    if diagnostics == True:    
        print('\n\n********************************************')
        for index in docs:
            print('%%%%%%%%%')
            print('docs ' + str(index) + ' is ' + str(docs[index]))
    else:
        print('number of paragraphs extracted = ' + str(len(docs.values())))
        for k,v in docs.items():
            print('paragraph ' + str(k) + ' has ' + str(len(v)) + ' sentences')


    return(docs)


if __name__ == "__main__": 
    print("corpus2sentences module running in diagnostics mode as __main__")
    action(True)
    #action(False)  #quick check of non-diagnostics output in diagnostics mode
else:
    print("corpus2sentences module imported")

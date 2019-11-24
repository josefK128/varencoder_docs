# vae.py 
# vae => Variational AutoEncoder
# encoder is Singular Value Decomposition (SVD) of the document-term matrix A
# SVD: A(nxm) = U(nxk) * S(kxk) * Vt(kxm) 
# variations are translations to close vectors in the semantic feature space U
# decoder is the mapping from the semantic feature space point (row-vector of U)
# to its corresponding sentence associated with the same row-vector in the 
# document-term matrix A


import os.path
from os import path
import time
import sys
sys.path.insert(0, './encoder')
import corpus2sentences 
import encoder 
sys.path.insert(0, './variation')
import variation
sys.path.insert(0, './decoder')
import decoder


basepath = './corpusgen/'


def action(diagnostics=False):
  
    #get corpusname from commandline (default = 'corpus0'
    nargs = len(sys.argv) - 1
    position = 1
    while nargs >= position:
        print('vae: sys.argv[' + str(position) + '] = ' + str(sys.argv[position]))
        position += 1


    #action based on sys.argv[position]
    corpusname = 'corpus0'
    prob = 1.0
    if nargs == 2:
        corpusname = sys.argv[1] 
        prob = sys.argv[2]
    if nargs == 1:
        corpusname = sys.argv[1] 
    else:
        print('too many command line args!')
        print('usage is  src>py vae.py [corpusname [prob]]')
        print('using corpusname = corpus0 and prob = 1.0')


    #set corpusname in corpus2sentences    
    print('vae: corpusname = ' + corpusname)
    corpus2sentences.corpus(corpusname)


    #start processing
    U, docs = encoder.action()

    #create dictionary mapping sentence index i to document 
    #paragraph-sentence [n,k] - nth doc, kth sentence in paragraph, i.e
    #array of sentences in doc
    map = {}
    index = 0
    for k,v in docs.items():
        s_index = 0
        for j in v:
            map[index] = [k,s_index]
            index += 1
            s_index +=1

    print('\n\n+++++++++++ vae +++++++++++++++++++++')
    print('docs:')
    print(docs)

    #report map of sentence index to [doc-index, sentence-index-in-doc]
    print('\n\nmap of sentence index to [doc-index, sentence-index-in-doc]:')
    print(map)


    if corpusname == 'corpus0':
        permutations = variation.action(U, map, prob, True)
    else:
        permutations = variation.action(U, map, prob)

    print('\n\n+++++++++++ vae +++++++++++++++++++++')
    print('permutations:')
    print(str(permutations))


    sentences_ = decoder.action(docs, map, permutations)
    print('\n\nsentences_:')
    print(sentences_)


    #finalize docs_
    docs_ = {}
    for k,a in docs.items():
        i = 0
        docs_[k] = ''
        for j in a:
            docs_[k] += sentences_[i] + '. ' 
            i += 1


    #for display - join the sentences in the arrays of sentences of docs
    print('\n\n\n\noriginal docs:')
    for k,a in docs.items():
        docs[k] = '. '.join(a) + '. '
        print('docs[' + str(k) + '] = ' + str(docs[k]) + '\n')


    print('\n\ngenerated docs_:')
    #print(docs_)
    for k,v in docs_.items():
        print('docs_[' + str(k) + '] = ' + str(docs_[k]) + '\n')


    #write docs to ./corpusgen/<corpusname>/docs
    #write docs_<time> to ./corpusgen/<corpusname>/docs_<date>
    #NOTE: there can be more than one version of docs_<date> :72,73s/date/time
    #docs_ files are timestamped by the 'epoch' time at their creation
    #these have a natural ordering in the corpusgen/<corpus_name> directory
    #docs.txt - constant so write only once - remove from dir to write fresh
    docspath = basepath + corpusname + '/docs.txt'
    if not path.exists(docspath):
        with open(docspath, 'wt') as f:
            print('\nwriting ' + docspath)
#            for k,a in docs.items():
#                docs[k] = '. '.join(a) + '. '
#                #print('docs[' + str(k) + '] = ' + str(docs[k]) + '\n')
            f.write(str(docs))
            f.close()

    #docs_<time>.txt
    docs_path = basepath + corpusname + '/docs_' + str(time.time()) + '.txt'
    with open(docs_path, 'wt') as f:
        print('\nwriting generated docs_ as ' + docs_path)
#        for k,a in docs_.items():
#            docs_[k] = '. '.join(a) + '. '
#            #print('docs_[' + str(k) + '] = ' + str(docs_[k]) + '\n')
        f.write(str(docs_))
        f.close()


    #check for repeats !!!!!
    for idx,v in docs_.items():
        x = v.split('.')
        _size = len(x) 
        repeated = [] 
        for i in range(_size): 
            k = i + 1
            for j in range(k, _size): 
                if x[i] == x[j] and x[i] not in repeated: 
                    repeated.append(x[i]) 
        print('docs_[' + str(idx) + '] repeated sentences = ' + str(repeated)) 



if __name__ == "__main__": 
    print("\n\nvae module running as __main__")
    action(True)
else:
    print("vae module imported")

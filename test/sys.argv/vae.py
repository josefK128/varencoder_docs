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
import sys
sys.path.insert(0, './encoder')
#%%%
import corpus2sentences 
#%%%

#import encoder 
#sys.path.insert(0, './variation')
#import variation
#sys.path.insert(0, './decoder')
#import decoder


def action(diagnostics=False):

    #%%% sys.argv
    nargs = len(sys.argv) - 1
    position = 1
    while nargs >= position:
        print('sys.argv[' + str(position) + '] = ' + str(sys.argv[position]))
        position += 1
        #action based on sys.argv[position]
        corpusname = sys.argv[1]
        print('corpusname = ' + corpusname)
        corpus2sentences.foo(corpusname)




if __name__ == "__main__": 
    print("\n\nvae module running as __main__")
    action(True)
else:
    print("vae module imported")

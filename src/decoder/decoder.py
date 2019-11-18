# decoder.py
#receives the map - sentences indices to doc index and sentence in 
#doc-sentences-array


import numpy as np


def action(docs, map, permutations, diagnostics=False):

    if diagnostics == True:
        print('\n\n+++++++++++ decoder +++++++++++++++++++++')
    #create sentences_ = {k:[n, sentence], ...} 
    #where k is the index of the kth sentence in sentences
    #n is the index of the document containing sentences[k]
    #and sentence is sentences[k]
    #below idx-d is the tuple associated with permutations key i, which is 
    #also the index of sentences
    sentences_ = {}
    for i,idx_d in permutations.items():   
        if diagnostics == True:
            print('\n\ni = ' + str(i) + ' idx_d = ' + str(idx_d))
        j = idx_d[0]      #index of nearest sentence to sentence[i]
        if diagnostics == True:
            print('j = ' + str(j))
        for k,tuple in map.items():
            if diagnostics == True:
                print('k = ' + str(k) + ' tuple = ' + str(tuple))
                print('j = ' + str(j) + ' k = ' + str(k))
            if j == k:
                sentences_[i] = docs[tuple[0]][tuple[1]] 
                if diagnostics == True:
                    print('i = ' + str(i))
                    print('tuple[0] = ' + str(tuple[0]))
                    print('tuple[1] = ' + str(tuple[1]))
                    print('sentences_[' + str(i) + '] = ' + sentences_[i])
                    print('***')

    return sentences_

if __name__ == "__main__": 
    print("decoder module running in diagnostics mode as __main__")

    docs = {0: ['we present a 3d stylization algorithm that can turn an input shape into the style of a cube while maintaining the content of the original shape', 'the key insight is that cubic style sculptures can be captured by the as rigid as possible energy with a regularization on rotated surface normals'], 1: ['the availability of image stylization filters and non-photorealistic rendering techniques has dramatically lowered the barrier of creating artistic  imagery to the point that even a non-professional user can easily create stylized images', 'in stark contrast, direct stylization of  3d shapes or non-realistic modeling has received far less attention']}

    permutations = {0: [1, 2.23606797749979], 1: [0, 2.23606797749979], 2: [3, 7.211102550927978], 3: [2, 7.211102550927978]}

    map = {0: [0, 0], 1: [0, 1], 2: [1, 0], 3: [1, 1]}

    action(docs, map, permutations, True)
else:
    print("decoder module imported")

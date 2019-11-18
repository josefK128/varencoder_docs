# variation.py
# Given a matrix U for each row r find the nearest k(=1) row(s) to r


import numpy as np
from numpy import random,argsort,sqrt
from scipy import spatial
from random import random


#def distance(a, b):
#    if len(a) != len(b):
#        print('\n' + str(a) + ' and ' + str(b) + ' have different lengths')
#        return None
#
#    v = np.subtract(a,b)
#    v = np.square(v)
#    sum = np.sum(v)
#    d = np.sqrt([sum])
#    return d


def replace(prob, i, idx, d):
    #print('\nreplace: prob = ' + str(prob))
    if prob == 1.0: 
        return [idx, d]
    if prob == 0.0:
        return [i, 0.0]

    if random() < prob:
        return [idx, d]
    else:
        return [i, 0.0]


def action(U, map, prob = 1.0, diagnostics = False):

    print('\n\n\n+++++++++++ variation +++++++++++++++++++++')
    #ensure prob is float and is in [0,1]
    if type(prob) == str:
        prob = float(prob)
    print('prob = ' + str(prob))
    print('diagnostics = ' + str(diagnostics))


    #permutations - i.e. replacements and associated semantic distances
    permutations = {}
    i = 0
    nchoices = 4    #retrieve nchoices closest U-vectors
    n = 0           #doc-paragraph

    #filter repeating closest-semantic-d sentences in same paragraph-doc 
    while i < len(map):
        indices_used = []
        match_found = False
        tuple = map[i]

        while tuple[0] == n:
            #tree
            row = U[i]
            rows = []
            for rw in U:
                if not np.array_equal(row,rw):
                    if diagnostics == True:
                        print('adding rw = ' + str(rw) + ' to rows')
                    rows.append(rw)
            tree = spatial.KDTree(rows)

            da, idxa = tree.query(U[i], nchoices)
#            for j in range(nchoices):
#                print('idxa[' + str(j) + '] = ' + str(idxa[j]))
#                print('da[' + str(j) + '] = ' + str(da[j]))

            #choose idx of closest U-vector to U[i] not U[i] and not prev chosen
            for k in range(nchoices):
                if not idxa[k] in indices_used:
                    if idxa[k] >= i:
                        permutations[i] = replace(prob, i, idxa[k] + 1, da[k])
                    else:
                        permutations[i] = replace(prob, i, idxa[k], da[k])

                    indices_used.append(idxa[k])
                    match_found = True
                    print('\nn = ' + str(n) + ' permutations[' + str(i) + ' = ' + str(permutations[i]))
                    break
    
            #if all len(idxa) matches are already used choose one at random
            if not match_found:
                print('\n\n################################### random choice!')
                m = np.rtandom.randint(nchoices)
                if idxa[m] >= i:
                    permutations[i] = replace(prob, i, idxa[m] + 1, da[m])
                else:
                    permutations[i] = replace(prob, i, idxa[m], da[m])
                match_found = True
    
            i += 1
            print('variation: i incremented is now ' + str(i))
            if i == len(map):
                break
            else:
                tuple = map[i]  #[n, sentence-index j]

        n += 1
        print('\n\n\n\nvariation: n incremented is now ' + str(n) + ' i = ' + str(i))


    if diagnostics == True:
        print('\n\npermutations:')
        print(str(permutations))

    return permutations


if __name__ == "__main__": 
    print("\n\nvariation module running in diagnostics mode as  __main__")
    U = np.array([[1,2,3,4],
                  [1,2,4,6],
                  [9,10,11,14],
                  [13,14,15,16]])

    action(U, True)
else:
    print("variation module imported")                

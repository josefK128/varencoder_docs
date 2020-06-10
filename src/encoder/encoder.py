# encoder.py
# obtains doc-term matrix A from sentences2matrix and also the docs dictionary
# created by corpus2sentencs.py (and passed upward to filter_sentences.py
# and sentences2matrix.py (which returns docs to encode)
# encoder.py performs Singular Value Decomposition on A to produce U*S*Vt
# U is the semantic feature space for the rows of A associated with all
# sentences in the corpus
# returns the semantic features matrix U, and the docs dictionary passed in
# by sentences2matrix.py


import numpy as np
import sentences2matrix as s2m
from typing import Tuple, List, Dict



def action(diagnostics:bool=False) -> Tuple[List[List[float]], Dict[int, List[str]]]:
    if diagnostics == True:
        A, docs = s2m.action(True)
    else:
        A, docs = s2m.action()


    #Singular Value Decomposition of A
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    print('\n\n\n+++++++++++ encoder +++++++++++++++++++++')
    print('SVD - esp. sentence-feature (encoding semantic space) matrix U:')
    print('A = U*S*Vt where:')

    # NOTE:mypy flags error - List[List[float]] does NOT have attr 'shape' 
    # Numpy ndarrays are not correctly type annotated - so ignore error
    print('matrix2d.shape is given by (rows, columns)')
    print('A.shape is ' + str(A.shape)); 
    print('U.shape is ' + str(U.shape));
    print('S.shape is ' + str(S.shape) + ' - diagonal of square matrix - non-diag els are zeroes');
    print('Vt.shape is ' + str(Vt.shape));
    print('U transpose is:\n')
    print(U.transpose())
 
    return U, docs


if __name__ == "__main__": 
    print("encoder module running in diagnostics mode as __main__")
    action(True)
else:
    print("encoder module imported")

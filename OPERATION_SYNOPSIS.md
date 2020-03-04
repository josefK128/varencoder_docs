__OPERATION_SYNOPSIS__

* for setup see README.md

* all relevant source files are in /src

* two typical usages are:
  

src> py vae.py  - runs using toy src/corpus/corpus0/toy_2 for simple diagnostics
and writes the generated corpus in src/corpusgen/corpus0/docs_<timestamp>
(NOTE: src/corpusgen/corpus0/docs is the original toy_2 corpus for ease of
reference)_


 src> py vae.py corpus3  - runs using using largest corpus src/corpus/corpus3/*
 for more realistic generated corpus at src/corpusgen/corpus3/docs_<timestamp>
 (NOTE: src/corpusgen/corpus3/docs is the original corpus3 for ease of reference) 


* the vae.py system is a functionally designed system with successive calls to the 'action' method of each module

* Each module can be run as either an independent self-contained test by running >py <module>.py, or by running the usage described above (>py vae.py [corpusK]) which runs a 'main' vae.py which sets up a hierarchical import of all other modules. In this usual application run vae.py imports and calls in succession encoder.py, variation.py, and decoder.py - the three parts of the Variational Encoder design pattern. Further encoder.py imports and calls in succession sentences2matrix.py, filter_sentences.py, and corpus2sentences.py.  NOTE: variation.py and decoder.py are singular modules - they do not import or call any submodules.

* KEY OPERATIONS: NOTE: exact details about actions, functions and returns can be found in very detained comments within the code at the appropriate opertional syntax

  1. vae.py

     corpus2sentences.corpus(corpus_name)  #set corpus mane in corpus2sentences.py

     U, docs = encoder.action(options)

     ​    2. encoder.py:

     ​         A, docs = sentences2matrix.action()

     ​             3. sentences2matrix:

     ​                   _docs, docs = filter_sentences.action()

     ​                          4. filter_sentences:

     ​                                docs = corpus2sentences.action()

     ​                                       5. corpus2sentences:

     ​                                               return docs

     ​                                return _docs, docs

     ​                   return A.transpose(), docs

     ​         A = U * S * Vt   #Singular value Decomposition of matrix A

     ​         return U, docs

     

     create map

     permutations = variation.action(U)

        6. variation.py

           create permutations    #semantically near feature vectors from U matrix

           return permutations

     

     sentences = decoder.action(docs, map, permutations)

        7. decoder.py:

           convert permutations to _sentences

           return _sentences

           

     create _docs using map

     write docs, _docs to src/corpusgen/<corpus_name>/docs  and docs<timestamp>

__README.md__

* install python 3.X (current latest 3.8.X) - see 
  https://www.python.org/downloads/ - simply click download button and follow 
  defaults for installation
* clone the repo - all the needed python application modules are in /src
* usage:  src> py vae.py [corpus2 [.5]]
  where first argument is corpus-name (corpus 0,1,2,3). Corpus0 (default) is a toy corpus
  of two texts each with two sentences intended just to show readable
  diagnostics of most of the steps leading to new corpus generation. The corpuses are numbered from smallets (0) to largest (3). Argument two is a probability for sentence replacement in the generated corpus with default being 1.0 (all sentences replaced)  NOTE: for the most original generated corpus it is best to use probability = 1.0 (default)
* Exps: 
  * src> py vae.py   (use corpus0 and probability=1.0)
  * src> py vae.py  corpus2  (use corpus2 and probability=1.0)
  * src> py vae.py  corpus2  .5  (use corpus2 and probability=0.5 for sentence replacement)
* all corpus examples are in src/corpus and the generated corpus examples are in
  corpusgen/<corpusK>  The original corpus (named 'docs') is copied for 
  reference and each run produces a distinct generated corpus with same name
  and a unique increasing timestamp (exp. docs_1573623216.9062061

__README.md__

* install python 3.X (current latest 3.8) - see 
  https://www.python.org/downloads/ - simply click download button and follow 
  defaults for installation
* clone the repo - all needed python modules are in /env, a virtual environment
  used to maintain consistency of needed versions
* usage:  src> py vae.py [corpus2 [.5]]
  where first argument is corpus-name (corpus 0,1,2,3). Corpus0 (default) is a toy corpus
  of two texts each with two sentences intended just to show readable
  diagnostics of most of the steps leading to new corpus generation
  Argument two is a probability for sentence replacement in the generated corpus
with default being 1.0 (all sentences replaced) 
* Exps: 
  * src> py vae.py   (use corpus0 and probability=1.0)
  * src> py vae.py  corpus2  (use corpus2 and probability=1.0)
  * src> py vae.py  corpus2  .5  (use corpus2 and probability=0.5 for sentence replacememt)
* all corpus examples are in src/corpus and the generated corpus examples are in
  corpusgen/<corpusK>  The original corpus (named 'docs') is copied for 
  reference and each run produces a distinct generated corpus with same name
  and a unique increasing timestamp (exp. docs_1573623216.9062061

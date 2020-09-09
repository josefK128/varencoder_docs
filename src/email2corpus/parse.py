# parse.py: email -> corpus

import os
import sys
import json
from typing import List, Dict


# determine emails - directory-name of collection of json-emails
if len(sys.argv) > 1:
    emails = sys.argv[1]
else:
    emails = 'emails1'
print('\nemails = ' + emails)


# vars
data:Dict = {}
msgs:str = "" 
emailpath = '../email/' + emails
corpuspath = '../corpus/' + emails
corpusname_ = emails + '.txt'
corpuspath_ = os.path.join(corpuspath, corpusname_)

# open target corpus-name (create if needed +)
fw = open(corpuspath_, 'w+')

# diagnostics
print('corpuspath_ = ' + corpuspath_)



# parse files in emails
i = 0
for filename in os.listdir(emailpath):
    filepath = os.path.join(emailpath, filename)
    print('---------------------------------------------------')
    print('****** filepath = ' + filepath)

    # parse email json files
    with open(filepath, 'r') as f:
        data = json.load(f) 
        msg = data['msg']
        f.close()

        # diagnostics
        #print(msg)

        # add to List of messages
        if i > 0:
            print('adding *** to msgs')
            msgs = msgs + "\n***\n"
        print(f'adding msg to msgs, i = {i}')
        msgs = msgs + msg
    i += 1
        


# write msgs to corpuspath_
fw.write(msgs)
fw.close()


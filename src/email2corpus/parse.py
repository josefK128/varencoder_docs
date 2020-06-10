# parse.py: emails -> corpus

import os
import sys
import json
from typing import List, Dict


# determine thread
if len(sys.argv) > 1:
    thread = sys.argv[1]
else:
    thread = 'thread1'
print('\nthread = ' + thread)


# vars
data:Dict = {}
msgs:str = "" 
directory = '../email/' + thread
directory_ = '../corpus/' + thread
filename_ = thread + '.txt'
filepath_ = os.path.join(directory_, filename_)

# open target corpus-name
fw = open(filepath_, 'w+')

# diagnostics
print('filepath_ = ' + filepath_)



# parse files in thread
i = 0
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
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
        


# write msgs to filepath_
fw.write(msgs)
fw.close()


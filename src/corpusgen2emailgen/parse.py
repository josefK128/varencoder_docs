# parse.py: corpusgen -> emailgen

import os
import sys
import json
from typing import List, Dict


# determine corpus
if len(sys.argv) > 1:
    corpus = sys.argv[1]
else:
    corpus = 'corpus1'
print('\ncorpus = ' + corpus)


# vars
data:Dict = {}
msgs:str = "" 
directory = '../corpusgen/' + corpus
directory_ = '../emailgen/' + corpus
filepath = directory + '/' + 'docs_.json'
filepath_ = directory_ + '/'


# parse json file to extract json-emails
with open(filepath, 'r') as f:
    dict = json.load(f) 
    #print(f'pair = {pair}')

    for items in dict.items():
        # form email json 
        data['msg'] = items[1]
        data['sender'] = ''
        data['receivers'] = []
        data['sent'] = ''
        data['subject'] = ''
    
        path = filepath_ + 'email' + items[0] + '.json'
        fw = open(path, 'w')
        json.dump(data, fw)
        




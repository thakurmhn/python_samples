#!/usr/bin/env python3.5

import random
import json
import os

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open("/usr/share/dict/words").readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
               #below is string formating for python3.5
    with open("./new/reciept-%s.json" %identifier, 'w') as F:
             # same in python 3.6 will be
    #with open("./new/reciept-{identifier}.json", 'w') as F:
        json.dump(content, F)

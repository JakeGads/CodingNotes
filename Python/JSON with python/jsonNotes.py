'''
Quick Tutorial on using the JSON pacakge for python 
'''

import json

x = {
    'name':'Jake',
    'age':20,
    'scores': [5,4,3,2,1]
}

# One Object per JSON

print(json.dumps(x))
# Converts into Json
with open('example.json', 'w+') as outWrite:
    # Dumps Preps it, dump writes it out
    json.dump(json.dumps(x), outWrite)
    # json.dump(json.dumps({'name':'Amanda', 'age':19}), outWrite)

with open('example.json', 'r') as inRead:
    data = json.load(inRead)
    print(data)

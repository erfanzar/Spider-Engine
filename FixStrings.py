import json
from opcode import opname



pend = open('outEngine.json' , 'r')

op = []

data = json.load(pend)
print(data)

for i in data['Name']:
    # print(i)
    i=i.replace(" ","-")
    print(i)
    op.append(i)


dic = {
        "name" : op
}

print(dic)


with open('Drugs.json' , 'a') as ou:
    json.dump(dic , ou)
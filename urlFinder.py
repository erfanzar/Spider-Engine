import json


pendata = open('Drugs.json' , 'r')

data = json.load(pendata)

urls = []

for i in data['name']:
    i = f'https://www.rxlist.com/{i}drug.htm#indications'
    urls.append(i)
    print(i)

    
dic = {
    'url': urls
}
with open('urls.json' , 'a') as ou:
    json.dump(dic , ou)


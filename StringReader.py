import json


pendata = open('phrm.json' , 'r')



data = json.load(pendata)

for a in data['howToUse']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')



for a in data['indication']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')


for a in data['Dosage']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')


for a in data['sideEffects']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')


for a in data['warnings']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')


for a in data['overdose']:
    a.replace('\u00a0','')
    a.replace('\u00df','')
    a.replace('\r' , '')
    a.replace('\n' , '')
    a.replace('\u00b0C','')
    a.replace('\u00b0F','')

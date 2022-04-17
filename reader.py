
import json
import numpy as np


A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []
L = []
M = []
N = []
O = []
P = []
Q = []
R = []
S = []
T = []
U = []
V = []
W = []
X = []
Y = []
Z = []






def Reader():


    letters = ['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']


    f = open('DrugNames.json')

    data = json.load(f)





    for k in letters:
        for i in data[f'{k}']['name']:
            print(f'with {k} in {i}')
            # k.append(i)




    for a in data['A']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        A.append(a)
        print(a)



    for a in data['B']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        B.append(a)
        print(a)

    for a in data['C']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        C.append(a)
        print(a)

    for a in data['D']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        D.append(a)
        print(a)



    for a in data['E']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        E.append(a)
        print(a)

    for a in data['F']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        F.append(a)
        print(a)

    for a in data['G']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        G.append(a)
        print(a)



    for a in data['H']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        H.append(a)
        print(a)

    for a in data['I']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        I.append(a)
        print(a)
        
    for a in data['J']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        J.append(a)
        print(a)



    for a in data['K']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        K.append(a)
        print(a)

    for a in data['L']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        L.append(a)
        print(a)
        

    for a in data['M']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        M.append(a)
        print(a)



    for a in data['N']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()
        N.append(a)
        print(a)

    for a in data['O']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()
        O.append(a)
        print(a)
        

    for a in data['P']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        P.append(a)
        print(a)



    for a in data['Q']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        Q.append(a)
        print(a)


    for a in data['R']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        R.append(a)
        print(a)
        
    for a in data['S']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()

        S.append(a)
        print(a)



    for a in data['T']['name']:
        print(a)
        a = a.split("(")
        a = a[0]

        a=a.lower()
        T.append(a)
        print(a)

    for a in data['U']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()

        U.append(a)
        print(a)
        
    for a in data['V']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()

        V.append(a)
        print(a)
        print(a)



    for a in data['W']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()

        W.append(a)
        print(a)

    for a in data['X']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()
        X.append(a)
        print(a)
        


    for a in data['Y']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a= a.lower()
        Y.append(a)
        print(a)

    for a in data['Z']['name']:
        print(a)
        a = a.split("(")
        a = a[0]
        a=a.lower()
        Z.append(a)
        print(a)




if __name__ == '__main__':
    Reader()
    dic = {
        'Name' : [
            A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
        ]
    }

    with open('outEngine.json' , 'w') as ou:
        json.dump(dic , ou)
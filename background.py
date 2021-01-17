from math import *

def crypterDecimalRacine(ch):
    t=''
    for i in range(len(ch)):
        t+=str(floor(sqrt(ord(ch[i].upper()))*100))
    return t
def crypterBinaireListe(ch):
    s=[]
    for i in range(len(ch)):
        s+=[bin(int(ch[i]))[2:]]
    return s
def crypterBinaireZero(L):
    M=[]
    for i in range(len(L)):
        if len(L[i])<=4:
            M+=[(4-len(L[i]))*str(0)+L[i]]
    return M
def crypterBinaireChaine(L):
    s=''
    for i in range(len(L)):
        s+=L[i]
    return s
def crypterSeparer(ch):
    L=[]
    for i in range(len(ch)):
        L+=[ch[i]]
    return L
def crypterCalculer(L):
    n=0
    for i in range(len(L)):
        n+=int(L[i])*(2**i)
    return n


def decrypterCalculer(n):
    M=[]
    a=bin(n)[2:]
    for i in range(len(a)):
        M+=[a[i]]
    M.reverse()
    return M
def decrypterBinaireChaine(L):
    s=''
    for i in range(len(L)):
        s+=L[i]
    return s

def decrypterBinaireListe(ch):
    s=''
    for i in range(0,len(ch),4):
        s+=str(int(ch[i:i+4],2))
    return s

def decrypterDecimalRacine(ch):
    L=[] ; s=''
    for i in range(0,len(ch),3):
        if ((int(ch[i:i+3])/100)**2)==floor((int(ch[i:i+3])/100)**2):
            L+=[floor((int(ch[i:i+3])/100)**2)]
        else:
            L+=[floor((int(ch[i:i+3])/100)**2)+1]
    for i in range(len(L)):
        s+=chr(L[i])
    return s.lower()


def crypter(ch):
    a=crypterDecimalRacine(ch)
    b=crypterBinaireListe(a)
    c=crypterBinaireZero(b)
    d=crypterBinaireChaine(c)
    e=crypterSeparer(d)
    f=crypterCalculer(e)
    return f

def decrypter(n):
    a=decrypterCalculer(n)
    b=decrypterBinaireChaine(a)
    c=decrypterBinaireListe(b)
    d=decrypterDecimalRacine(c)
    return d


def code2decode():
    g=open('decode.txt','w')
    f=open('code.txt','r')
    ch=f.read()
    g.write(decrypter(int(ch)))
    g.close()

def decode2code():
    f=open('decode.txt','r')
    g=open('code.txt','w')
    ch=f.read()
    g.write(str(crypter(ch)))
    g.close()

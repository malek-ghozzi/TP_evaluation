"""
Déclarations des bibliothéques

"""
import matplotlib.pyplot as plt 
import numpy as np

"""
Déclarations de variables

"""
t= np.linspace(1,24) # de à 24 essais
D=0.30
Dmax=0.301
Z=37.10/60 # convertir Zmoy en minitues

"""
Calcule et affichage de X(N)
d'ou 
An < X(N) < min(Bn,Cn)

"""
def An(N):
    A=[]
    for i in N:
        A.append(i/((i*D)+Z))
    return A

def Bn(N):
    B=[]
    for i in N:
        B.append(1/Dmax)
    return B

def Cn(N):
    C=[]
    for i in N:
        C.append(i/(D+Z))
    return C

AN=An(t)
BN=Bn(t)
CN=Cn(t)

plt.figure(1)
plt.plot(t,AN,label="N/ND+Z")
plt.plot(t,BN,label="1/Dmax")
plt.plot(t,CN,label="N/D+Z")
plt.title("Courbe du débit du système X(N)")
plt.legend()
plt.grid()


"""
Calcule et affichage de R(N)
d'ou 
max(Dn,En) < X(N) < Fn

"""
def Dn(N):
    D=[]
    for i in N:
        D.append((i*Dmax)-Z)
    return D

def En(N):
    E=[]
    for i in N:
        E.append(D)
    return E

def Fn(N):
    F=[]
    for i in N:
        F.append(i*D)
    return F


DN=Dn(t)
EN=En(t)
FN=Fn(t)

plt.figure(2)
plt.plot(t,DN,label="NDmax")
plt.plot(t,EN,label="D")
plt.plot(t,FN,label="ND")
plt.title("Courbe du temps de réponse R(N)")
plt.legend()
plt.grid()
plt.show()
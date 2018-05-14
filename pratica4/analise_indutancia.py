import numpy as np
from LabIFSC import M
from erros_mult import err_o200

mu_0 = 4e-7*np.pi

N1 = M((760,0))
a = M((15.20e-2,.05e-3))
N2 = M((2100,0))
b = M((59.95e-3,.05e-3))
D = M((14.90e-3,.05e-3))

A = np.pi*D*D/4 # área de seção reta do solenoide interno

Lteo = mu_0*N1*N2*A/a # indutância mútua obtida teoricamente

R = M((98.6,err_o200(98.6))) # (escala de 200 ohm) resistência do resistor ligado ao solenoide externo
dados7 = np.loadtxt('pratica4/dados/indutancia.dat').T
f = dados7[0] # +- 0.05, frequência (Hz) da corrente alternada
erro_f = f*0 + 0.05
eps0 = dados7[1] # tensão de pico no solenoide interno
erro_eps0 = dados7[2]
V0 = dados7[3] # tensão de pico no resistor ligado ao solenoide externo
erro_V0 = dados7[4]

Lmed = []
for i in range(len(f)):
    eps0i = M((eps0[i],erro_eps0[i]))
    fi = M((f[i],0.05))
    V0i = M((V0[i],erro_V0[i]))
    Lmed.append(eps0i*R/(2*np.pi*fi*V0i))
Lmed = np.array(Lmed)

print("Indutância pelos parâmetros geométricos: {}mT/As".format(Lteo*1e3))
print("Indutância pelos dados experimentais:")
for lmed in Lmed: print("        {}mT/As".format(lmed*1e3))
print("Média = {}mT/As".format(Lmed.mean()*1e3))

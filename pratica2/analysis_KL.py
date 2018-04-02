import numpy as np
from LabIFSC import M

# OBJETIVO
# Mostrar que a corrente que entra em um nó é experimentalmente
# equivalente às correntes que saem deste nó.

N = 2
file = "data/kcl_{}.dat".format(N)
data = []
data_np = np.loadtxt(file)
data.append(data_np)
data = np.asarray(data) if len(data_np.shape)==1 else data_np

Ie = [M((i[0], i[-1])) for i in data]
I0 = [M((i[1], i[-1])) for i in data]
I1 = [M((i[2], i[-1])) for i in data]
I2 = [M((i[3], i[-1])) for i in data] if len(data[0]) > 4 else 0
I3 = [M((i[4], i[-1])) for i in data] if len(data[0]) > 4 else 0

if (N==1):
    print("Para o primeiro circuito temos que:            ")
    print("I_0 + I_1 = I_e\n------")
    for i in range(data.shape[0]):
        print("{:-,ifsc,-3} = {:-,ifsc,-3} : {}".format(I0[i]+I1[i],Ie[i],I0[i]+I1[i]==Ie[i]))
else:
    print("Para o segundo circuito temos que:            ")
    print("I_0 + I_1 = I_2\n------")
    for i in range(data.shape[0]):
        print("{:-,ifsc,-3} = {:-,ifsc,-3} : {}".format(I0[i]+I1[i],I2[i],I0[i]+I1[i]==I2[i]))
    print("\nE também:")
    print("I_2 + I_3 = I_e\n------")
    for i in range(data.shape[0]):
        print("{:-,ifsc,-3} = {:-,ifsc,-3} : {}".format(I2[i]+I3[i],Ie[i],I2[i]+I3[i]==Ie[i]))

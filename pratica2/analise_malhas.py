import numpy as np
from LabIFSC import M

# OBJETIVO:
# Calcular as quedas de potencial numa malha e mostrar que a soma
# é zero.

# PROCEDIMENTO:
# Colocar o voltímetro nos terminais de cada componente.
#
# Qual o erro propagado deste método? Pela altíssima resistencia interna
# voltimetro, ele não puxará muito da corrente, e como no caso anterior,
# a precisao dos instrumentos é maior que a alteração que as resistencias internas
# do multimetro pode causar.

N = 2
file = "pratica2/data/kvl_{}.dat".format(N) # pratica2/
data = []
data_np = np.loadtxt(file)
data.append(data_np)
data = np.asarray(data) if len(data_np.shape)==1 else data_np

Vfonte = [M((i[0], i[-1])) for i in data]
Va = [M((i[1], i[1]*0.05)) for i in data]
Vb = [M((i[2], i[2]*0.05)) for i in data]
Vc = [M((i[3], i[3]*0.05)) for i in data]
Vd = [M((i[4], i[4]*0.05)) for i in data] if len(data[0]) > 5 else 0
Ve = [M((i[5], i[5]*0.05)) for i in data] if len(data[0]) > 5 else 0
Vfonte2 = [M((i[6], i[-1])) for i in data] if len(data[0]) > 5 else 0


for i in range(4):          # quantidade de dados
        print("${:latex}$ & ${:latex}$ & ${:latex}$ & ${:latex}$ & Sim \\\\".format(Vc[i], Vb[i], Vfonte2[i], Vd[i]))


if (N==1):
    print("V_fonte - V_A - V_B - V_C = 0")
    for i in range(data.shape[0]):
        u_soma = Vfonte[i]
        u_queda = Va[i]+Vb[i]+Vc[i]
        zero = M((0,data[i][-1]))
        print("{} = {} : {}".format(u_soma-u_queda, zero, u_soma-u_queda==zero ))
else:
    print("MALHA 1: V_fonte - V_A - V_C - V_E = 0")
    for i in range(data.shape[0]):
        u_soma = Vfonte[i]
        u_queda = Va[i]+Vc[i]+Ve[i]
        zero = M((0,data[i][-1]))
        print("{} = {} : {}".format(u_soma-u_queda, zero, u_soma-u_queda==zero ))


    print("\nMALHA 2: V_C - V_B + V_fonte2 - V_D = 0")
    for i in range(data.shape[0]):
        u_soma = Vc[i]+Vfonte2[i]
        u_queda = Vb[i]+Vd[i]
        zero = M((0,data[i][-1]))
        print("{} = {} : {}".format(u_soma-u_queda, zero, u_soma-u_queda==zero ))

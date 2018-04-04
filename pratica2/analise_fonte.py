import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt('pratica2/data/fonte.dat')
V_i, V_c = dados.T

r_e = 4.6 # atualizar com a medida real durante a prática
i = V_i/r_e
Pu = (V_i+V_c)*i
R = V_c/i

# teorema da máxima transferência de potência
indice_pmax = np.argmax(Pu)
indice_pmax
r_i = R[indice_pmax] + r_e
r_i

print(r_i)

# parte (6)
Pd = r_i*i**2
Pt = Pd + Pu
eta = Pu/Pt

# PLOTAR TUDO EM FUNÇÃO DE x = R + r_e
x = R + r_e
R
plt.figure(dpi=100)
plt.plot(x,Pu,'.',x,Pd,'.',x,Pt,'.')
plt.legend(['Potência útil','Potência dissipada','Potência total','Eficiência'])

import matplotlib.pyplot as plot
import numpy as np

dados = np.loadtxt('dados/fonte.dat')
V_i, V_c = dados.T

r_e = 4.7 # atualizar com a medida real durante a prática
i = V_i/r_e
Pu = (V_i+V_c)*i
R = V_c/i

# teorema da máxima transferência de potência
indice_pmax = np.argmax(Pu)
r_i = R[indice_pmax] + r_e

print(r_i)

# parte (6)
Pd = r_i*i**2
Pt == Pd + Pu
eta = Pu/Pt

# PLOTAR TUDO EM FUNÇÃO DE x = R + r_e
x = R + r_e
plt.plot(x,Pu,x,Pd,x,Pt,x,eta,'--k')
plt.legend(['Potência útil','Potência dissipada','Potência total','Eficiência'])

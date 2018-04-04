import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt('pratica2/data/wheatstone.dat')
Vp, i = dados.T

# substituir com valores reais medidos
Vf = 5.01
R1, R2, R3 = 671, 666, 470

# análise
mu, l = Vp/Vf, R2/(R1+R2)
Rx = R3*(l-mu)/(1-l+mu)

# plot
plt.figure(dpi=90)
plt.plot(Rx,Vp,'.',Rx,Rx*0,'k')
plt.xlabel('Resistência do potenciômetro (Ω)')
plt.ylabel('Tensão na ponte (V)')
plt.title('Ponte de Wheatstone')

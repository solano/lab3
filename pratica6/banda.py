# Largura de banda: frequências onde a potência é metade do máximo

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt

R = np.linspace(1,1e3,1000)
L = 44e-3
C = 1e-7
w0 = 1/sqrt(L*C)

a = R**2 + 2*L/C
b = R*sqrt(R**2 + 4*L/C)
w1 = sqrt((a-b)/(2*L*L))
w2 = sqrt((a+b)/(2*L*L))

plt.figure(dpi=300)
f = 1e-3
plt.plot(R,w1*f,'-')
plt.plot(R,w2*f,'-')
plt.xlabel(r'Resistência ($\Omega$)')
plt.ylabel(r'Frequência angular (10$^{3}$ rad/s)')
plt.xlim(0,1000)
plt.ylim(0,32)
i=600
plt.annotate('',xy=(R[i],w1[i]*f),xytext=(R[i],w2[i]*f),
    arrowprops=dict(arrowstyle='<->',shrinkA=0,shrinkB=0),size='x-large')
plt.annotate(r'$\Delta \omega = R/L$',xy=(R[i+25],(w1[i]+w2[i])*f/2))
plt.title(r'Largura de banda do circuito RLC, L = 44 mH, C = 100 nF')
plt.savefig('pratica6/banda.png',bbox_inches='tight')

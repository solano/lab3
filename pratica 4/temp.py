import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

u = 12e-7 #constante magnética
# I = 1 #corrente elétrica
# a = 10e-2 #raio da espira
# B = lambda z: u*I/2*a**2/(z**2+a**2)**(3/2)
#
# r = np.linspace(-20e-2,20e-2,41)
# plt.figure(dpi=100)
#
# plt.plot([0,0], [-5,7], color="lightgray")
# plt.plot([-20,20], [0,0], color="lightgray")
# plt.plot(r*1e2,(B(r))*1e6, color="red", label="Individual")
# plt.plot(r*1e2, (B(r-a/2)-B(r+a/2))*1e6, label="Helmholtz")
# plt.xlim([-20,20])
# plt.ylim([-5,7])
# plt.plot([-5,0,5], [0,0,0], 'ok')
# plt.text(-7,1, "Bobina 1\nHelmholtz")
# plt.text(4,1, "Bobina 2\nHelmholtz")
# plt.text(-.5,-2, "Bobina\nIndividual")
# plt.title(r"Bobinas de raio $a=10$ cm")
# plt.xlabel("Posição do sensor Hall (cm)")
# plt.ylabel(r"Campo magnético ($\mu$T)")
# plt.legend(loc=0)
# plt.savefig("tarefa23.png", dpi=300)

# I = 0.25
# L = 30e-2
# R = 2e-2
# n = 120
# B = lambda z : u*n*I/2*((L/2-z)/((L/2-z)**2 + R**2)**.5   + (L/2+z)/((L/2+z)**2 + R**2)**.5)
# B_approx = lambda z: u*n*I+z*0
# x = np.linspace(-L/2,L/2,50)
# x_approx = np.linspace(-L/3,L/3,50)
#
#
#
# plt.figure(dpi=100)
# #plt.ylim([75,155])
# plt.plot(x*1e2, B(x)*1e6, color="red", label="Solução exata")
# plt.plot(x_approx*1e2, B_approx(x_approx)*1e6, "--k", label=r"Aproximação para $L\gg R$")
# plt.xlabel("Posição do sensor Hall (cm)")
# plt.ylabel(r"Campo magnético ($\mu$T)")
# plt.legend(loc=0)
# plt.title(r"Campo magnético de um solenoide $L=30$ cm, $R=2$ cm")
# plt.savefig("tarefa1.png", dpi=300)

x = np.linspace(0,2*np.pi, 200)
plt.figure(dpi=150)
#plt.plot(x, 2*np.sin(x), color="black" ,label="Corrente do circuito")
plt.plot(x, 2*np.sin(x)*u*1e6, label="Campo do circuito")
plt.plot(x, -12e-7*8*220**2*2*np.cos(x), label="Campo induzido")
plt.plot(x, 2*np.sin(x)*u*1e6-12e-7*8*220**2*2*np.cos(x), '--', label="Sobreposição dos campos")
plt.yticks([0])
plt.xticks([np.pi/2,np.pi], [r"$\pi/2$",r"$\pi$"])
plt.xlabel("Tempo (s)")
plt.grid()
plt.text(3*np.pi/2.5, 1.5, r"$B(t) = A\sin(\omega t)+B\cos(\omega t)$")
plt.legend(loc="lower left")
#plt.savefig("tarefa4iisa.png", dpi=300)

np.max(2*np.sin(x)*u*240)

np.max(-12e-7*8*220**2*2*np.cos(x))
plt.figure(dpi=150)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

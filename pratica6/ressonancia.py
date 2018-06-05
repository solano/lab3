# Ressonância num circuito RLC

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt

L = 44e-3
C = 1e-7
R = 100
w0 = 1/sqrt(L*C)

V0 = 5

I0 = lambda w, R: V0/sqrt(R**2 + (w*L-1/(w*C))**2)
Pmed = lambda w: 0.5*V0**2*R/(R**2 + (w*L - 1/(w*C))**2)

# plt.figure(dpi=300)
# for R in (47,100,220):
#     w = np.linspace(1e-3*w0,w0*2.5,400)
#     plt.plot(w/w0,I0(w,R),label=r'R = {} $\Omega$'.format(R))
# plt.plot([1,1],[0,1],'--k',alpha=0.5)
# plt.xlabel(r'$\omega/\omega_0$')
# plt.ylabel(r'Amplitude de corrente $I_0$ (A)')
# plt.xlim(0,2.5)
# plt.ylim(0,0.11)
# plt.legend(loc='right')
# plt.title(r'Circuito RLC com $L$ = 44 mH, $C$ = 100 nF')
# plt.savefig('pratica6/ressonancia.png',bbox_inches='tight')

# plt.figure(dpi=300)
# for C in (1e-6,1e-7,1e-8):
#     w0 = 1/sqrt(L*C)
#     w = np.linspace(1e-3*w0,w0*3,400)
#     plt.plot(w/w0,I0(w,R),label='C = {} nF'.format(int(C*1e9)))
# plt.xlabel(r'$\omega/\omega_0$')
# plt.ylabel(r'Amplitude de corrente $I_0$ (A)')
# plt.xlim(0,3)
# plt.ylim(0,5.3e-2)
# plt.legend(loc='right')
# plt.title(r'Circuito RLC com $L$ = 44 mH, $R$ = 100 $\Omega$')
# plt.savefig('pratica6/ressonancia2.png',bbox_inches='tight')

# plt.figure(dpi=300)
# f = 1e-6
# x = np.linspace(1/sqrt(1000e-9*L),1/sqrt(1e-9*L), 10)*f
# plt.plot(x,x,'ok')
# plt.xlim(0,1.1*1/sqrt(1e-9*L)*f)
# plt.ylim(0,1.1*1/sqrt(1e-9*L)*f)
# plt.xlabel(r'$(LC)^{-1/2}$ ($10^6$ s$^{-1}$)')
# plt.ylabel(r'$\omega_0$ ($10^6$ s$^{-1}$)')
# plt.title(r'Frequência de ressonância e o produto $LC$')
# plt.savefig(r'pratica6/ressonancia3.png',bbox_inches='tight')

plt.figure(dpi=300)
f = 1e3
for R in (470,):
    a = R**2 + 2*L/C
    b = R*sqrt(R**2 + 4*L/C)
    w1 = sqrt((a-b)/(2*L*L))
    w2 = sqrt((a+b)/(2*L*L))
    w = np.linspace(1e-3*w0, 3*w0, 200)
    Ppico = V0*V0/(2*R)
    plt.plot([0,3],[f*Ppico/2,f*Ppico/2],'--k',alpha=0.5)
    plt.plot(w/w0,Pmed(w)*f)
    plt.plot([w1/w0,w2/w0],[f*Ppico/2,f*Ppico/2],'.g')
    plt.annotate('',xy=(w1/w0,f*Ppico/2), xytext=(w2/w0,f*Ppico/2),
        arrowprops=dict(arrowstyle='<->'), size='xx-large')
    plt.annotate(r'$\Delta \omega$', xy=((1.2*w1+0.8*w2)/(2*w0),
     f*0.85*Ppico/2))
plt.xlim(0,3)
plt.ylim(0,29)
plt.xlabel(r'$\omega/\omega_0$')
plt.ylabel(r'Potência média (mW)')
plt.title(r'Potência dissipada com $R$ = 470 $\Omega$, $L$ = 44 mH, $C$ = 100 nF')
plt.savefig('pratica6/ressonancia-banda.png',bbox_inches='tight')

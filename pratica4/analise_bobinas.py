import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from LabIFSC import M
from erros_mult import *

mu_0 = 4e-7*np.pi # valor exato

# esse valor vem de analise_calibracao.py
K = M((265.653591676,0.641925750322))

N = 130 # número de espiras por bobina

# Modelos para ajuste
def bobina(z, I, a, z0):
    return mu_0*N*I*a**2/(2*((z-z0)**2 + a**2)**(3/2))
def antihelmholtz(z, I, a, b, z0):
    return bobina(z-b/2,I,a,z0) - bobina(z+b/2,I,a,z0)

# Bobina
dados31 = np.loadtxt('pratica4/dados/bobina.dat').T
z,Vh = dados31
erroVh = erro_array(Vh,err_v200m)
Vfundo = M((-.002,err_v200m(-.002)))
Vh = Vh - Vfundo.nominal
erroVh = np.array(erroVh) + Vfundo.incerteza
B, erroB = [], []
for i in range(len(Vh)):
    b = M((Vh[i],erroVh[i]))/K
    B.append(b.nominal)
    erroB.append(b.incerteza)
B,erroB = np.array(B),np.array(erroB)
a = 14e-2
I = 1.0

ajuste31,mcov31 = optimize.curve_fit(bobina,z,B,[I,a,0],erroB)
I = ajuste31[0]
erro_I = np.sqrt(mcov31[0][0])
a = ajuste31[1]
erro_a = np.sqrt(mcov31[1][1])
z0 = ajuste31[2]
erro_z0 = np.sqrt(mcov31[2][2])
print('Ajuste (bobina):')
print('Corrente = {}A'.format(M((I,erro_I))))
print('Raio a = {}m'.format(M((a,erro_a))))
print('Offset z0 = {}m'.format(M((z0,erro_z0))))

plt.figure(dpi=300)
tz = 1.05*np.linspace(-a,a,300)
plt.plot(1e2*tz,1e3*bobina(tz,I,a,z0),label='Ajuste',zorder=0)
plt.errorbar(1e2*z,B*1e3,erroB*1e3,z*0+0.1e-2,'.k',label="Dados experimentais",zorder=1)
plt.legend()
plt.title('Bobina circular')
plt.xlabel("Posição (cm)")
plt.ylabel("Campo magnético (mT)")
plt.savefig('pratica4/figuras/bobina.png',bbox_inches='tight')

# Par anti-Helmholtz
dados32 = np.loadtxt('pratica4/dados/antihelmholtz.dat').T
z,Vh = dados32
erroVh = erro_array(Vh,err_v200m)
Vfundo = M((-.001,err_v200m(-.001)))
Vh = Vh - Vfundo.nominal
erroVh = np.array(erroVh) + Vfundo.incerteza
B, erroB = [], []
for i in range(len(Vh)):
    b = M((Vh[i],erroVh[i]))/K
    B.append(b.nominal)
    erroB.append(b.incerteza)
B,erroB = np.array(B),np.array(erroB)
a = 14e-2
I = 1.0

ajuste32,mcov32 = optimize.curve_fit(antihelmholtz,z,B,[I,a,a,0],erroB)
I = ajuste32[0]
erro_I = np.sqrt(mcov32[0][0])
a = ajuste32[1]
erro_a = np.sqrt(mcov32[1][1])
b = ajuste32[2]
erro_b = np.sqrt(mcov32[2][2])
z0 = ajuste32[3]
erro_z0 = np.sqrt(mcov32[3][3])
print('Ajuste (anti-Helmholtz):')
print('Corrente = {}A'.format(M((I,erro_I))))
print('Raio a = {}m'.format(M((a,erro_a))))
print('Distância b = {}m'.format(M((b,erro_b))))
print('Offset z0 = {}m'.format(M((z0,erro_z0))))

plt.figure(dpi=300)
tz = 1.05*np.linspace(-b,b,300)
plt.plot(1e2*tz,1e3*antihelmholtz(tz,I,a,b,z0),label='Ajuste',zorder=0)
plt.errorbar(1e2*z,B*1e3,erroB*1e3,z*0+0.1e-2,'.k',label='Dados experimentais',zorder=1)
plt.legend()
plt.title('Par de bobinas anti-Helmholtz')
plt.xlabel("Posição (cm)")
plt.ylabel("Campo magnético (mT)")
plt.savefig('pratica4/figuras/antihelmholtz.png',bbox_inches='tight')

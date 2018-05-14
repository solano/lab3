import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from LabIFSC import M
from erros_mult import *

mu_0 = np.pi*4e-7   # valor exato
N = M((760,0))
L = M((15.2e-2,.05e-3))
n = N/L

dados1 = np.loadtxt('pratica4/dados/calibração.dat').T
Vfundo = M((4.7e-3,err_v200m(4.7e-3)))
Vh, I = dados1
erroVh = erro_array(Vh,err_v2)
Vh = Vh-Vfundo.nominal
erroVh = np.array(erroVh)+Vfundo.incerteza
erroI = erro_array(I,err_a200m)
B = mu_0*n.nominal*I
erroB=[]
for i in I:
    i = M((i,err_a200m(i)))
    erroB.append((mu_0*n*i).incerteza)

ajuste1 = stats.linregress(B,Vh)
slope1,intercept1 = ajuste1[:2]
see = ajuste1[-1]
mv = Vh.mean()
sv2 = ((Vh-mv)**2).sum()
sd_intercept = see * np.sqrt(1./len(Vh) + mv*mv/sv2)
sd_slope = see * np.sqrt(1./sv2)

K = M((slope1,sd_slope))
print(slope1,sd_slope)
intercept = M((intercept1,sd_intercept))

print("Valor esperado para K em torno de 280\nK = {} V/T".format(K))
print("Intercept =",intercept,'V')

plt.figure(dpi=300)
plt.errorbar(B*1e3,Vh,erroVh,erroB,fmt='.k',label="Dados experimentais")
Bn = np.linspace(0,1.3e-3,3)
plt.plot(Bn*1e3,slope1*Bn+intercept1,label='Ajuste linear')
plt.legend(loc='best')
plt.title('Calibração da sonda Hall')
plt.xlim(0,1.3)
plt.ylim(0,.35)
plt.ylabel("Tensão Hall (V)")
plt.xlabel("Campo magnético (mT)")
plt.savefig('pratica4/figuras/calibração.png',bbox_inches='tight')

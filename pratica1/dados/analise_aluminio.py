from matplotlib import pyplot as plt
import numpy as np
from scipy import stats,optimize
from IPython.display import display, Math, Latex
from LabIFSC import M

#Resistividade (sigma) esperada: 2.92e−8
i = M((0.500,0.001)) # corrente em amperes

espessura = M((0.075e-3, 0.005e-3))
larguraA = M((29.75e-3, 0.05e-3))
larguraB = M((20.45e-3, 0.05e-3))
larguraC = M((10.20e-3, 0.05e-3))
areaA = larguraA*espessura # área de seção, região A
areaB = larguraB*espessura # área de seção, região B
areaC = larguraC*espessura # área de seção, região C

data1, data2, data3 = [np.loadtxt(f"data/aluminio_{i}.dat").T for i in range(1,4)]
r = stats.linregress(data1[0],data1[1])
EA = M((r[0],r[4]))
r = stats.linregress(data2[0],data2[1])
EB = M((r[0],r[4]))
r = stats.linregress(data3[0],data3[1])
EC = M((r[0],r[4]))
plt.figure(dpi=100)
plt.plot(data1[0],data1[1],'.',
    data2[0],data2[1],'.',
    data3[0],data3[1],'.')
plt.legend(['Região A', 'Região B', 'Região C'])
plt.title("Análise do alumínio")
plt.xlabel('Posição (m)')
plt.ylabel('Diferença de potencial (V)')
display(Math(r'E=-\dfrac{\mathrm{d}V}{\mathrm{d}x}'))
print(f"EA = {EA:txt,ifsc,-3} V/m")
print(f"EB = {EB:txt,ifsc,-3} V/m")
print(f"EC = {EC:txt,ifsc,-3} V/m")

sigmaA = i/(EA*areaA)
sigmaB = i/(EB*areaB)
sigmaC = i/(EC*areaC)
sigma = (sigmaA+sigmaB+sigmaC)/3
dpsigma = np.std(np.array([sigmaA.nominal,sigmaB.nominal,sigmaC.nominal]), ddof=1)
print('Condutividade: {:txt,ifsc,7}, {:txt,ifsc,7}, {:txt,ifsc,7}\nMédia = {:txt,ifsc,7} DP = {:.1e}'.format(sigmaA,sigmaB,sigmaC,sigma,dpsigma))

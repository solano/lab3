import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from LabIFSC import M

dados = np.loadtxt('pratica2/data/fonte.dat')
V_i, V_c = dados.T

erro_voltm = lambda x: 0.003+0.005*abs(x) #veja wheatstone.dat
erro_V_i = np.array(list(map(erro_voltm,V_i)))
erro_V_c = np.array(list(map(erro_voltm,V_c)))

r_e = M(4.6, 0.5+0.008*4.6) # medida feita no lab
i,Pu,R = [],[],[]
for k in range(len(V_i)):
    vi = M(V_i[k], erro_V_i[k])
    vc = M(V_c[k], erro_V_c[k])
    i_ = vi/r_e
    i.append(i_)
    Pu.append((vi+vc)*i_)
    R.append(vc/i_)
erro_R = np.array([r.incerteza for r in R])
R = np.array([r.nominal for r in R])
erro_Pu = np.array([pu.incerteza for pu in Pu])
Pu = np.array([pu.nominal for pu in Pu])
erro_i = np.array([i_.incerteza for i_ in i])
i = np.array([i_.nominal for i_ in i])

# ajuste
def pot_util(R,r_i,fem):
    i = fem/(r_e.nominal+r_i+R)
    return (r_e.nominal+R)*i*i
ajuste = optimize.curve_fit(pot_util,R,Pu,[47,1.5])

r_i = M(ajuste[0][0],np.sqrt(ajuste[1][0,0]))
fem = M(ajuste[0][1],np.sqrt(ajuste[1][1,1]))
Rx = np.linspace(0,max(R),1001)
i_aj = fem.nominal/(r_e.nominal+r_i.nominal+Rx)
Pu_aj = (r_e.nominal+Rx)*i_aj*i_aj
Pt_aj = fem.nominal*i_aj
Pd_aj = Pt_aj-Pu_aj
eta_aj = Pu_aj/Pt_aj

# PLOTAR TUDO EM FUNÇÃO DE x = R + r_e
x = R + r_e.nominal
xx = Rx + r_e.nominal
fig=plt.figure(dpi=100)
plt.plot(xx,Pu_aj,color='royalblue',label='Potência útil')
plt.plot(x,Pu,'.r',color='royalblue')
plt.plot(xx,Pd_aj,color='orange',label='Potência dissipada')
plt.plot(xx,Pt_aj,color='tomato',label='Potência total')
plt.plot(x,x*0-10,'--k',label='Eficiência') #só pra aparecer na legenda
plt.ylim([0,0.04])
plt.xlim([0,820])
#plt.axis([0,200,0,0.02])
plt.xlabel('Resistência total $r_e + R$ ($\Omega$)')
plt.ylabel('Potência (W)')
plt.legend(loc=(0.6,0.4))
plt.twinx()
plt.plot(xx,eta_aj,'--k')
plt.ylabel('Eficiência')
plt.ylim([0,1])
plt.title('Análise da fonte não-ideal')
plt.show()

# PLOTAR SÓ A POTÊNCIA ÚTIL
plt.figure(dpi=100)
plt.plot(xx,Pu_aj,zorder=1)
#plt.errorbar(x,Pu,erro_Pu,erro_R+r_e.incerteza,fmt='.k',elinewidth=0.5)
plt.plot(x,Pu,'.k')
#plt.xticks([r_i]+list(range(0,301,30)),['$r_i$']+list(range(0,301,30)))
plt.xlim([0,100])
plt.ylim([0.007,0.013])
plt.xlabel('Resistência total $r_e + R$ ($\Omega$)')
plt.ylabel('Potência útil (W)')
plt.title('Análise da fonte não-ideal')
plt.show()

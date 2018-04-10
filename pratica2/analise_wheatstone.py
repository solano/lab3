import matplotlib.pyplot as plt
import numpy as np
from LabIFSC import M   # esse módulo tá bugado :/
from scipy import optimize

print('TODOS OS TESTES DE EQUIVALÊNCIA ESTÃO BUGADOS, TESTE NA MÃO')

dados = np.loadtxt('pratica2/data/wheatstone.dat')
Vp, i = dados.T
Vp = -Vp

erro_voltm = lambda x: 0.003+0.005*abs(x)
erro_Vp = np.array(list(map(erro_voltm, Vp)))
erro_ampm = lambda x: 0.1e-3+0.008*abs(x)
erro_i = np.array(list(map(erro_ampm, i)))

# valores constam em wheatstone.dat
Vf = M(5.01,0.06)
R1, R2, R3 = M(671,5), M(666,5), M(470,4)
Rx_eq_prev = R2*R3/R1
print('R1, R2, R3:',R1,R2,R3)

# análise
#mu = []
#for x,xerr in zip(Vp,erro_Vp):
#    mu.append(M(x,xerr)/Vf)
l = R2/(R1+R2)

Rx = []
for corrente,err_corrente in zip(i,erro_i):
    Req = Vf/M(corrente,err_corrente)
    Rx.append(((R1+R2)*(R3-Req)-R3*Req)/(Req-R1-R2))

#erro_mu = np.array([m.incerteza for m in mu])
#mu = np.array([m.nominal for m in mu])
erro_Rx = np.array([r.incerteza for r in Rx])
Rx = np.array([r.nominal for r in Rx])

func = lambda r,l,r3,vf: (l-r/(r+r3))*vf
ajuste = optimize.curve_fit(func,Rx,Vp,[l.nominal,R3.nominal,Vf.nominal],erro_Vp)
l_ajuste = M(ajuste[0][0],np.sqrt(ajuste[1][0,0]))
R3_ajuste = M(ajuste[0][1],np.sqrt(ajuste[1][1,1]))
Vf_ajuste = M(ajuste[0][2],np.sqrt(ajuste[1][2,2]))
print('R3 do ajuste =',R3_ajuste,'EQ' if R3_ajuste==R3 else 'NEQ')
print('Vf do voltímetro =',Vf)
print('Vf do ajuste =',Vf_ajuste,'EQ' if Vf_ajuste==Vf else 'NEQ')
print('l do voltímetro =',l)
print('l do ajuste =',l_ajuste,'EQ' if l_ajuste==l else 'NEQ')
func2 = lambda r: func(r,l_ajuste.nominal,R3_ajuste.nominal,Vf_ajuste.nominal)

Rx_eq_aj = l_ajuste*R3_ajuste/(1-l_ajuste)
# estimativa do erro que vem de Rx
Rx_eq_aj.incerteza = max(Rx_eq_aj.incerteza,
      erro_Rx[(erro_Rx-Rx_eq_aj.nominal).argmin()])
print('Resistência Rx de equilíbrio prevista:', Rx_eq_prev)
print('Resistência obtida no ajuste:',Rx_eq_aj)
print('EQUIVALENTES' if Rx_eq_aj==Rx_eq_prev else 'NÃO EQUIVALENTES')

# plot
#plt.figure(dpi=500)
plt.plot(Rx,Rx*0,'--k',zorder=0)
plt.plot(Rx,func2(Rx),label='Ajuste',zorder=1)
#plt.errorbar(Rx,Vp,yerr=erro_Vp,xerr=erro_Rx,fmt=".",color='g',elinewidth=0.5,label='Dados')
plt.errorbar(Rx,Vp,yerr=erro_Vp,fmt=".",color='g',label='Dados')
plt.legend()
plt.xlabel('Resistência do potenciômetro (Ω)')
plt.ylabel('Tensão na ponte (V)')
#plt.axis([490,543,-0.07,0.07])
#plt.title('Ponte de Wheatstone (gráfico ampliado)')
#plt.savefig('pratica2/graficos/wheatstone-ampliado.png',bbox_inches='tight')
plt.title('Ponte de Wheatstone')
#plt.savefig('pratica2/graficos/wheatstone.png',bbox_inches='tight')
#plt.savefig('pratica2/graficos/wheatstone-xerr.png',bbox_inches='tight')

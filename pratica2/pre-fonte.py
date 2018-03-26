import matplotlib.pyplot as plt
import numpy as np

# Simulação dos dados esperados no experimento da fonte não-ideal
eps = 5       # força eletromotriz = 5 V (fixa)
re = 4.7      # resistor
ri = 70       # resistência interna da fonte

R = np.linspace(0,1000,1000) # potenciômetro

i = eps/(re+ri+R)
Vi = re*i
Vc = R*i

Pu = (Vi+Vc)*i
Pt = eps*i
Pd = Pt-Pu
eta = Pu/Pt

# parte (5)
fig = plt.figure(dpi=80)
#fig = plt.figure(dpi=500)
ax = fig.add_subplot(1,1,1)
ax.plot(re+R, Pu)
ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
ax.set_title("Simulação ($\\varepsilon$ = 5 V, $r_i$ = 70 $\\Omega$)")
ax.set_xlabel("$R + r_e$ ($\\Omega$)")
ax.set_ylabel("$P_u$ (W)")
#fig.savefig('graficos/pot-util-fonte.png',bbox_inches='tight')

# parte (6)
fig2 = plt.figure(dpi=80)
#fig2 = plt.figure(dpi=500)
ax = fig2.add_subplot(1,1,1)
ax.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
ax.plot(re+R, Pt, re+R, Pd, re+R, Pu, [500,444],[-1,-1],'--k')
ax.set_title("Simulação ($\\varepsilon$ = 5 V, $r_i$ = 70 $\\Omega$)")
ax.set_xlabel("$R + r_e$ ($\\Omega$)")
ax.set_ylabel("Potência (W)")
ax.set_ylim([0,25e-2])
ax.legend(["Potência total","Potência dissipada","Potência útil","Eficiência"],loc=(0.6,0.4))

ax2 = ax.twinx()
ax2.plot(re+R, eta, '--k')
ax2.set_ylim([0,1])
ax2.set_ylabel("Eficiência")

#fig2.savefig('graficos/potencias-eficiencia-fonte.png',bbox_inches='tight')

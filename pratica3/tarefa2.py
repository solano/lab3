import numpy as np
import matplotlib.pyplot as plt


Capacitor = [100e-6,10e-6,220e-6]


# Componentes que serão usados no experimento -------------------
Rvolt = 10e6    # Resistencia interna do voltimetro
paralelo = lambda a,b : a*b/(a+b)

R = 100e3   # Resistência dada no enunciado da tarefa 1
R = paralelo(R,Rvolt)
C1 = Capacitor[0]*Capacitor[1]/(Capacitor[0]+Capacitor[1])   # Associação em paralelo
C2 = Capacitor[0]+Capacitor[1] #
C3 = Capacitor[0]*(Capacitor[1]+Capacitor[2])/(Capacitor[0]+Capacitor[1]+Capacitor[2])  #
# --------------------------------------------------------------- v_max
v_max = 5   # Tensão máxima no capacitor (Calculada no ohmimetro)
t_max = 30 # Tempo máximo que serão pegos os dados.
t = np.linspace(0,t_max,100)
v = lambda t,C : v_max*(1-np.exp(-t/(R*C)))    # Função tensão por tempo
# Plot das curvas esperadas -------------------------------------
plt.figure(dpi=100)
plt.title(r"Associações de capacitores, $R_i=10M\Omega$")
# Eixo vertical
plt.ylim([0,v_max+1])
plt.yticks([0,v_max], ["0", r"$v_0$"])
plt.plot([0,t_max], [v_max, v_max], 'k--')
plt.ylabel("ddp do capacitor (v)")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xticks([R*C1, R*C2, R*C3], ["{:.1f}".format(R*C1), "{:.1f}".format(R*C2), "{:.1f}".format(R*C3)])
plt.xlabel("Tempo (s)")
# Série
plt.plot(t,v(t,C1), label=r"Série: ${:.2f}\mu F$".format(C1*1e6))
plt.plot([R*C1, R*C1], [0,v(R*C1, C1)], '--', color="royalblue")
# Mista
plt.plot(t,v(t,C3), label=r"Mista: ${:.2f}\mu F$".format(C3*1e6))
plt.plot([R*C3, R*C3], [0,v(R*C3, C3)], '--', color="darkorange")
# Paralelo
plt.plot(t,v(t,C2), label=r"Paralela: ${:.0f}\mu F$".format(C2*1e6))
plt.plot([R*C2, R*C2], [0,v(R*C2, C2)], '--', color="forestgreen")

plt.legend(loc=0)
plt.savefig("pratica3/graph/(2)curva_capacitores.png")
# Regressão linear para encontrar a capacitância ---------------------
plt.figure(dpi=100)
plt.title(r"$\ln(v_0-v(t))=\ln(v_0)-t/RC$")
# Eixo vertical
plt.ylabel(r"$v_0-v(t)$")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xlabel("Tempo (s)")
# Capacitor de 1e-6 F
plt.semilogy(t,v_max-v(t,C1), label=r"Série: ${:.2f}\mu F$".format(C1*1e6))
plt.semilogy(t,v_max-v(t,C3), label=r"Mista: ${:.2f}\mu F$".format(C3*1e6))
plt.semilogy(t,v_max-v(t,C2), label=r"Paralela: ${:.0f}\mu F$".format(C2*1e6))

plt.legend(loc=0)
plt.savefig("pratica3/graph/(2)semilogy_capacitancia.png")

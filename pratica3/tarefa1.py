import numpy as np
import matplotlib.pyplot as plt

# Componentes que serão usados no experimento -------------------
Rvolt = 10e6    # Resistencia interna do voltimetro
paralelo = lambda a,b : a*b/(a+b)

R = 100e3   # Resistência dada no enunciado da tarefa 1
R = paralelo(R,Rvolt)
C1 = 10e-6   # Capacitores que serão usados na prática
C2 = 100e-6 #
C3 = 220e-6  #
# --------------------------------------------------------------- v_max
v_max = 5   # Tensão máxima no capacitor (Calculada no ohmimetro)
t_max = 30 # Tempo máximo que serão pegos os dados.
t = np.linspace(0,t_max,100)
v = lambda t,C : v_max*(1-np.exp(-t/(R*C)))    # Função tensão por tempo
# Plot das curvas esperadas -------------------------------------
plt.figure(dpi=100)
plt.title(r"Curva de carga de capacitores, $R_i=10M\Omega$")
# Eixo vertical
plt.ylim([0,v_max+1])
plt.yticks([0,v_max])
plt.plot([0,t_max], [v_max, v_max], 'k--')
plt.ylabel("ddp do capacitor (v)")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xticks([R*C1, R*C2, R*C3], ["{:.1f}".format(R*C1), "{:.1f}".format(R*C2), "{:.1f}".format(R*C3)])
plt.xlabel("Tempo (s)")
# Capacitor de 1e-6 F
plt.plot(t,v(t,C1), label=r"${:.0f}\mu F$".format(C1*1e6))
plt.plot([R*C1, R*C1], [0,v(R*C1, C1)], '--', color="royalblue")
# Capacitor de 4.7e-6 F
plt.plot(t,v(t,C2), label=r"${:.0f}\mu F$".format(C2*1e6))
plt.plot([R*C2, R*C2], [0,v(R*C2, C2)], '--', color="darkorange")
# Capacitor de 10e-6 F
plt.plot(t,v(t,C3), label=r"${:.0f}\mu F$".format(C3*1e6))
plt.plot([R*C3, R*C3], [0,v(R*C3, C3)], '--', color="forestgreen")
plt.legend(loc=0)
plt.savefig("pratica3/graph/(1)curva_capacitores.png")
# Regressão linear para encontrar a capacitância ---------------------
plt.figure(dpi=100)
plt.title("Linearização da curva de carga")

# Eixo vertical
plt.ylabel(r"$v_0-v(t)$")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xlabel("Tempo (s)")
# Capacitor de 1e-6 F
plt.semilogy(t,v_max-v(t,C1), label=r"${:.0f}\mu F$".format(C1*1e6))
# Capacitor de 4.7e-6 F
plt.plot(t,v_max-v(t,C2), label=r"${:.0f}\mu F$".format(C2*1e6))
# Capacitor de 10e-6 F
plt.plot(t,v_max-v(t,C3), label=r"${:.0f}\mu F$".format(C3*1e6))
plt.legend(loc=0)
plt.savefig("pratica3/graph/(1)semilogy_capacitancia.png")

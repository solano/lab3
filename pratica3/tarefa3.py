import numpy as np
import matplotlib.pyplot as plt

# Componentes que serão usados no experimento -------------------
Rvolt = 10e6    # Resistencia interna do voltimetro
paralelo = lambda a,b : a*b/(a+b)
R1_l = 200e3
R2_l = 100e3   # Resistência padrão
R3_l = 68e3
R4_l = 47e3
R5_l = 22e3
C = 100e-6   # Capacitor padrão
# Resistência equivalente em paralelo com a resistencia interna do voltimetro
R1 = paralelo(Rvolt, R1_l)
R2 = paralelo(Rvolt, R2_l)
R3 = paralelo(Rvolt, R3_l)
R4 = paralelo(Rvolt, R4_l)
R5 = paralelo(Rvolt, R5_l)



# --------------------------------------------------------------- v_max
v_max = 10   # Tensão máxima no capacitor (Calculada no ohmimetro)
t_max = 30 # Tempo máximo que serão pegos os dados.
t = np.linspace(0,t_max,100)
v = lambda t,R : v_max*(np.exp(-t/(R*C)))    # Função tensão por tempo
# Plot das curvas esperadas -------------------------------------
plt.figure(dpi=100)
plt.title(r"R variável, $C=100\mu F$, $R_i=10M\Omega$")
# Eixo vertical
plt.ylim([0,v_max+1])
plt.yticks([0,v_max], ["0", r"$v_0$"])
plt.ylabel("ddp do capacitor (v)")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xticks([R1*C, R2*C, R3*C, R4*C, R5*C], ["{:.1f}".format(R1*C), "{:.1f}".format(R2*C),"{:.1f}".format(R3*C),"{:.1f}".format(R4*C),"{:.1f}".format(R5*C)])
plt.xlabel("Tempo (s)")


# R1C
plt.plot(t,v(t,R1), label=r"${:.0f} k \Omega$".format(R1_l*1e-3))
plt.plot([R1*C, R1*C], [0,v(R1*C, R1)], '--', color="royalblue")
# R2C
plt.plot(t,v(t,R2), label=r"${:.0f} k \Omega$".format(R2_l*1e-3))
plt.plot([R2*C, R2*C], [0,v(R2*C, R2)], '--', color="darkorange")
# R3C
plt.plot(t,v(t,R3), label=r"${:.0f} k \Omega$".format(R3_l*1e-3))
plt.plot([R3*C, R3*C], [0,v(R3*C, R3)], '--', color="forestgreen")
# R4C
plt.plot(t,v(t,R4), label=r"${:.0f} k \Omega$".format(R4_l*1e-3))
plt.plot([R4*C, R4*C], [0,v(R4*C, R4)], '--', color="crimson")
# R3C
plt.plot(t,v(t,R5), label=r"${:.0f} k \Omega$".format(R5_l*1e-3))
plt.plot([R5*C, R5*C], [0,v(R5*C, R5)], '--', color="mediumpurple")


plt.legend(loc=0)
plt.savefig("pratica3/graph/(3)curva_descarga.png")
# Regressão linear para encontrar a capacitância ---------------------
plt.figure(dpi=100)
plt.title(r"$\ln(v(t))=\ln(v_0)-t/RC$")
# Eixo vertical
plt.ylabel(r"$v(t)$")
# Eixo horizontal
plt.xlim([0,t_max])
plt.xlabel("Tempo (s)")
# Capacitor de 1e-6 F
plt.semilogy(t,v(t,R1), label=r"${:.0f} k \Omega$".format(R1_l*1e-3))
plt.semilogy(t,v(t,R2), label=r"${:.0f} k \Omega$".format(R2_l*1e-3))
plt.semilogy(t,v(t,R3), label=r"${:.0f} k \Omega$".format(R3_l*1e-3))
plt.semilogy(t,v(t,R4), label=r"${:.0f} k \Omega$".format(R4_l*1e-3))
plt.semilogy(t,v(t,R5), label=r"${:.0f} k \Omega$".format(R5_l*1e-3))
plt.legend(loc=0)
plt.savefig("pratica3/graph/(3)semilogy_descarga.png")

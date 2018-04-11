import numpy as np
import matplotlib.pyplot as plt

C1 = 100e-6
U = lambda C2:1+C2/C1

r = np.linspace(0, 200e-6)
plt.xlim([0,2])
plt.ylim([0,3])
plt.title(r"Relação de energia entre $C_1=10\mu F$ e $C_2$ variável")
plt.ylabel(r"$U_i/U_f$")
plt.xlabel(r"C2/C1")
plt.plot(r/C1,U(r))
plt.savefig("pratica3/graph/(4)energia.png", dpi=300)

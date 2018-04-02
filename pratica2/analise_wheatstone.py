# $$ \frac{1}{R_{eq}} = \left[\frac{1}{R_1+R_2} + \frac{1}{R_3+R_x}\right]^{-1} $$
# Portanto, segundo o Wolfram,
# $$ R_x = \frac{R_1 + R_2 + R_3 - (R_1+R_2) R_3 R_{eq}}{(R_1 + R_2) R_{eq} - 1} $$
# (será se tá certo mesmo? e as unidades?)

import matplotlib.pyplot as plt
import numpy as np

dados = np.loadtxt('dados/wheatstone.dat')
Vp, i = dados.T

# substituir com valores reais medidos
Vf = 5
R1, R2, R3 = 680, 680, 470

# análise
Req = Vf/i
Rx = (R1 + R2 + R3 - (R1+R2)*R3*Req)/((R1+R2)*Req-1)

# plot
plt.plot(Rx,Vp)

# Análise referente à tarefa 3 (circuito RL)

from errolab import *
from erros_mult import *

_L1 = 46.2e-3           # 1000 voltas
L1 = unc.ufloat(_L1,err_i200m(_L1))
_r1 = 14.4
r1 = unc.ufloat(_r1,err_o200(_r1))

_L2 = 14.6e-3            # 2100 voltas
L2 = unc.ufloat(_L2,err_i200m(_L2))
_r2 = 201
r2 = unc.ufloat(_r2,err_o2k(_r2))

_R = 463
R = unc.ufloat(_R,err_o2k(_R))

f = unc.ufloat(1.481e3, 1)
w = 2*np.pi*f
T = 1/f

print(f"f = {f} Hz\nR = {R} ohms\nL1 = {L1*1e3} mH\nr1 = {r1} ohms\nL2 = {L2*1e3} mH\nr2 = {r2} ohms\n\n")

# %%

print('ANÁLISE DA FASE\n')
escdt1, quaddt1 = 50e-6, 2.4
escVr1, quadVr1 = 1, 2
escVl1, quadVl1 = 5, 3+3.3/5
dt1 = unc.ufloat(escdt1*quaddt1, escdt1/10)
Vr1 = unc.ufloat(escVr1*quadVr1, escVr1/10)/2
Vl1 = unc.ufloat(escVl1*quadVl1, escVl1/10)/2

escdt2, quaddt2 = 50e-6, 1
escVr2, quadVr2 = 1, 2.6
escVl2, quadVl2 = 5, 2+4.7/5
dt2 = unc.ufloat(escdt2*quaddt2, escdt2/10)
Vr2 = unc.ufloat(escVr2*quadVr2, escVr2/10)/2
Vl2 = unc.ufloat(escVl2*quadVl2, escVl2/10)/2

phiteo1 = unp.arctan(w*L1/r1)
phiteo2 = unp.arctan(w*L2/r2)
phi1 = w*dt1
phi2 = w*dt2

print(f"phi1 = {phi1} rad, esperado {phiteo1} rad",
    "equivalentes" if equiv(phiteo1,phi1) else "não equivalentes")
print(f"phi2 = {phi2} rad, esperado {phiteo2} rad",
    "equivalentes" if equiv(phiteo2,phi2) else "não equivalentes")

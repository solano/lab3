# Análise referente à tarefa 1 (circuito RC)

from errolab import *

f = unc.ufloat(31298, 1)

escVr = 2
quadVr = 5
escVc = 1
quadVc = 4.7
escdt = 5e-6
quaddt = 1.5

Vr = unc.ufloat(escVr*quadVr, escVr/10)/2
Vc = unc.ufloat(escVc*quadVc, escVc/10)/2
dt = unc.ufloat(escdt*quaddt, escdt/10)

T = 1/f

print('T = {} s, f = {} Hz'.format(T,f))
print(f'Vr = {Vr} V, Vc = {Vc} V, dt = {dt} s')
print(f'\ndt/T = {dt/T} (esperado = 0.25)')
print('equivalente' if equiv(dt/T,unc.ufloat(1/4,0)) else \
      'não equivalente')

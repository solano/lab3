from math import pi
from LabIFSC import M
from erros_mult import *

mu_0 = 4e-7*pi

# esse valor vem de analise_calibracao.py
K = M((265.653591676,0.641925750322))

N = M((760,0))
L = M((15.2e-2,.05e-3))
n = N/L

R = M((10.1,err_o200(10.1))) # resistência ligada ao solenoide
phi = 0 # fase (segundos), valor esperado = 0
Vh = M((0.7,0.05)) # tensão Hall medida no osciloscópio
B = Vh/K # amplitude do campo magnético
Vr = M((3.3,0.05)) # tensão do gerador de funções (aplicada no resistor)
I = Vr/R # amplitude de corrente
B0 = mu_0*I*n # valor esperado pro B, aproximação de solenoide longo
print("Amplitude do campo: {} mT (esperada), {} mT (medida)".format(B0*1e3,B*1e3))
print('equivalentes' if B0==B else 'não equivalentes')
print('Medidas:')
print('R = {}ohms'.format(R))

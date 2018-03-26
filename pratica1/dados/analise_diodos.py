from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize
from IPython.display import display, Math, Latex
from LabIFSC import M


e = M((1.6021762e-19, 0.0000001e-19))   # Carga fundamental
kb = M((1.3806485e-23, 0.0000001e-23))  # Constante de boltzmann
k = e/kb                                # 'k' da equação de Shockley
h = M((6.62607004e-34, 0.00000001e-34)) # Constante de Planck
#la = np.linspace(450e-9, 495e-9,50)    # Comprimento de onda luz azul (466)
la = M((466e-9, 1e-9))
#lv = np.linspace(495e-9, 570e-9,50)    # Comprimento de onda luz verde (575)
lv = M((575e-9, 1e-9))
c = M((299792458,0))                    # Velocidade da luz

T = M((295,1))                          # Temperatura ambiente
R = M((47.4,0.1))                       # Resistência

# Chutes default pros valores
I0 = M((1e-9,0))
k = e/(kb*2)

i_shockley = lambda x,i0,k: x*i0*(np.exp(k*x/T)-1)/(x+R*i0*(np.exp(k*x/T)-1))

#####################################################################
########  MODELAGEM EXATA DO CIRCUITO - NÃO VAMOS USAR ##############
#####################################################################

# Sejam V1 a tensão no diodo, V2 a tensão no resistor. Então V = V1+V2
# Vou calcular V1 (tensão no diodo) a partir de V numericamente
# Equação: V = V1 + V2 = V1 + R*I0*(exp(k*V1/T)-1)
@np.vectorize
def V1(V, I0, k):
    func = lambda _V1: -V + _V1 + R*I0*(np.exp(k*_V1/T) - 1)
    deriv = lambda _V1: 1 + (R*I0*k/T) * np.exp(k*_V1/T)
    return optimize.newton(func,0,deriv,maxiter=150)

# corrente no circuito
i_circ = lambda V, I0, k: i_shockley(V1(V,I0,k),I0.nominal,k.nominal)

#domV = np.linspace(0,2.3,50)
#plt.plot(domV, i_circ(domV,I0,k))
#plt.xlabel('Tensão da fonte (V)')
#plt.ylabel('Corrente no circuito (A)')
#plt.savefig('corrente_tensao.png')
#plt.show()

########################################################################
######################## FIM DA MODELAGEM EXATA ########################
########################################################################

############# ANÁLISE DE FATO VEM AGORA ###############

# A ideia é fazer um ajuste linear na parte dos dados depois do 'joelho',
# e encontrar a tensão Vt onde a reta encontra o eixo das tensões. Vamos
# considerar essa tensão, no caso dos LEDs, como aquela em que eles acen-
# dem, pra encontrar a constante de Planck. Pro diodo vamos refazer o
# experimento de outra forma.

led1 = np.loadtxt('data/led_1.dat').transpose()
led2 = np.loadtxt('data/led_2.dat').transpose()

linear = lambda x,a,b: a*x+b

# Ajuste linear para encontrar as tensões V1 e V2 em que os leds
# azul e verde (respectivamente) começam a funcionar
# O ajuste começa depois do 'joelho'
limled1, limled2 = 11, 10 # encontrados graficamente
res, pcov = optimize.curve_fit(linear,led1[1][limled1:],
            led1[0][limled1:],p0=[R.nominal,0])
V1 = M((res[1],np.sqrt(pcov[1,1])))

res, pcov = optimize.curve_fit(linear,led2[1][limled2:],
            led2[0][limled2:],p0=[R.nominal,0])
V2 = M((res[1],np.sqrt(pcov[1,1])))
h1,h2 = la*V1*e/c, lv*V2*e/c
print(f"V1 = {V1}, V2 = {V2}\nh1 = {h1:txt,ifsc,-34}, h2 = {h2:txt,ifsc,-34}")

plt.plot(led1[0],led1[1],'-b',led2[0],led2[1],'-g')
# Mostra em destaque os pontos que foram usados no ajuste
plt.plot(led1[0][limled1:],led1[1][limled1:],'ob',
    led2[0][limled2:],led2[1][limled2:],'og')
plt.legend(['LED azul','LED verde'])
plt.xlabel('Tensão aplicada (V)')
plt.ylabel('Corrente no circuito (A)')
#plt.savefig('graficos/leds.png')
plt.show()

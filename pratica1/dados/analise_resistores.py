from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize
from IPython.display import display, Math, Latex
from LabIFSC import M

#47 nom == 47.4
#100 nom == 109.1
#100 nom == 98.0

GERAR_GRAFICOS = False

resistores = {'resistor_1':('Resistor de 10 kΩ', M((10.09e3,0.01e3))),
            'resistor_2':('Resistor de 1 kΩ', M((1.002e3,0.001e3))),
            'resistor_3':('Resistor de 100 Ω', M((105.2,0.1))),
            'associacao_1':('Associação em série', M((221.0,0.1))),
            'associacao_2':('Associação em paralelo', M((32.0,0.1))),
            'associacao_3':('Associação mista', M((100.4,0.1)))}

def i_ohm(x,a,b,k):return a*x**k+b  # i = u/r

erros = lambda pcov: np.sqrt(np.diag(pcov))

display(Math(r'I = aU^k+b'))
for resistor in resistores:
    if GERAR_GRAFICOS: plt.figure(figsize=(3.5,2.5),dpi=200)
    else: plt.figure(figsize=(3.5,2.5),dpi=100)

    nome, R = resistores[resistor]
    data = np.loadtxt(f'data/{resistor}.dat').T

    params, pcov = optimize.curve_fit(i_ohm, data[0], data[1], p0=[1/R.nominal,0,1])
    err = erros(pcov)
    a, b, k = map(M, zip(params,err))
    #a,b,k = tuple(params)

    plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))
    #plt.scatter(data[0], data[1])
    plt.plot(data[0], i_ohm(data[0], params[0], params[1],params[2]),
            data[0],data[1],'ok')
    plt.xlabel('Tensão aplicada (V)')
    plt.ylabel('Corrente (A)')
    plt.title(f'{nome}')
    plt.axis([0,data[0][-1]+0.2,0,data[1][-1]+0.05*data[1][-1]])
    if GERAR_GRAFICOS:
        plt.savefig(f'graficos/{resistor}.png',bbox_inches='tight')
    print(f"{nome} ({resistor}):")
    print("a = {:txt,ifsc,-6}, 1/R = {:txt,ifsc,-6}, {}\nb = {:txt,ifsc,-3}, k = {}".format(a, M((1,0))/R,
    ('equivalentes' if a==M((1,0))/R else 'não equiv'), b, k))
    print('\n')

import numpy as np
from LabIFSC import M

data = np.loadtxt("data/grafite.dat").T

r = M((np.average(data),np.std(data,ddof=1))) # resistência média dos retangulinhos

################################
# Bastão de grafite
# Resistencia = 6.1 Ohms
# Diametros = 2.47 mm +-(0.01mm)
# Comprimento = 5.70 cm +-(0.01cm)
###############################
R = M((6.1,0.1))
D = M((2.47e-3,0.01e-3))
Lb = M((5.70e-2,0.01e-2))

# resistividade
rho = np.pi*D**2*R/(4*Lb)

# paralelepípedos
Lp = M((0.8e-2,0.05e-2)) # comprimento
a = M((0.2e-2,0.05e-2))  # largura

#espessura
e = rho*Lp/(a*r)

# Comprimento máximo de um paralelepípedo feito com esse bastão,
# tendo essa espessura e essa largura
comp = np.pi*D**2/(4*e*a)

print(f"Resistividade: {rho:txt,full,-5}S/m")
print(f"Espessura média: {e:txt,full,-10}m")
print(f"Comprimento máximo: {comp:txt,full,6}m")

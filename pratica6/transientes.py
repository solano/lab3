# Correntes transientes num circuito RLC

import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt

R = 40
L = 1e-4
C = 1e-8
w0 = 1/sqrt(L*C)

##### Amortecimento subcrítico ######

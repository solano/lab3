# feito pra funcionar com o pacote uncertainties

a = 3
import uncertainties as unc
from uncertainties import unumpy as unp
import numpy as np

# equivalência de duas grandezas
# NOTA: equiv(a,b) não é o mesmo que equiv(a-b,0)!
def equiv(a,b):
    if type(a)==np.ndarray:
        anom,bnom = unp.nominal_values(a),unp.nominal_values(b)
        aerr,berr = unp.std_devs(a),unp.std_devs(b)
    else:
        anom,bnom = a.nominal_value,b.nominal_value
        aerr,berr = a.std_dev,b.std_dev
    return np.abs(anom-bnom) < 2*(aerr+berr)

# Erro associado às medidas do multímetro em diferentes escalas
# Modelo Minipa ET-2082C

# voltímetro, corrente contínua
err_v200m = lambda x: 300e-6 + 0.5e-2*x
err_v2    = lambda x: 3e-3   + 0.5e-2*x
err_v20   = lambda x: 30e-3  + 0.5e-2*x
err_v200  = lambda x: 300e-3 + 0.5e-2*x
err_v1000 = lambda x: 10     + 2.0e-2*x

# amperímetro, corrente contínua
err_a2m   = lambda x: 10e-6  + 0.8e-2*x
err_a20m  = lambda x: 100e-6 + 0.8e-2*x
err_a200m = lambda x: 1e-3   + 1.2e-2*x
err_a20   = lambda x: 0.1    + 2.0e-2*x

# ohmímetro
err_o200  = lambda x: 0.5    + 0.8e-2*x
err_o2k   = lambda x: 3      + 0.8e-2*x
err_o20k  = lambda x: 30     + 0.8e-2*x
err_o200k = lambda x: 300    + 0.8e-2*x
err_o2M   = lambda x: 3e3    + 0.8e-2*x
err_o20M  = lambda x: 250e3  + 1.0e-2*x
err_o2000M= lambda x: 20e6   + 5.0e-2*(x-10e6)

# capacímetro
err_c20n  = lambda x: 0.2e-9 + 2.5e-2*x
err_c200n = lambda x: 2e-9   + 2.5e-2*x
err_c2u   = lambda x: 20e-9  + 2.5e-2*x
err_c20u  = lambda x: 200e-9 + 2.5e-2*x
err_c200u = lambda x: 2e-6   + 5.0e-2*x

def erro_array(arr, ferr):
    erros = []
    for medida in arr:
        erros.append(ferr(medida))
    return erros

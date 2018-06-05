# Erro associado às medidas do multímetro em diferentes escalas
# Modelo Minipa ET-2082C

def _funcao_erro(inf,sup,absol,rel):
    def f(x):
        if x<inf or x>sup:
            raise Exception('fora de escala: %f não está dentro de [%f,%f]'\
               %(x,inf,sup))
        return absol + rel*abs(x)
    return f

# voltímetro, corrente contínua
err_v200m = _funcao_erro(-200e-3,200e-3,300e-6,0.5e-2)
err_v2    = _funcao_erro(-2,     2,     3e-6,  0.5e-2)
err_v20   = _funcao_erro(-20,    20,    30e-6, 0.5e-2)
err_v200  = _funcao_erro(-200,   200,   300e-6,0.5e-2)
err_v1000 = _funcao_erro(-1000,  1000,  10,    2.0e-2)

# amperímetro, corrente contínua
err_a2m   = _funcao_erro(-2e-3,  2e-3,  10e-6, 0.8e-2)
err_a20m  = _funcao_erro(-20e-3, 20e-3, 100e-6,0.8e-2)
err_a200m = _funcao_erro(-0.2,   0.2,   1e-3,  1.2e-2)
err_a20   = _funcao_erro(-20,    20,    0.1,   2.0e-2)

# TODO: CONVERTER O RESTO DAS FUNÇÕES
# ohmímetro
err_o200  = lambda x: 0.5    + 0.8e-2*abs(x)
err_o2k   = lambda x: 3      + 0.8e-2*abs(x)
err_o20k  = lambda x: 30     + 0.8e-2*abs(x)
err_o200k = lambda x: 300    + 0.8e-2*abs(x)
err_o2M   = lambda x: 3e3    + 0.8e-2*abs(x)
err_o20M  = lambda x: 250e3  + 1.0e-2*abs(x)
err_o2000M= lambda x: 20e6   + 5.0e-2*(abs(x)-10e6)

# capacímetro
err_c20n  = lambda x: 0.2e-9 + 2.5e-2*abs(x)
err_c200n = lambda x: 2e-9   + 2.5e-2*abs(x)
err_c2u   = lambda x: 20e-9  + 2.5e-2*abs(x)
err_c20u  = lambda x: 200e-9 + 2.5e-2*abs(x)
err_c200u = lambda x: 2e-6   + 5.0e-2*abs(x)

# indutímetro (frequência de teste = 100 Hz)
err_2m    = lambda x: 30e-6  + 2.5e-2*abs(x)
err_20m   = lambda x: 300e-6 + 2.5e-2*abs(x)
err_200m  = lambda x: 3e-3   + 2.5e-2*abs(x)
err_2     = lambda x: 30e-3  + 2.5e-2*abs(x)
err_20    = lambda x: 300e-3 + 2.5e-2*abs(x)

def erro_array(arr, ferr):
    erros = []
    for medida in arr:
        erros.append(ferr(medida))
    return erros

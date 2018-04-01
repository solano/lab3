import json
from LabIFSC import M

N = 1 # 1 para o primeiro circuito, 2 para o segundo
data_open = open("data/kcl_{}.json".format(N)).read()
data_json = json.loads(data_open)




# RESISTENCIA --------------------------------------------------------
R_error = data_json["uncertainty"]["ohmeter"] # Incerteza do ohmimetro
R_nom = data_json["resistance"]["nominal"] # Resistencias nominais.
R_ohm = data_json["resistance"]["ohmeter"] # Resistências medidas com o ohmimetro.
for i in R_ohm: # Colocando incerteza em cada resistencia
    R_ohm[i] = M((R_ohm[i],R_error))
R_eq = lambda D: (D["r_0"]*D["r_1"]/(D["r_0"]+D["r_1"])+D["r_2"])*D["r_3"]/((D["r_0"]*D["r_1"]/(D["r_0"]+D["r_1"])+D["r_2"])+D["r_3"]) if N == 2 else D["r_0"]*D["r_1"]/(D["r_0"]+D["r_1"]) # Resistencia equivalente de todo o circuito; parâmetro é uma lista.


# TENSAO --------------------------------------------------------
V_error = data_json["uncertainty"]["voltage"] # Incerteza da fonte
V_nom = data_json["voltage"] # Tensao para calculos de valores nominais
V_ohm = M((V_nom,V_error)) # Tensao da fonte com incerteza


# CORRENTE --------------------------------------------------------
I_error = data_json["uncertainty"]["ammeter"] # Incerteza do amperimetro
I_nom = {} # Corrente do circuito
I_ohm = {} # Corrente obtida pelas resistências medidas no ohmimetro
I_amm = data_json["current"] # Correntes medidas no amperimetro
for i in I_amm: # Colocando incerteza nas correntes
    I_amm[i] = M((I_amm[i],I_error))



if N == 2 : # Calculo das correntes para a corrente do circuito 2
    I_nom["i_e"] = V_nom/R_eq(R_nom)
    I_nom["i_3"] = V_nom/R_nom["r_3"]
    I_nom["i_2"] = I_nom["i_e"] - I_nom["i_3"]
    I_nom["i_1"] = I_nom["i_2"]/(R_nom["r_1"]/R_nom["r_0"]+1)
    I_nom["i_0"] = I_nom["i_2"] - I_nom["i_1"]

    I_ohm["i_e"] = V_ohm/R_eq(R_ohm)
    I_ohm["i_3"] = V_ohm/R_ohm["r_3"]
    I_ohm["i_2"] = I_ohm["i_e"] - I_ohm["i_3"]
    I_ohm["i_1"] = I_ohm["i_2"]/(R_ohm["r_1"]/R_ohm["r_0"]+1)
    I_ohm["i_0"] = I_ohm["i_2"] - I_ohm["i_1"]
else:
    I_nom["i_e"] = V_nom/R_eq(R_nom)
    I_nom["i_0"] = V_nom/R_nom["r_0"]
    I_nom["i_1"] = V_nom/R_nom["r_1"]

    I_ohm["i_e"] = V_ohm/R_eq(R_ohm)
    I_ohm["i_0"] = V_ohm/R_ohm["r_0"]
    I_ohm["i_1"] = V_ohm/R_ohm["r_1"]

save = open("out/kcl_{}.out".format(N), "w") # Salvando os resultados da analise
save.write("Current\t Nominal (A)\t Ammeter (A)\t\t Ohmeter (A)\n")
for i in I_nom:
    x_amm = I_amm[i]
    x_ohm = I_ohm[i]
    eq = ""
    if (abs(x_amm.nominal-x_ohm.nominal) < 2*(x_amm.incerteza+x_ohm.incerteza)):
        eq = "Equivalente"
    elif (abs(x_amm.nominal-x_ohm.nominal) > 3*(x_amm.incerteza+x_ohm.incerteza)):
        eq = "Não equivalente"
    else:
        eq = ""
    save.write("{}:\t {:.5f}\t\t {}\t\t {}\t {} \n".format(i,I_nom[i],I_amm[i],I_ohm[i],eq))

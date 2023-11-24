#1. the nature of gas and oil

class CrudeOil:
    carbon = 0.85 # 84 to 87%
    hydrogen = 0.12 # 11 to 14 %
    sulfur = 0.01 # 0.06 to 2%
    nitrogen = 0.003# 0.1 to 2%
    oxygen = 0.003 # 0.1 to 2%
    n_carbon_atoms = 5 # >= 5

    hydrocarbon_series = "paraffin" #paraffin, napthene, aromatic asphaltic
    saturated = True #only single bonds, unsaturated if one or more double bonds

class NaturalGas:
    carbon = 0.75 # 65 to 80%
    hydrogen = 0.12 # 1 to 25%
    sulfur = 0.001 # 0 to 0.2%
    nitrogen = 0.1# 1 to 15%
    oxygen = 0 # 0%
    n_carbon_atoms = 1 #1 to 4

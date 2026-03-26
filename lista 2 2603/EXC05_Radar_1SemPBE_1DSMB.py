velocidade_carro = float(input("Velocidade do carro: "))
limite_via = float(input("Limite da via: "))

if limite_via <= 100:
    limite_tolerado = limite_via+7
else :
    limite_tolerado = limite_via*1.07

if velocidade_carro-limite_tolerado >= limite_tolerado**0.2:

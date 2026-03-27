velocidade_carro = float(input("Velocidade do carro: "))
limite_via = float(input("Limite da via: "))

if limite_via <= 100:
    if velocidade_carro <= (limite_via + 7):
        print("Isento")
    elif velocidade_carro - (limite_via + 7) <= ((limite_via + 7) * 0.2):
        print("Multa média")
    elif ((limite_via + 7) * 0.2) < velocidade_carro - (limite_via + 7) <= ((limite_via + 7) * 0.5):
        print("Multa grave")
    elif velocidade_carro - (limite_via + 7) > ((limite_via + 7) * 0.5):
        print("Multa gravissima + Suspensão")
    else :
        print("não deve cair aqui")

elif limite_via > 100:
    if velocidade_carro <= (limite_via*1.07):
        print("Isento")
    elif velocidade_carro - (limite_via *1.07) <= ((limite_via*1.07) * 0.2):
        print("Multa média")
    elif ((limite_via*0.07) * 0.2) < velocidade_carro - (limite_via*1.07) <= ((limite_via*1.07) * 0.5):
        print("Multa grave")
    elif velocidade_carro - (limite_via*1.07) > ((limite_via*0.07) * 0.5):
        print("Multa gravissima + Suspensão")
    else:
        print("Nao deve cair aqui")
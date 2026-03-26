L1 = float (input ("Digite o valor do lado 1:"))
L2 = float (input ("Digite o valor do lado 2:"))
L3 = float (input ("Digite o valor do lado 3:"))

if (L1 <= (L2 + L3)) and L2 <= (L1 + L3) and L3 <= (L1 + L2):
    print("É um triângulo")
    if L1 == L2 and L1 == L3 and L2 == L3:
        print("É um Equilatero")
    elif L1 == L2 and L2 != L3 or L1 == L3 and L1 != L2 or L2 == L3 and L3 != L1:
        print("É um Isosceles")
    else :
        print("É um Escaleno")
    #Achar o maior
    if L1 >= L2 and L1 > L3:
        maior = L1
    elif L2 >= L3 and L2 > L1:
        maior = L2
    else :
        maior = L3

    #Achar o menor
    if L1 <= L2 and L1 < L3:
        menor = L1
    elif L2 <= L3 and L2 < L1:
        menor = L2
    else :
        menor = L3

    #achar o do meio
    if L2 < L1 and L1 < L3 or L3 < L1 and L1 < L2:
        meio = L1
    elif L1 < L2 and L2 < L3 or L3 < L2 and L2 < L1:
        meio = L2
    else :
        meio = L3

    if maior**2 == menor**2+meio**2:
        print("É um triângulo retângulo")
    else :
        print("Não é um Triângulo Retangulo")
else :
    print("Não é um triângulo")

import math

x1 = int(input("Digite o valor x1: "))
y1 = int(input("Digite o valor y1: "))
x2 = int(input("Digite o valor x2: "))
y2 = int(input("Digite o valor y2: "))

distancia = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
print(distancia)
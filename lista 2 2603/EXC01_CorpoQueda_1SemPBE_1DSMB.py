import math

h = float(input("Informe a altura do corpo: "))
g = -9.8
if h < 0 :
    print("A altura nao pode ser negativa!")
else:
    t = ((-2 * h) / g ) **0.5
    print(f"O tempo de queda é de: {t}")
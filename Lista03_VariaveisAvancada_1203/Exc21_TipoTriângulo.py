a = int(input("Informe o lado A do triângulo: "))
b = int(input("Informe o lado B do triângulo: "))
c = int(input("Informe o lado C do triângulo: "))

print("O triângulo é...\n")
print(f"Isósceles: {a == b and a != c or a != b and a == c} ")
print(f"Escaleno: {a != b and a != c }")
print(f"Equilátero: {a == b and a == c and b == c}")

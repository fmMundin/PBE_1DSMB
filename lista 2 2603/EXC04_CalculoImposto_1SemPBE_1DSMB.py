from winsound import SND_ALIAS

salario_bruto = float(input("Informe o valor do salário bruto: "))

if salario_bruto <= 2000:
    imposto = 0
elif 2000.01 < salario_bruto <= 4000:
    imposto = (salario_bruto - 2000)*0.1
elif 4000.01 < salario_bruto <= 8000:
    imposto = ((salario_bruto - 4000)*0.2)+ (salario_bruto - 2000)*0.1
else:
    imposto = (( salario_bruto - 8000)*0.3 )+ ((salario_bruto - 4000)*0.2) + ((salario_bruto - 2000)*0.1)
print(f"Salário Bruto: {salario_bruto}")
print(f"Imposto: {imposto}")
print(f"Salário Líquuido: R${salario_bruto+imposto:.2f}")
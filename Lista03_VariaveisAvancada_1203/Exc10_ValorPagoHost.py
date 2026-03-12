mensalidade = float(input("Informe o valor do mensalidade do sistema: "))
qtd_meses = int(input("Informe a quantidade de meses contratados: "))
total_pg = mensalidade*qtd_meses
print(F"O valor a ser pago é de R${total_pg:.2f}")
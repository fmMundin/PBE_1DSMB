preco_licenc = float(input("Informe o valor de uma licença:"))
qtd_dev = int(input("Quantidade de desenvolvedores: "))
custoLicencas = preco_licenc * qtd_dev
print(f"O custo total em licenças será de R${custoLicencas:.2f}")
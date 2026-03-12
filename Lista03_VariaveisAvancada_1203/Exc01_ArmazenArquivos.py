qtd_arquivos = int(input("Informe a quantidade de arquivos: "))
tam_medio = float(input("Informe a tamanho médio dos arquivo: "))
tam_gb = (tam_medio*qtd_arquivos)/1024
print(f"A quantidade de arquivos em Gigabytes é: {tam_gb}")
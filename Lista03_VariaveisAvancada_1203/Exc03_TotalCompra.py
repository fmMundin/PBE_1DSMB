preco_prod = float(input("informe o valor do produto: "))
qtd = int(input("Informe a quantidade comprada: "))
frete = float(input("informe o valor do frete: "))
valor_total = (preco_prod*qtd) + frete
print(f"O valor total da compra foi R${valor_total:.2f}")
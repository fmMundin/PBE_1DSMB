dia = input("Digite o dia do seu nascimento: ")
mes = input("Digite o mes de seu nascimento: ")
ano = input("Digite o ano de seu nascimento: ")
bissexto = False
char_ano = ano
char_mes = mes
ano = int(ano)

if 1900 >= ano < 2026 and len(char_ano) == 4:
    print("Ano válido")
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        bissexto = True
else :
    print("Ano inválido")

match char_mes:
    case 1:
        print("mes encontrado")
    case "2":
        print("mes n encontrado")
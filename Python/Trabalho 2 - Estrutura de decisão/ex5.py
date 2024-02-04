#Escreva um programa que inserido o mês, exiba quantos dias tem esse mês.
# Considere que o ano não é bissexto.

mes = input()

if mes == "Janeiro":
    print("31")
elif mes == "Fevereiro":
    print("28")
elif mes == "Março":
    print("31")
elif mes == "Abril":
    print("30")
elif mes == "Maio":
    print("31")
elif mes == "Junho":
    print("30")
elif mes == "Julho":
    print("31")
elif mes == "Agosto":
    print("31")
elif mes == "Setembro":
    print("30")
elif mes == "Outubro":
    print("31")
elif mes == "Novembro":
    print("30")
else:
    print("31")
    
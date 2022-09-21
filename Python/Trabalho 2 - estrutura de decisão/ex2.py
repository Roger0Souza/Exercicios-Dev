# Faça um programa que receba um número inteiro e exiba uma mensagem indicando se o número é par ou ímpar.
# se é positivo ou negativo, ou se é zero.

n = int(input())

if n == 0:
    resul = "Zero"
    print(resul)
elif n % 2 == 0 and n > 0:
    sinal = "Positivo"
    resul = "Par"
    print(resul)
    print(sinal)
elif n % 2 == 0 and n < 0:
    sinal = "Negativo"
    resul = "Par"
    print(resul)
    print(sinal)
elif n % 2 != 0 and n > 0:
    sinal = "Positivo"
    resul = "Impar"
    print(resul)
    print(sinal)
else:
    sinal = "Negativo"
    resul = "Impar"
    print(resul)
    print(sinal)

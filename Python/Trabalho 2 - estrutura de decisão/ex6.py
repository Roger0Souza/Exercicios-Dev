#Escreva um programa que determine se um determinado ano é um ano bissexto.
#Um ano é bissexto se for divisível por 4, mas não por 100, ou se for divisível por 400.

ano = int(input())
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("SIM")
else:
    print("NÃO")
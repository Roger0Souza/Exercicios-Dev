#Escreva um programa para calcular o valor da função f abaixo

#f(a,b) = 3(a+b)³ + 275b² - 127a - 41

#dados os valores inteiros a e b

a = int(input())
b = int(input())
soma = (3*((a+b)**3))+(275*(b**2)) - (127*a) - 41

print("%.2f", soma)
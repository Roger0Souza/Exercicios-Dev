#Escreva um programa que leia um inteiro positivo n, 1<=n<=9 e gera o valor do número n + nn + nnn

n = input()
n2 = n+n
n3 = n+n+n
n2 = int(n2)
n3 = int(n3)
n= int(n)
print("%.d"% (n + n2 + n3))
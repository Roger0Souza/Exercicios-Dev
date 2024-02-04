'''
Escreva um programa que receba um vetor com 
�
n valores reais e calcule a soma e multiplicação prefixas dos valores do vetor. A saída deve exibir o valor da soma e multiplicação prefixas para cada índice.

'''

vetor = [float(x) for x in input().split()]

for i in range(len(vetor)):
    sum = vetor[i]
    prod = vetor[i]
    for j in range(i):
        sum += vetor[j]
        prod = prod*vetor[j]
    print("%.2f %.2f" % (sum,prod))
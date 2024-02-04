'''
Faça um programa que leia um vetor de 
�
n posições com valores entre 0 e 20 e encontre:

A soma dos valores armazenados no vetor;
O número de ocorrências do valor vn;
O maior valor armazenado no vetor;
As posições onde aparecem o maior valor encontrado no item 3. – note que aqui o programa possivelmente imprimirá mais de uma posição.

'''

vetor1 = [int(x) for x in input().split()]
soma = 0
num = 0
posição= ""
a = len(vetor1)
for i in range(a):
    soma += vetor1[i]
    if(vetor1[i] ==  
max(vetor1)):
        posição += str(i) + ' '
    if(vetor1[i] == vetor1[a-1]):
           num += 1
print(soma)
print(num)
print(max(vetor1))
print(posição)
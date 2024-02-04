'''
Faça um programa que preenche um vetor com valores inteiros, fornecidos um por linha até que seja dado um valor negativo (o valor negativo não deve ser inserido no vetor). Depois imprima:

A quantidade de valores maiores do que 5;
A soma dos valores pares que foram armazenados no vetor;
A soma dos valores ímpares que foram armazenados no vetor,
A quantidade total de valores armazenados no vetor;
O vetor, em uma linha;

'''

vetor = []

qtd = 0
par = 0 
impar = 0
while True:
    x= int(input())
    if(x < 0):
        break
    vetor. append(x)
for i in range(len(vetor)):
    if(vetor[i] > 5):
        qtd += 1
    if((vetor[i] + 1) %2==0):
        impar += vetor [i]
    else: 
        par += vetor[i]
print(qtd) 
print(par)
print(impar)
print(len (vetor))
print(*vetor)
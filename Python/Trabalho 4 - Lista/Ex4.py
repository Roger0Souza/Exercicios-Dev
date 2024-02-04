'''
Faça um programa que leia um vetor 
�
�
�
vet de 20 posições. O programa deve gerar, a partir do vetor lido, um outro vetor 
�
�
�
pos que contenha apenas os valores inteiros positivos de 
�
�
�
vet. A partir do vetor 
�
�
�
pos, deve ser gerado um outro vetor 
�
�
�
�
�
�
semdup que contenha apenas uma ocorrência de cada valor de 
�
�
�
pos.

A saída do programa deve ser composta apenas pelos elementos de 
�
�
�
�
�
�
semdup separados por um espaço.

'''

vet = list(map(int, input().split()))

pos = list()
semdup = list()
for i in vet:
    if i >= 0:
        pos.append(i)
        if i not in semdup:
            semdup.append(i)
lst_str = str(semdup)[1:-1] 

lst_str =lst_str.replace(",","")

print(lst_str)
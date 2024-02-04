'''
Escreva um programa que receba um vetor com 
�
n valores inteiros entre 
0
0 e 
20
20, com possíveis repetições e imprima os números repetidos e quantas vezes aparecem. Ordene a saída pelos valores repetidos e ignore aqueles que aparecem apenas 
1
1 vez. Caso não hajam repetições a saída do programa deve ser vazia.

'''

v = list(map(int,input().strip().split()))

listed=list(set(v))
qtd=[0]*len(listed)

for i in range(len(listed)):
    tmp_qtd=0
    for j in range(len(v)):
       if(listed[i]==v[j]):
           tmp_qtd+=1
    qtd.append(tmp_qtd)

qtd = [i for i in qtd if i != 0]

if(len(qtd)==len(listed)):
    for i in range(len(qtd)):
        if(qtd[i]>1):
            print(str(listed[i]) + ' ' + str(qtd[i]))
'''Dada uma matriz inteira A 
�
×
�
n×n, verificar se A é de permutação.'''

dimensao = int(input())

matriz = [float(x) for x in input().split()]
contador = 0
j = 0
k = 0
matrizF = []
confirmL = False
confirmC = False
#montando matriz


for i in range(dimensao):
    matrizF.append([])
    for j in range(dimensao):
        matrizF[i].append(matriz[contador])
        contador += 1
#verificando matriz
#passando por linhas
for i in range(dimensao):
    if sum(matrizF[i]) == 1:
        confirmL = True
    #if sum(matrizF[j]) != 1 or sum(matrizF[j]) != 0:
        
for i in range(dimensao):
    soma = 0
    for j in range(dimensao):
        soma += matrizF[j][i]
    if soma != 1:
        confirmC = False
        break
    else:
        confirmC = True
            
#mostrando resultados
if confirmL == True and confirmC == True:
    for f in matrizF:
        print(' '.join(map(str, ['%.1d' % x for x in f])))
    print(confirmC)
else:
    for f in matrizF:
        print(' '.join(map(str, ['%.1d' % x for x in f])))
    print(confirmC)
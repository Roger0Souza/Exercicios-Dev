'''
Dada uma matriz 
�
A de tamanho 
�
×
�
m×n, definimos uma "ampulheta" na matriz um pedaço de 
�
A no qual os elementos se dispõem na seguinte maneira:

a b c
  d 
e f g

Faça um programa que calcule a ampulheta com a maior soma de seus elementos.

Por exemplo, imagine a matriz quadrada de ordem 6:

1 1 1 0 0 0 
0 1 0 0 0 0 
1 1 1 0 0 0 
0 0 2 4 4 0 
0 0 0 2 0 0 
0 0 1 2 4 0

então, suas ampulhetas são:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

'''

LA, LB = input().split()
LA, LB = int(LA), int(LB)

matriz = []

for i in range(0, LA):
    matriz.append([0]*LB)
    matriz[i] = [float(x) for x in input().split()]

lista_soma = []
soma = 0
i = 0


while i < (LA-2):
    j = 0
    while j < (LB - 2):
        lista_soma.append(matriz[i][j])
        lista_soma.append(matriz[i][j+1])
        lista_soma.append(matriz[i][j+2])
        lista_soma.append(matriz[i+1][j+1])
        lista_soma.append(matriz[i+2][j])
        lista_soma.append(matriz[i+2][j+1])
        lista_soma.append(matriz[i+2][j+2])
        if sum(lista_soma) > soma:
            soma = sum(lista_soma)
            lista_soma = []
        else:
            lista_soma = []
        j += 1
    i += 1
print('%.1d' % soma)
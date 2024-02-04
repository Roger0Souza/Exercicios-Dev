'''
Dado um tabuleiro 
�
×
�
N×M de batalha naval (1 = navio, 0 = água) e uma sequência de 
�
T tiros 
(
�
,
�
)
(x,y), calcule se todos os navios foram destruídos ou não. Para um navio ser destruído, todas casas do tabuleiro das quais ele ocupa devem ser atingidas.

Entrada

A primeira linha contém os valores de N, M e T;
As N linhas subsequentes contêm as linhas da matriz que representa o tabuleiro;
As últimas T linhas contém as coordenadas dos tiros.
Saída

A saída deverá ser
S ou N

'''

n, m, t = (int(i) for i in input().split())
tabuleiro = []
tiros = []
c = 0
for i in range(n):
    tabuleiro.append([int(i) for i in input().split()])
for i in range(t):
    tiros.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        for k in range(t):
            if i == tiros[k][0] and j == tiros[k][1]:
                tabuleiro[i][j] = 0
        if tabuleiro[i][j] == 0:
            c += 1
if c == n*m:
    print('S')
else:
    print('N')
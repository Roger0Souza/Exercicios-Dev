'''

Dada a configuração inicial das bombas (1 = bomba, 0 = caso contrario) em um tabuleiro de tamanho N x M, imprima o tabuleiro completo com todos os números. Coloque -1 no lugar das bombas e 0 a 8 no restante.

'''

m = [int(i) for i in input().split()]
matriz = [[], [], []]

matriz[0].append([0] * (m[1] + 2))
matriz[1].append([0] * (m[1] + 2))

for i in range(m[0]):
    matriz[0].append([0] + [int(j) for j in input().split()] + [0])
    matriz[1].append([0] * (m[1] + 2))

matriz[0].append([0] * (m[1] + 2))
matriz[1].append([0] * (m[1] + 2))

for i in range(1, 1 + m[0]):
    for j in range(1, 1 + m[1]):
        if matriz[0][i][j]:
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k or l:
                        matriz[1][i + k][j + l] += 1

for i in range(1, m[0] + 1):
    matriz[2].append(matriz[1][i][1:m[1] + 1])
    for j in range(1, m[1] + 1):
        if matriz[0][i][j]: matriz[2][i - 1][j - 1] = -1

for i in matriz[2]:
    print(' '.join(format(j, 'd') for j in i))
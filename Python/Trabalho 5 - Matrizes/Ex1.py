'''
Faça um programa que leia as dimensões de duas matrizes 
�
A e 
�
B, e depois leia as duas matrizes.

Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes e imprima o resultado da multiplicação, caso contrário, imprima 'Incompatíveis'.

'''

la, ca, lb, cb = input().split()
la, ca, lb, cb = int(la), int(ca), int(lb), int(cb)

A = [] #matriz A
B = [] #matriz B
F = [] #matriz resultado da multiplicação

if ca == lb:
    for l in range(la):
        L = [float(x) for x in input().split()]
        A.append(L)

    for l in range(lb):
        L = [float(x) for x in input().split()]
        B.append(L)

    for k in range(la):
        F.append([])
        for m in range(cb):
            F[k].append(0)
            for n in range(ca):
                F[k][m] += A[k][n] * B[n][m]
    for f in F:
        print(' '.join(map(str, ['%.2f' % x for x in f])))
else:
    print('Incompatíveis')
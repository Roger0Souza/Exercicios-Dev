N = int(input())
cont = 0

for i in range(1, N):
    if N%i == 0:
        cont += i
if cont == N:
    print("True")
else:
    print("False")
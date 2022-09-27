n = int(input())
cont = 0

for i in range (2, n):
    if n%i == 0:
        print (i)
        cont += 1
if cont == 0:
     print('primo')
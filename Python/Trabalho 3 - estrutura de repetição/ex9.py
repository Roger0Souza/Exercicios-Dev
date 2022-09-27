n = int(input())
count = 0
palavra = ""
while (count < n):
    palavra += input()
    count += 1
silaba = input()
count = 0
while (count < len(silaba)):
    k = 0
    quant = 0
    while(k < len(palavra)):
        if (silaba[count] == palavra[k]):
            quant += 1
        k += 1
    print(str(silaba[count] + " = " + str(quant)))
    count += 1


            


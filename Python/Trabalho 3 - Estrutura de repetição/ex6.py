# put your python code here
n = int(input())

S = 0

for i in range (0, n):
    S += (i+1)/(n-i)
print("%.48f" % S)
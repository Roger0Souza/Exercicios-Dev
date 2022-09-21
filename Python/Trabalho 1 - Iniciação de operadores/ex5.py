# Escreva um programa que transforme o valor correspondente a um intervalo temporal, expresso em horas, minutos e segundos no valor correspondente em segundos

h, m, s = input().split(':')
h = float(h)*3600
m = float(m)*60
s = float(s)
T = h+m+s
print("%.d"%T)
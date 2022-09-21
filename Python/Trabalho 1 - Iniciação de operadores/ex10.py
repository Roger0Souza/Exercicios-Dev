#Supondo que k tangerinas serão distribuídas igualmente para n alunos, escreva um programa que
# Calcule quantas tangerinas inteiras cada aluno receberá e quantas tangerinas inteiras permanecerão na cesta!

#Entrada: quantidade de alunos, quantidade de tangerinas

#Saída Quantidade de tangerinas que cada aluno receberá, quantidade de tangerinas que permanecerão na cesta

al = int(input())
tg = int(input())

resul = tg//al
rest = tg%al

print(resul)
print(rest)

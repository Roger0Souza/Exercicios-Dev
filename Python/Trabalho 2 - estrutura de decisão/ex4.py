#Escreva um programa que recebe como entrada a data de nascimento do usuário, e informa qual o seu signo.
# A lista de signos e as datas podem ser encontradas na wikipédia.

d,m = input().split('/')

d,m = int(d),int(m)

x = d+(30*m)

if x <= 48:
    print ("Sagitário")
elif x <= 75:
    print ("Capricórnio")
elif x <= 101:
    print ("Aquário")
elif x <= 138:
    print("Peixes")
elif x <= 163:
    print("Áries")
elif x <= 199:
    print("Touro")
elif x <= 230:
    print("Gêmeos")
elif x <= 249:
    print("Câncer")
elif x <= 285:
    print("Leão")
elif x <= 330:
    print("Virgem")
elif x <= 352:
    print("Libra")
elif x <= 359:
    print("Escorpião")
elif x <= 377:
    print("Serpentário")
else:
    print("Sagitário")
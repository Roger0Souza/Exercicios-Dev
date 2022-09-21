#Voce recebe duas casas diferentes do tabuleiro de xadrez.
# Escreva um programa que determine se o rei pode ir da primeira casa para a segunda em um movimento

lin1, col1 = input().split()
lin2, col2 = input().split()

lin1, lin2, col1, col2 = int(lin1), int(lin2), int(col1), int(col2)

if lin2 == lin1 + 1 and col2 == col1 + 1:
    print("SIM")
elif lin2 == lin1 + 1 and col2 == col1 - 1:
    print("SIM")
elif lin2 == lin1 - 1 and col2 == col1 + 1:
    print("SIM")
elif lin2 == lin1 - 1 and col2 == col1 - 1:
    print("SIM")
elif lin2 == lin1 + 1 and col2 == col1:
    print("SIM")
elif lin2 == lin1 - 1 and col2 == col1:
    print("SIM")
elif lin2 == lin1 and col2 == col1 + 1:
    print("SIM")
elif lin2 == lin1 and col2 == col1 - 1:
    print("SIM")
else:
    print("NÃO")


# Faça um programa que dada a expressão algébrica de uma equação do segundo grau, troque x por y e vice versa

# A equação sempre estará disposta na forma: y = ax² + bx + c

eq = input()

eq = eq.replace('x', 'a')
eq = eq.replace('y', 'x')
eq = eq.replace('a', 'y')

print(eq)
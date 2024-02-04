# Faça um programa que calcule as raízes reais de uma equação de segundo grau:
# f(x) = ax² + bx + c, usando a fórmula de bhaskara.

a, b, c =  input().split()
a = float(a)
b = float(b)
c = float(c)

delta = ((b**2) - (4*a*c))

if delta < 0:
    print("No real roots.")
elif delta == 0:
    x = -b / (2*a)
    print("%.2f"% x)
else:
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    print("%.2f"% x1)
    print("%.2f"% x2)
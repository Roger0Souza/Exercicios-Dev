# Dados dois vetores em R³, dados como entrada na forma:

# x1 y1 z1
# x2 y2 z2

# Onde x1, y1, z1 são coordenadas do primeiro vetor, calcule:

# A soma entre eles
# O produto escalar
# O produto vetorial

x1, y1, z1 = input().split()
x2, y2, z2 = input().split()
x1, y1,z1  = float(x1), float(y1), float(z1)
x2, y2,z2  = float(x2), float(y2), float(z2)
somax = x1+x2 
somay = y1+y2
somaz = z1+z2
print("%.2f %.2f %.2f" %(somax,somay,somaz))
produto = x1*x2 + y1*y2 + z1*z2
print("%.2f" % produto)
vetx = y1*z2-y2*z1
vety = -(x1*z2-x2*z1)
vetz = x1*y2-x2*y1
print("%.2f %.2f %.2f" % (vetx, vety, vetz))

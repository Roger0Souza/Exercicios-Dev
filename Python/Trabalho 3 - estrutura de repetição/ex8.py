x, y, z, r = input().split()
x, y, z, r = int(x), int(y), int(z), int(r)

n = 0
for xi in range(-r-1, r+1):
    for yi in range(-r-1, r+1):
        for zi in range(-r-1, r+1):
            if (xi**2 + yi**2 + zi**2) <= r**2:
                dist = ((int(xi))**2 + (int(yi))**2 + (int(zi))**2)**(1/2)
                if (dist <= r):
                    n += 1
print(n)
n = float(input("Informe uma nota entre 0 e 10!"))

while n > 10 or n < 0:
    n = float(input("\nNota inválida, digite uma nota entre 0 e 10!"))
print("\nNota válida!!!")
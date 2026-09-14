a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print("Maior:", maior)
print("Menor:", menor)

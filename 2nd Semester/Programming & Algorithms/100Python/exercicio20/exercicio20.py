a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"Ordem crescente: {a}, {b}, {c}")

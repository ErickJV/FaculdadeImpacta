nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
print(f"Media: {media:.1f}")
if media >= 7:
    print("Situacao: APROVADO")
else:
    print("Situacao: REPROVADO")

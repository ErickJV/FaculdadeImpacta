valor_imovel = float(input("Valor do imovel: R$ "))
salario = float(input("Salario: R$ "))
prazo = int(input("Prazo (anos): "))

prestacao = valor_imovel / (prazo * 12)
limite = salario * 0.30

print(f"Prestacao: R$ {prestacao:.2f}")
print(f"Limite: R$ {limite:.2f}")

if prestacao <= limite:
    print("Resultado: APROVADO")
else:
    print("Resultado: NEGADO")

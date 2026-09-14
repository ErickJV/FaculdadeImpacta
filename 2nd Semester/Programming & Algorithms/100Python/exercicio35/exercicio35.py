idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NAO): ").strip().upper()

preco = 30.00

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor = preco * 0.50
else:
    valor = preco

print(f"Valor do ingresso: R$ {valor:.2f}")

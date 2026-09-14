numero = int(input("Digite um numero (1-7): "))

dias = {
    1: "SEGUNDA-FEIRA",
    2: "TERCA-FEIRA",
    3: "QUARTA-FEIRA",
    4: "QUINTA-FEIRA",
    5: "SEXTA-FEIRA",
    6: "SABADO",
    7: "DOMINGO"
}

if numero in dias:
    print(dias[numero])
else:
    print("OPCAO INVALIDA")

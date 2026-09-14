peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura * altura)
print(f"IMC: {imc:.1f}")

if imc < 18.5:
    print("Classificacao: ABAIXO DA FAIXA")
elif imc < 25:
    print("Classificacao: FAIXA NORMAL")
elif imc < 30:
    print("Classificacao: ACIMA DA FAIXA")
else:
    print("Classificacao: FAIXA ELEVADA")

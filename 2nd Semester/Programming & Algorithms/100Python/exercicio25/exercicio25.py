preco = float(input("Preco: R$ "))
print("1 - Dinheiro ou Pix")
print("2 - Debito")
print("3 - Credito a vista")
print("4 - Credito parcelado")
opcao = int(input("Opcao: "))

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    print("OPCAO INVALIDA")
    valor_final = None

if valor_final is not None:
    print(f"Valor final: R$ {valor_final:.2f}")

preco = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))
subtotal = preco * quantidade
total = subtotal + frete
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")

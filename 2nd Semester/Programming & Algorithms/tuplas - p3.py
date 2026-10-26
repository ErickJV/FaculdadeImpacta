print("="*60 + "\n")

# 3. Tuplas são imutáveis
print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla_usuario = ("Erick", "00000000000", "erick@gmail.com", "#12345abcde")
print(f"Tupla original: {tupla_usuario}\n")

print("Tentando modificar:")
try:
    tupla_usuario[0] = "Igor"
except TypeError as e:
    print(f"Erro: {e}\n")

print("Tentando adicionar:")
try:
    tupla_usuario.append("teste")
except AttributeError as e:
    print(f"Erro: Tuplas não têm append\n")

print("Tuplas são imutáveis (proteção de dados)")
print("Listas podem ser modificadas\n")

print("="*60 + "\n")
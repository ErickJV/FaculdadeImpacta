print("="*60)
print("TUPLAS EM PYTHON")
print("="*60 + "\n")

print("O QUE É UMA TUPLA?\n")
print("""
Uma tupla é uma sequência de elementos imutável (não pode ser modificada).

Características:
- Imutável (Não pode ser modificada)
- Ordenada (mantém ordem)
- Acessa por índice (como listas)
- pode conter diferentes tipos
- Usa parênteses: ()

Sintaxe: tupla = (elemento1, elemento2, elemento3)
""")

print("1. CRIANDO TUPLAS:\n")

tupla_vazia = ()

print(f"Tupla vazia: {tupla_vazia}")

tupla_um = (42,)
print(f"Tupla com um elemento: {tupla_um}")

tupla_numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {tupla_numeros}")

tupla_palavras = ("Python", "é", "incrivel")
print(f"Tupla de palavras: {tupla_palavras}")

tupla_mista = ("João", 25, 8.5, True)
print(f"Tupla mista: {tupla_mista}")

tupla_implicita = 5, 10, 15
print(f"Tupla sem parênteses: {tupla_implicita}\n")
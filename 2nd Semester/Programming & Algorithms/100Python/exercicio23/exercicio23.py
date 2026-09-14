idade = int(input("Digite a idade: "))

if idade < 16:
    print("NAO PODE VOTAR")
elif idade <= 17:
    print("VOTO OPCIONAL")
elif idade <= 69:
    print("VOTO OBRIGATORIO")
else:
    print("VOTO OPCIONAL")

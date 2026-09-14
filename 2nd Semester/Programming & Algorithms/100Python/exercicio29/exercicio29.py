a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("EQUILATERO")
    elif a == b or a == c or b == c:
        print("ISOSCELES")
    else:
        print("ESCALENO")
else:
    print("NAO FORMA TRIANGULO")

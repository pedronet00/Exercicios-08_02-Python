val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))

tupla = (val1, val2, val3)

print("Valores informados e inseridos em uma tupla:")
for valor in (tupla):
    print("-", valor)
val1 = int(input("Digite o primeiro valor: "))
val2 = int(input("Digite o segundo valor: "))
val3 = int(input("Digite o terceiro valor: "))
val4 = int(input("Digite o quarto valor: "))
val5 = int(input("Digite o quinto valor: "))

tupla = (val1, val2, val3, val4, val5)

if len(set(tupla)) == len(tupla):
    print("A tupla não possui valores repetidos.")
else:
    print("A tupla possui valores repetidos.")
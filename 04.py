valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))
valor5 = int(input("Digite o quinto valor: "))

tupla = (valor1, valor2, valor3, valor4, valor5)

soma = sum(tupla)
multiplicacao = 1
for valor in tupla:
    multiplicacao *= valor
media = soma / len(tupla)

print("Resultados:")
print("Soma dos valores:", soma)
print("Multiplicação dos valores:", multiplicacao)
print("Média dos valores:", media)
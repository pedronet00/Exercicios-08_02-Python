def calculadora():
    while True:
        print("Selecione a operação desejada:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Divisão")
        print("4 - Multiplicação")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 0:
            print("Encerrando a calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif opcao == 3:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        elif opcao == 4:
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        else:
            print("Opção inválida. Tente novamente.")


calculadora()
while True:
    print("\nEscolha uma opção:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Divisão")
    print("4: Multiplicação")
    print("5: Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        num1 = input("Digite o primeiro número da adição: ")
        num2 = input("Digite o segundo número da adição: ")
        print("A soma é igual a: " + str(int(num1) + int(num2)))

    elif opcao == "2":
        num1 = input("Digite o primeiro número da subtração: ")
        num2 = input("Digite o segundo número da subtração: ")
        print("A subtração é igual a: " + str(int(num1) - int(num2)))

    elif opcao == "3":
        num1 = input("Digite o primeiro número da divisão: ")
        num2 = input("Digite o segundo número da divisão: ")
        print("A divisão é igual a: " + str(int(num1) / int(num2)))

    elif opcao == "4":
        num1 = input("Digite o primeiro número da multiplicação: ")
        num2 = input("Digite o segundo número da multiplicação: ")
        print("O produto é igual a: " + str(int(num1) * int(num2)))

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Essa opção não é válida, por favor, escolha entre os números de 1 a 5")

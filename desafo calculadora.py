class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero!"
        return a / b


# Programa principal
calc = Calculadora()

while True:
    print("\n=== CALCULADORA ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # validação da opção
    while opcao not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida!")
        opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Saindo da calculadora...")
        break

    # entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = calc.somar(num1, num2)

    elif opcao == "2":
        resultado = calc.subtrair(num1, num2)

    elif opcao == "3":
        resultado = calc.multiplicar(num1, num2)

    elif opcao == "4":
        resultado = calc.dividir(num1, num2)

    print(f"Resultado: {resultado}")
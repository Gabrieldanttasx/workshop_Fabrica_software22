class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            return "Erro: divisão por zero não é permitida."
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def mostrar_historico(self):
        if len(self.historico) == 0:
            print("Nenhuma operação foi realizada ainda.")
        else:
            print("\n=== HISTÓRICO ===")
            for operacao in self.historico:
                print(operacao)


calc = Calculadora()

while True:
    print("\n=== CALCULADORA ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Ver histórico")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "6":
        print("Saindo da calculadora...")
        break

    elif opcao == "5":
        calc.mostrar_historico()

    elif opcao in ["1", "2", "3", "4"]:
        try:
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

        except ValueError:
            print("Erro: digite apenas números válidos.")

    else:
        print("Opção inválida. Tente novamente.") 
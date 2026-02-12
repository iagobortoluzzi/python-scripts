import math

historico = []

def menu():
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("7 - Logaritmo")
    print("8 - Seno")
    print("9 - Cosseno")
    print("10 - Tangente")
    print("11 - Ver histórico")
    print("0 - Sair")

def registrar(operacao, resultado):
    historico.append(f"{operacao} = {resultado}")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "0":
                print("Saindo...")
                break

            elif opcao in ["1", "2", "3", "4", "5"]:
                a = float(input("Digite o primeiro valor: "))
                b = float(input("Digite o segundo valor: "))

                if opcao == "1":
                    res = a + b
                    registrar(f"{a} + {b}", res)

                elif opcao == "2":
                    res = a - b
                    registrar(f"{a} - {b}", res)

                elif opcao == "3":
                    res = a * b
                    registrar(f"{a} * {b}", res)

                elif opcao == "4":
                    if b == 0:
                        print("Erro: divisão por zero.")
                        continue
                    res = a / b
                    registrar(f"{a} / {b}", res)

                elif opcao == "5":
                    res = a ** b
                    registrar(f"{a} ^ {b}", res)

            elif opcao == "6":
                x = float(input("Digite o valor: "))
                res = math.sqrt(x)
                registrar(f"sqrt({x})", res)

            elif opcao == "7":
                x = float(input("Digite o valor: "))
                res = math.log10(x)
                registrar(f"log({x})", res)

            elif opcao == "8":
                x = math.radians(float(input("Digite o ângulo em graus: ")))
                res = math.sin(x)
                registrar(f"sin({x})", res)

            elif opcao == "9":
                x = math.radians(float(input("Digite o ângulo em graus: ")))
                res = math.cos(x)
                registrar(f"cos({x})", res)

            elif opcao == "10":
                x = math.radians(float(input("Digite o ângulo em graus: ")))
                res = math.tan(x)
                registrar(f"tan({x})", res)

            elif opcao == "11":
                print("\n=== HISTÓRICO ===")
                for item in historico:
                    print(item)
                continue

            else:
                print("Opção inválida.")
                continue

            print(f"Resultado: {res}")

        except ValueError:
            print("Erro: valor inválido.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
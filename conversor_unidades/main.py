def menu():
    print("\n=== CONVERSOR INTELIGENTE DE UNIDADES ===")
    print("1 - Comprimento")
    print("2 - Peso")
    print("3 - Temperatura")
    print("4 - Tempo")
    print("5 - Dados digitais")
    print("0 - Sair")

def converter_comprimento(valor, de, para):
    unidades = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001
    }
    return valor * unidades[de] / unidades[para]

def converter_peso(valor, de, para):
    unidades = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "t": 1000
    }
    return valor * unidades[de] / unidades[para]

def converter_temperatura(valor, de, para):
    if de == "c" and para == "f":
        return valor * 9/5 + 32
    if de == "f" and para == "c":
        return (valor - 32) * 5/9
    if de == "c" and para == "k":
        return valor + 273.15
    if de == "k" and para == "c":
        return valor - 273.15
    if de == "f" and para == "k":
        return (valor - 32) * 5/9 + 273.15
    if de == "k" and para == "f":
        return (valor - 273.15) * 9/5 + 32
    return valor

def converter_tempo(valor, de, para):
    unidades = {
        "s": 1,
        "min": 60,
        "h": 3600,
        "d": 86400
    }
    return valor * unidades[de] / unidades[para]

def converter_dados(valor, de, para):
    unidades = {
        "b": 1,
        "kb": 1024,
        "mb": 1024**2,
        "gb": 1024**3
    }
    return valor * unidades[de] / unidades[para]

def escolher_unidades(lista):
    print("Unidades disponíveis:", ", ".join(lista))
    de = input("Converter de: ").lower()
    para = input("Converter para: ").lower()
    return de, para

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break

        valor = float(input("Digite o valor: "))

        if opcao == "1":
            de, para = escolher_unidades(["m", "km", "cm", "mm"])
            resultado = converter_comprimento(valor, de, para)

        elif opcao == "2":
            de, para = escolher_unidades(["kg", "g", "mg", "t"])
            resultado = converter_peso(valor, de, para)

        elif opcao == "3":
            de, para = escolher_unidades(["c", "f", "k"])
            resultado = converter_temperatura(valor, de, para)

        elif opcao == "4":
            de, para = escolher_unidades(["s", "min", "h", "d"])
            resultado = converter_tempo(valor, de, para)

        elif opcao == "5":
            de, para = escolher_unidades(["b", "kb", "mb", "gb"])
            resultado = converter_dados(valor, de, para)

        else:
            print("Opção inválida.")
            continue

        print(f"\nResultado: {resultado}\n")

if __name__ == "__main__":
    main()

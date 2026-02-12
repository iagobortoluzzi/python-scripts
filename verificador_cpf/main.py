def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))

def calcular_digito(cpf, peso):
    soma = sum(int(dig) * p for dig, p in zip(cpf, range(peso, 1, -1)))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto

def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    return cpf[-2:] == f"{digito1}{digito2}"

def main():
    print("=== VERIFICADOR DE CPF ===")
    cpf = input("Digite o CPF: ")

    if validar_cpf(cpf):
        print("CPF VÁLIDO")
    else:
        print("CPF INVÁLIDO")

if __name__ == "__main__":
    main()
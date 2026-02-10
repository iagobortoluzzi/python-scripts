import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return None

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def avaliar_forca(senha):
    pontos = 0

    if any(c.islower() for c in senha):
        pontos += 1
    if any(c.isupper() for c in senha):
        pontos += 1
    if any(c.isdigit() for c in senha):
        pontos += 1
    if any(c in string.punctuation for c in senha):
        pontos += 1
    if len(senha) >= 12:
        pontos += 1

    if pontos <= 2:
        return "FRACA"
    elif pontos == 3:
        return "MÉDIA"
    elif pontos == 4:
        return "FORTE"
    else:
        return "MUITO FORTE"

def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")

    tamanho = int(input("Tamanho da senha (ex: 12): "))

    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == "s"
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("Incluir números? (s/n): ").lower() == "s"
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    senha = gerar_senha(
        tamanho,
        usar_maiusculas,
        usar_minusculas,
        usar_numeros,
        usar_simbolos
    )

    if senha:
        print(f"\nSenha gerada: {senha}")
        print(f"Força da senha: {avaliar_forca(senha)}")
    else:
        print("Erro: Nenhum conjunto de caracteres selecionado.")

if __name__ == "__main__":
    main()

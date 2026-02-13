import re
from collections import Counter

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

def analisar_texto(texto):
    caracteres = len(texto)
    letras = sum(c.isalpha() for c in texto)
    palavras = texto.split()
    frases = re.split(r'[.!?]+', texto)

    palavras_limpa = limpar_texto(texto).split()

    contagem = Counter(palavras_limpa)
    total_palavras = len(palavras_limpa)
    vocabulario = len(set(palavras_limpa))

    diversidade = (vocabulario / total_palavras * 100) if total_palavras else 0

    return {
        "caracteres": caracteres,
        "letras": letras,
        "palavras": len(palavras),
        "frases": len([f for f in frases if f.strip()]),
        "frequencia": contagem,
        "total_palavras": total_palavras,
        "vocabulario": vocabulario,
        "diversidade": diversidade
    }

def mostrar_resultado(dados):
    print("\n=== RELATÓRIO DO TEXTO ===")
    print(f"Caracteres: {dados['caracteres']}")
    print(f"Letras: {dados['letras']}")
    print(f"Palavras: {dados['palavras']}")
    print(f"Frases: {dados['frases']}")
    print(f"Vocabulário único: {dados['vocabulario']}")
    print(f"Diversidade vocabular: {dados['diversidade']:.2f}%")

    print("\n--- TOP 10 PALAVRAS ---")
    for palavra, qtd in dados["frequencia"].most_common(10):
        print(f"{palavra}: {qtd}")

def salvar_relatorio(dados):
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE ANÁLISE DE TEXTO\n\n")
        for k, v in dados.items():
            if k != "frequencia":
                f.write(f"{k}: {v}\n")

        f.write("\nTOP 10 PALAVRAS:\n")
        for palavra, qtd in dados["frequencia"].most_common(10):
            f.write(f"{palavra}: {qtd}\n")

def main():
    print("=== ANALISADOR INTELIGENTE DE TEXTO ===")
    print("1 - Digitar texto")
    print("2 - Ler arquivo .txt")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("\nDigite seu texto (ENTER duas vezes para finalizar):\n")
        linhas = []
        while True:
            linha = input()
            if linha == "":
                break
            linhas.append(linha)
        texto = "\n".join(linhas)

    elif opcao == "2":
        caminho = input("Digite o caminho do arquivo .txt: ")
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                texto = f.read()
        except:
            print("Erro ao abrir arquivo.")
            return
    else:
        print("Opção inválida.")
        return

    dados = analisar_texto(texto)
    mostrar_resultado(dados)
    salvar_relatorio(dados)

    print("\nRelatório salvo em: relatorio.txt")

if __name__ == "__main__":
    main()
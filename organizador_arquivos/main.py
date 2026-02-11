import os
import shutil

EXTENSOES = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".pptx"],
    "Planilhas": [".xlsx", ".csv"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi", ".bat", ".sh"]
}

def criar_pastas(base_path):
    for pasta in EXTENSOES:
        os.makedirs(os.path.join(base_path, pasta), exist_ok=True)
    os.makedirs(os.path.join(base_path, "Outros"), exist_ok=True)

def mover_arquivos(base_path):
    contagem = {pasta: 0 for pasta in EXTENSOES}
    contagem["Outros"] = 0

    for arquivo in os.listdir(base_path):
        caminho_arquivo = os.path.join(base_path, arquivo)

        if os.path.isfile(caminho_arquivo):
            _, ext = os.path.splitext(arquivo)
            movido = False

            for pasta, extensoes in EXTENSOES.items():
                if ext.lower() in extensoes:
                    shutil.move(caminho_arquivo, os.path.join(base_path, pasta, arquivo))
                    contagem[pasta] += 1
                    movido = True
                    break

            if not movido:
                shutil.move(caminho_arquivo, os.path.join(base_path, "Outros", arquivo))
                contagem["Outros"] += 1

    return contagem

def main():
    print("=== ORGANIZADOR AUTOMÁTICO DE ARQUIVOS ===")
    pasta = input("Digite o caminho da pasta que deseja organizar: ").strip()

    if not os.path.isdir(pasta):
        print("Caminho inválido.")
        return

    criar_pastas(pasta)
    resultado = mover_arquivos(pasta)

    print("\nOrganização concluída!\nResumo:")
    for pasta, qtd in resultado.items():
        print(f"{pasta}: {qtd} arquivos")

if __name__ == "__main__":
    main()

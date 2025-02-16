import os
from pathlib import Path
import patoolib

def images_to_cbr(folder_path, output_file):
    folder_path = Path(folder_path)

    if not folder_path.exists():
        print(f"A pasta {folder_path} não existe.")
        return

    files = sorted([f for f in folder_path.glob('*') if f.is_file() and f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.bmp', '.gif')])

    if not files:
        print("Nenhuma imagem encontrada na pasta.")
        return

    # Lista de arquivos para incluir no RAR
    file_list = [str(f) for f in files]

    try:
        # Cria o arquivo CBR (RAR) com as imagens
        patoolib.create_archive(output_file, file_list)
        print(f"Arquivo CBR criado: {output_file}")
    except Exception as e:
        print(f"Erro ao criar o arquivo CBR: {e}")

# Exemplo de uso:
# images_to_cbr('.', 'meu_comic.cbr')

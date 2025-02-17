import os
from pathlib import Path
import patoolib
import re

def images_to_cbr(folder_path, output_file):
    folder_path = Path(folder_path)

    if not folder_path.exists():
        print(f"A pasta {folder_path} não existe.")
        return

    # Função para obter a parte numérica do nome do arquivo, ignorando pontos, vírgulas e outros símbolos
    def get_number(filename):
        numbers = re.findall(r'\d+', ''.join(char for char in filename.name if char.isalnum()))
        return int(numbers[0]) if numbers else 0

    # Procurar por arquivos de imagem em todas as subpastas de forma recursiva
    files = sorted([
        f for f in folder_path.rglob('*')
        if f.is_file() and f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    ], key=lambda x: (
        [''.join(char for char in part if char.isalnum()) for part in x.parts[:-1]],  # Limpar nomes de pastas
        get_number(x), 
        ''.join(char for char in x.stem if char.isalnum()).zfill(3) + x.suffix  # Limpar nome do arquivo
    ))

    if not files:
        print("Nenhuma imagem encontrada na pasta ou subpastas.")
        return

    # Lista de arquivos para incluir no RAR
    file_list = [str(f) for f in files]

    try:
        # Criar o arquivo CBR (RAR) com as imagens
        patoolib.create_archive(output_file, file_list)
        print(f"Arquivo CBR criado: {output_file}")
    except Exception as e:
        print(f"Erro ao criar o arquivo CBR: {e}")

# Exemplo de uso:
# images_to_cbr('.', 'meu_comic.cbr')
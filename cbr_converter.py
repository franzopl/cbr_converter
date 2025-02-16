import os
from pathlib import Path
import patoolib

def images_to_cbr(folder_path, output_file):
    folder_path = Path(folder_path)

    if not folder_path.exists():
        print(f"A pasta {folder_path} não existe.")
        return

    # Function to get a numeric part from filename, ignoring dots
    def get_number(filename):
        import re
        numbers = re.findall(r'\d+', filename.name.replace('.', ''))
        return int(numbers[0]) if numbers else 0

    # Search for image files in all subfolders recursively
    files = sorted([
        f for f in folder_path.rglob('*')
        if f.is_file() and f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    ], key=lambda x: (list(x.parts[:-1]), get_number(x), x.stem.replace('.', '').zfill(3) + x.suffix))

    if not files:
        print("Nenhuma imagem encontrada na pasta ou subpastas.")
        return

    # List of files to include in the RAR
    file_list = [str(f) for f in files]

    try:
        # Create the CBR (RAR) file with the images
        patoolib.create_archive(output_file, file_list)
        print(f"Arquivo CBR criado: {output_file}")
    except Exception as e:
        print(f"Erro ao criar o arquivo CBR: {e}")

# Example usage:
# images_to_cbr('.', 'meu_comic.cbr')

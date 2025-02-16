import sys
from cbr_converter import images_to_cbr

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 main_converter.py <caminho_da_pasta> <nome_do_arquivo_saida>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = sys.argv[2]

    images_to_cbr(folder_path, output_file)

if __name__ == "__main__":
    main()

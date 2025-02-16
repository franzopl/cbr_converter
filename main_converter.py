# Importa a função images_to_cbr do módulo cbr_converter
from cbr_converter import images_to_cbr

# Define o caminho da pasta onde as imagens estão armazenadas
# Aqui usamos '.' para indicar a pasta atual
folder_path = '.'

# Define o nome do arquivo CBR que você quer criar
output_file = 'meu_comic.cbr'

# Chama a função para converter imagens para CBR
images_to_cbr(folder_path, output_file)

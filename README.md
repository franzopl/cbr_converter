- Este script ao ser executado irá converter todas as imagens no diretório atual em um arquivo cbr seguindo a ordem natural do nome dos arquivos.
- Se existirem subpastas o script seguirá primeiro a ordem das pastas e depois seguirá a ordem dos arquivos dentro das subpastas.
- Para executar o script siga os seguintes passos:

    1. git clone https://github.com/franzopl/cbr_converter.git
    2. pip install patool # bibliotéca necessária para executar o script
    3. instale rar no PATH do sistema # o rar é necessário para gerar os arquivos .cbr
    4. abra o terminal na pasta do scrip e execute o comando:
        ```
        python3 main_converter.py /caminho/para/a/pasta meu_arquivo.cbr


import sys
import re

for line in sys.stdin:
    line = re.sub(r'[^a-zA-ZáéíóúñÑ\s]|[\d]', '', line.strip())
    words = line.split()

    # Obtener el nombre del archivo desde el nombre de la entrada
    filename = sys.argv[1] 

    for word in words:
        # Excluir palabras vacías
        if word:
            word_lower = word.lower()  # Convertir la palabra a minúsculas
            print('{}\t{}\t{}'.format(filename, word, 1))

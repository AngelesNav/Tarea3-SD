import sys
import re
import os

# Lista de caracteres especiales a excluir
exclude_chars = set([",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"])

for line in sys.stdin:
    # Eliminar caracteres numéricos y los especificados en la lista
    line = re.sub(r'[^a-zA-ZñÑ\s]|[\d]', '', line.strip())
    words = line.split()

    for word in words:
        # Excluir palabras vacías y caracteres especiales
        if word and word not in exclude_chars:
            print('{}\t{}'.format(word, 1))

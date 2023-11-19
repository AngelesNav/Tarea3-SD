import sys
import re

all_words = []  # Lista para almacenar todas las palabras del texto

for line in sys.stdin:
    line = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]', '', line.strip())
    words = line.split()

    # Agregar todas las palabras a la lista
    all_words.extend(words)

# Obtener el nombre del archivo desde el nombre de la entrada
filename = sys.argv[1]

# Usar un conjunto para obtener palabras únicas y contar su frecuencia
unique_word_set = set(all_words)
for word in unique_word_set:
    # Excluir palabras vacías
    if word:
        print('{}\t{}\t{}'.format(filename, word, all_words.count(word)))

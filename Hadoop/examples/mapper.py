import sys
import re

for line in sys.stdin:
    line = re.sub(r'[^a-záéíóúñÑ\s]|[\d]', '', line.strip())
    words = line.split()

    filename = sys.argv[1] 

    for word in words:
         if word:
            word_lower = word.lower()  # Convertir la palabra a minúsculas
            print('{}\t{}\t{}'.format(filename, word, 1))

import sys

current_word = None
current_count = 0
word = None
current_filename = None

for line in sys.stdin:
    line = line.strip()
    filename,word, count = line.split('\t', 2)

    try:
        count = int(count)
    except ValueError:
        continue


    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}\t{}'.format(filename, current_word, current_count))
        current_word = word
        current_count = count

# Imprimir el último grupo de palabras al final del archivo
if current_word:
    print('{}\t{}\{}'.format(filename, current_word, current_count))

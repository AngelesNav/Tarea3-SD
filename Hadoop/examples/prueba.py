# Mapper function
def mapper(line):
    words = line.strip().split()
    for word in words:
        print(f"{word.lower()}\t1")

# Reducer function
def reducer(word, counts):
    total = sum(counts)
    print(f"{word}\t{total}")

# Simulación de entrada
input_data = [
    "El MapReduce es un modelo de programación",
    "MapReduce se utiliza para procesar grandes conjuntos de datos",
    "El modelo MapReduce consiste en funciones de mapeo y reducción"
]

# Fase de mapeo (se ejecuta en nodos esclavos)
for line in input_data:
    mapper_output = line.strip().split('\t')
    if len(mapper_output) == 2:
        word, count = mapper_output
        print(f"{word}\t{count}")

# Fase de reducción (se ejecuta en nodos esclavos)
current_word = None
current_count = 0
counts = []

for line in sorted(input_data):  # Ordenar para agrupar palabras
    reducer_output = line.strip().split('\t')
    if len(reducer_output) == 2:
        word, count = reducer_output
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                reducer(current_word, counts)
            current_word = word
            current_count = count
            counts = [count]

if current_word:  # Agregar una verificación para la última palabra
    reducer(current_word, counts)

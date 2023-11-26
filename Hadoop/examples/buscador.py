import re

def buscar_en_archivo(consulta, archivo, diccionario_documentos):
    # Leemos el contenido del archivo
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()

    # Utilizamos una expresión regular para encontrar todas las líneas que contienen la palabra de consulta
    patrón = re.compile(f'{consulta}:.*?\n')
    coincidencias = patrón.findall(contenido)

    # Creamos una lista de tuplas con el número de documento y la frecuencia para cada coincidencia
    resultados = [(int(match.group(1)), int(match.group(2))) for match in re.finditer(r'\((\d+), (\d+)\)', ''.join(coincidencias))]

    # Ordenamos los resultados por frecuencia en orden descendente
    resultados = sorted(resultados, key=lambda x: x[1], reverse=True)

    # Tomamos los 5 números de documento con las frecuencias más altas
    mejores_resultados = resultados[:5]

    # Extraemos la dirección de Wikipedia para cada resultado
    resultados_con_direccion = [(numero_documento, frecuencia, diccionario_documentos.get(numero_documento, f'Dirección de Wikipedia no encontrada para el documento {numero_documento}')) for numero_documento, frecuencia in mejores_resultados]

    return resultados_con_direccion

entradas = [
    "Apple", "Samsung", "Google", "Microsoft", "Amazon",
    "Coca-Cola", "IBM", "Toyota", "McDonald's", "Disney",
    "Nike", "Adidas", "Pepsi", "Panasonic", "BMW",
    "Mercedes-Benz", "Volkswagen", "Ford", "Chevrolet", "Prada",
    "Nestlé", "Intel", "Honda", "LG", "Nikon",
    "JBL", "Philips", "Lenovo", "Asus", "Salesforce"
]

diccionario_documentos = {i+1: f'https://es.wikipedia.org/wiki/{entrada}' for i, entrada in enumerate(entradas)}

# Ejemplo de uso
consulta_usuario = input("Ingrese la palabra a buscar: ")
archivo_a_buscar = '/workspaces/Tarea3-SD/Hadoop/examples/outhadoop/part-00000'  # Reemplaza 'archivo.txt' con el nombre de tu archivo

# Realizamos la búsqueda
resultados = buscar_en_archivo(consulta_usuario, archivo_a_buscar, diccionario_documentos)

if resultados:
    print(f"\nLos 5 mejores resultados para '{consulta_usuario}' son:")
    
    for i, resultado in enumerate(resultados, 1):
        print(f"\nDocumento: {resultado[0]}\nFrecuencia: {resultado[1]}\nURL: {resultado[2]}\n")
else:
    print(f"\nNo se encontraron resultados para '{consulta_usuario}'.")

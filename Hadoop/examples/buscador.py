import re

# Ruta al archivo de datos
ruta_archivo = '/workspaces/Tarea3-SD/Hadoop/examples/outhadoop/part-00000.txt'

# Arreglo de entradas y diccionario de documentos
entradas = [
    "Apple", "Samsung", "Google", "Microsoft", "Amazon",
    "Coca-Cola", "IBM", "Toyota", "McDonald's", "Disney",
    "Nike", "Adidas", "Pepsi", "Panasonic", "BMW",
    "Mercedes-Benz", "Volkswagen", "Ford", "Chevrolet", "Prada",
    "Nestlé", "Intel", "Honda", "LG", "Nikon",
    "JBL", "Philips", "Lenovo", "Asus", "Salesforce"
]

diccionario_documentos = {i+1: f'https://es.wikipedia.org/wiki/{entrada}' for i, entrada in enumerate(entradas)}

# Procesar datos proporcionados
def procesar_datos(datos_providenciados):
    diccionario_resultados = {}

    lineas = datos_providenciados.strip().split('\n')

    for linea in lineas:
        palabra, posiciones = linea.split(None, 1)
        posiciones = re.findall(r'\((\d+), (\d+)\)', posiciones)

        diccionario_resultados[palabra] = [(int(doc), int(freq)) for doc, freq in posiciones]

    return diccionario_resultados

# Función de búsqueda e impresión de los 5 con mayor frecuencia
def buscar_e_imprimir(diccionario_resultados, diccionario_documentos, palabra):
    resultados = diccionario_resultados.get(palabra, [])

    if resultados:
        # Ordenar los resultados por frecuencia en orden descendente
        resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)[:5]

        print(f'\nResultados para la palabra "{palabra}":\n')
        for doc, freq in resultados_ordenados:
            url = diccionario_documentos.get(doc, f'URL no encontrada para el documento {doc}')
            print(f'Documento: {doc}\nFrecuencia: {freq}\nURL: {url}')
            print('\n')
    else:
        print(f'No se encontraron resultados para la palabra "{palabra}".')

# Leer el archivo de datos
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    datos_providenciados = archivo.read()

# Solicitar al usuario ingresar una palabra clave
palabra_clave = input("Ingrese la palabra clave a buscar: ").strip().lower()

# Procesar datos y realizar búsqueda e impresión de los 5 con mayor frecuencia
resultados_procesados = procesar_datos(datos_providenciados)
buscar_e_imprimir(resultados_procesados, diccionario_documentos, palabra_clave)

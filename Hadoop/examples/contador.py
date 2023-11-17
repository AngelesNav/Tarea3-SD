#!/bin/bash

# Definir las carpetas de entrada
INPUT_FOLDER1="carpeta1"
INPUT_FOLDER2="carpeta2"

# Definir el directorio de salida
OUTPUT_DIR="output"
mkdir -p $OUTPUT_DIR

# Archivo para almacenar todos los resultados
RESULT_FILE="resultados_contador_simple.txt"

# Limpiar o crear el archivo de resultados
> $RESULT_FILE

# Ejecutar el script mapper en todos los archivos de la carpeta 1
for file in $INPUT_FOLDER1/*.txt; do
    filename=$(basename -- "$file")
    echo "Procesando archivo: $filename"
    cat $file | python mapper.py $filename > $OUTPUT_DIR/$filename.mapped
    cat $OUTPUT_DIR/$filename.mapped >> $RESULT_FILE
done

# Ejecutar el script mapper en todos los archivos de la carpeta 2
for file in $INPUT_FOLDER2/*.txt; do
    filename=$(basename -- "$file")
    echo "Procesando archivo: $filename"
    cat $file | python mapper.py $filename > $OUTPUT_DIR/$filename.mapped
    cat $OUTPUT_DIR/$filename.mapped >> $RESULT_FILE
done


echo "Resultados guardados en $RESULT_FILE"

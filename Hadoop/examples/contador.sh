#!/bin/bash

# Archivo para almacenar todos los resultados
RESULT_FILE="resultados_contador_simple.txt"

# Limpiar o crear el archivo de resultados
> $RESULT_FILE

# Ejecutar el script mapper en todos los archivos de la carpeta 1
for file in carpeta1/*.txt; do
    filename=$(basename -- "$file")
    echo "Procesando archivo: $filename"
    cat $file | python mapper.py $filename >> $RESULT_FILE
done

# Ejecutar el script mapper en todos los archivos de la carpeta 2
for file in carpeta2/*.txt; do
    filename=$(basename -- "$file")
    echo "Procesando archivo: $filename"
    cat $file | python mapper.py $filename >> $RESULT_FILE
done

# Ejecutar el script reducer en el archivo de resultados
cat $RESULT_FILE | sort | python reducer.py > resultado_final.txt

echo "Resultados finales guardados en resultado_final.txt"


echo "Resultados guardados en $RESULT_FILE"


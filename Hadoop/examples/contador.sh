#!/bin/bash

# Archivo para almacenar todos los resultados de mapper
RESULT_FILE="mapper.txt"

# Limpiar o crear el archivo de resultados
> $RESULT_FILE

# Ejecutar el script mapper en todos los archivos de las carpetas
for file in carpeta1/*.txt carpeta2/*.txt; do
    filename=$(basename -- "$file")
    echo "Procesando archivo: $filename"
    cat $file | python mapper.py $filename >> $RESULT_FILE
done

# Ejecutar el script reducer en el archivo de resultados
cat $RESULT_FILE | sort | python reducer.py > resultado_final.txt

echo "Resultados finales guardados en resultado_final.txt"


echo "Resultados finales guardados en resultado_final.txt"


echo "Resultados guardados en $RESULT_FILE"


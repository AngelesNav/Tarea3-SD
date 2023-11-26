#!/usr/bin/env python
# -*-coding:utf-8 -*
import re
import sys
import os

for line in sys.stdin:
    line = re.sub(r'[\d]', '', line.strip())
    words = line.split()

    # Obtener el nombre del archivo actual
    file_name = os.environ['map_input_file']

    for word in words:
        word_lower = word.lower()
        word_cleaned = re.sub(r'[^a-zA-ZáéíóúñÑ\s]', '', word_lower)
        if word_cleaned:
            print('{}\t{}\t{}'.format(word_cleaned, file_name, 1))

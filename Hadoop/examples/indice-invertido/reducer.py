#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_count = 0
word = None

doc_count = {}
for line in sys.stdin:
    result = line.strip().split('\t')

    if len(result) == 3:
        word, file_path, count = result
        count = int(count)

        # Extraer el número del archivo desde el path
        file_number = file_path.split('/')[-1].split('.')[0]

        if word == current_word:
            doc_count[file_number] = doc_count.get(file_number, 0) + count
        else:
            if current_word:
                print('{}\t{}'.format(current_word, ', '.join(['({}, {})'.format(doc, count) for doc, count in doc_count.items()])))
            current_word = word
            doc_count = {file_number: count}

if current_word:
    print('{}\t{}'.format(current_word, ', '.join(['({}, {})'.format(doc, count) for doc, count in doc_count.items()])))
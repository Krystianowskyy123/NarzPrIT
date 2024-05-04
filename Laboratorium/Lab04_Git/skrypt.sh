#!/bin/bash

if [[ -z "$2" ]]; then
    num_files=100
else
    num_files=$2
fi

if [[ "$1" == "--date" ]]; then
    date
elif [[ "$1" == "--logs" ]]; then
    for ((i=1; i<=$num_files; i++)); do
        filename="log${i}.txt"
        echo "Nazwa pliku: $filename" > "$filename"
        echo "Nazwa skryptu: $0" >> "$filename"
        echo "Data: $(date)" >> "$filename"
    done 
else
    echo "Blad"
fi

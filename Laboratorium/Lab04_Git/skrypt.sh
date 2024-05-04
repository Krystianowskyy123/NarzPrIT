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
elif [[ "$1" == "--help" ]]; then
    echo "skrypt v.1.0"
    echo
    echo "Syntax: ./skrypt.sh [--date|--logs parm|--help]"
    echo "options:"
    echo "--date         show date"
    echo "--logs parm    create logs times parm"
    echo "--help         show this info"
else
    echo "Blad"
fi

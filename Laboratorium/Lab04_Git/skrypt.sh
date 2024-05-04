#!/bin/bash

if [[ -z "$2" ]]; then
    num_files=100
else
    num_files=$2
fi

while getopts ":hn:" option; do
   case $option in
      d)
        date;;
      h)
        echo "skrypt v.1.0"
        echo
        echo "Syntax: ./skrypt.sh [-d|-h|- parm|-e parm|--init|--date|--logs parm|--help|--error parm]"
        echo "options:"
        echo "--date | -d             show date"
        echo "--logs parm | -l parm   create logs times parm"
        echo "--help | -h             show this info"
        echo "--init                  clone repo"
        echo "-e parm | --error parm  create error logs times parm"
        exit;;
      l)
        for ((i=1; i<=$num_files; i++)); do
            filename="log${i}.txt"
            echo "Nazwa pliku: $filename" > "$filename"
            echo "Nazwa skryptu: $0" >> "$filename"
            echo "Data: $(date)" >> "$filename"
        done
        exit;;
      e)
        for ((i=1; i<=$num_files; i++)); do
            filename="error${i}/error${i}.txt"
            touch "${filename}"
        done;;
     \?)
         echo "Error: Invalid option"
         exit;;
   esac
done

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
    echo "Syntax: ./skrypt.sh [-d|-h|- parm|-e parm|--init|--date|--logs parm|--help|--error parm]"
    echo "options:"
    echo "--date | -d             show date"
    echo "--logs parm | -l parm   create logs times parm"
    echo "--help | -h             show this info"
    echo "--init                  clone repo"
    echo "-e parm | --error parm  create error logs times parm"
elif [[ "$1" == "--init" ]]; then
    git clone https://github.com/Krystianowskyy123/NarzPrIT ./repo
    export PATH="$PATH:$(pwd)/my_repo"
elif [[ "$1" == "--error" ]]; then
    for ((i=1; i<=$num_files; i++)); do
        filename="error${i}/error${i}.txt"
        touch "${filename}"
    done 
else
    echo "Blad"
fi

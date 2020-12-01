if [ "$#" != 2 ]
then
    echo 'Musia byt 2 argumenty'
    exit 1
fi

FROM="$1"
TO="$2"

seq "$FROM" "$TO" | paste -s -d '*' | bc

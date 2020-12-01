SUM=0

while read LINE
do
    let SUM=SUM+LINE

done

echo "$SUM"

# seq 1 10 | sed 's/\(.*\)/\1*\1/' | ./scitaj.sh

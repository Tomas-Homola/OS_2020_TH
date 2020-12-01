echo pocet argumentov je "$#"

echo 1.."$1"
echo 2.."$2"

echo vsetky argumenty $*

for ARG in "$@"
do
    echo argument "$ARG"
done

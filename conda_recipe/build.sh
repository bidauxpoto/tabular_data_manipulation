#!/bin/bash

#build.sh must be adapted to the logic in /src
#this small template is suitable for single file scripts
mkdir -p $PREFIX/bin/
cp fasta2tab.pl $PREFIX/bin/fasta2tab
cp tab2fasta.py $PREFIX/bin/tab2fasta
cp tab2matrix.py $PREFIX/bin/tab2fasta
cp set_expand.py $PREFIX/bin/set_expand
chmod -R +x $PREFIX/bin/

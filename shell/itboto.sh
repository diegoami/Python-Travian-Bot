#!/usr/local/bin/bash
(sleep $(($2)))

for ((i=0;i<=$1;i+=1)) ; do

    
    python -u doonce.py itaccount4.txt $i 2>&1 > ../public_html/travian/it4res.txt 
done   




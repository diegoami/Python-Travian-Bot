#!/usr/local/bin/bash
while true;
do
    python -u doonce.py itaccount.txt 2>&1 > ../public_html/travian/itres.txt 
    python -u doonce.py itaccount4.txt 2>&1 > ../public_html/travian/it4res.txt 
    python -u doonce.py itaccount9.txt 2>&1 > ../public_html/travian/it9res.txt 
done


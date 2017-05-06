#!/usr/bin/bash

while true;

do
	for ((i=0;i<=$1;i+=1)) ; do
	
	    
        python -u doonce.py itaccount4.txt $i 2>&1 > log/it4res.txt 
    done   
    (sleep $(($2 + ($RANDOM % 600))))
done


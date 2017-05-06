while true;
do
	python -u dbreport.py itaccount4.txt $1
	python -u dbreport.py itaccount9.txt $1
        sleep $2
done

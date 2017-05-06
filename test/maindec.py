#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_addestra, travian_caserma, travian_raid
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids


def do_troops():
    try:
        travian_addestra.addestradecurione(t10Arg=1)
    except:
        print "Addestra cavalleria non ha avuto successo "
    effettua_raids()


def do_build():
    minimo_livello = travian_resdorf.build_random_resource()
    if (minimo_livello > 0):
        travian_edifici.build_missing_edifici(minimo_livello)
        



accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))

 
while (1):
   

    login()
    do_troops() 
       
    
    sleepvalue = random.randint(10*60, 16*60)    
    print "Done!\nSleeping ..", sleepvalue
   
    time.sleep(sleepvalue )    
    
        
    
    
          
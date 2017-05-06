#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids, effettua_spade_raids, effettua_eduani_raids
from travian_risorse import get_risorse, get_magazzino, has_mercanti,get_villaggio_risorse, quantita_trasferire, init_coef
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi
from travian_mail import get_roberto, get_schiva, get_rinforza, get_fake

RAND1=180
RAND2=200

def manda_fake(xx, yy):
    print " XX = ", xx
    print " YY = ", yy
    
    print " FAKE ", xx, " ", yy
    travian_addestra.spediscitruppe(t1Arg=1, xArg= xx, yArg=yy)

sleepvalue = random.randint(RAND1*60, RAND2*60)    
print "First nSleeping ..", sleepvalue
#time.sleep(sleepvalue )  
    
accountfile = sys.argv[1]
getaccount(os.path.join("config",accountfile ))
init_coef()
loopcounter = 0
lista_fake=[]
try:
    print travian_account.fake_file 
    filefake=open(os.path.join("config",travian_account.fake_file ),'r')
    lista_fake=filefake.readlines()  
except:
    print "COULD NOT OPEN ", travian_account.fake_file 

while (1):
    loggedin = 0
    while (loggedin == 0):
        try:
            login()
            loggedin = 1
        except:
            print "Could not login, retrying ...."
            time.sleep(5)  
    try:
        if ((get_roberto() == 1) and (get_fake() == 1)):
            print "ROBERT FAKE ATTIVO"
            dictvills =  travian_villaggi.getvillaggi()
            dictvillkeys = dictvills.keys()
            dictvillkeys.sort()

            for vill in dictvillkeys:
                print "VILLO = "+vill  
                travian_villaggi.vaiavillaggio(dictvills, vill)   
                for fake in lista_fake:
                    fakesplit  = fake.split(" ")  
                    manda_fake(fakesplit[0],fakesplit[1])
                  
        else:
            print "ROBERT DISATTIVO!"
    except:
        print "ERROR DONT KNOW WHY"
        print sys.exc_info()
    sleepvalue = random.randint(RAND1*60, RAND2*60)    
    print "Done!\nSleeping ..", sleepvalue
    time.sleep(sleepvalue )  
    loopcounter = loopcounter+1  
    
    
          
#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids, effettua_spade_raids, effettua_eduani_raids
from travian_risorse import get_risorse, get_magazzino, has_mercanti,get_villaggio_risorse, quantita_trasferire
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi
from travian_messaggi import get_messaggi
from travian_spedisci import spedisci

accountfile = sys.argv[1]
getaccount(os.path.join("config",accountfile ))     

loggedin = 0

         
lista_bastardi = ["SuperMH","Multihunter4", "Multihunter2","Multihunter3","Multihunter","admin"]   
login()
while (1):
    for bastardo in lista_bastardi:
        result = spedisci("STRONZO",bastardo  )
        if (result == 1):
            print "SPEDITO !!!"
        time.sleep(200)
        print "sleeping..."

    
          
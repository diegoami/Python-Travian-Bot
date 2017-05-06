#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")
from sgmllib import SGMLParser
import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raid
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids
from travian_risorse import get_risorse, get_magazzino, has_mercanti,get_villaggio_risorse, quantita_trasferire
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi
import travian_carta
import travian_anavill, travian_anaally
import travian_anapla
import travian_language
import travian_raidmap

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))


login()


allvillaggilinks = travian_carta.get_all_villaggi(-11,-226,0)
print allvillaggilinks
raidlines = []



for villaggiolink in allvillaggilinks:
    villaggio =  travian_anavill.get_villaggio(travian_account.start_page+villaggiolink )
    raidlines.append(villaggio)
print raidlines
raids = travian_raidmap.setupraids(raidlines, -11, -226)  

print raids
possibleraids = travian_raidmap.get_possible_raids(60)    
print possibleraids
        
    
    
          
#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raid
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids
from travian_risorse import get_riepilogo,get_risorse, get_magazzino, has_mercanti, get_villaggio_risorse, quantita_trasferire, sotto_attacco
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi



accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))

def do_sposta_tutto(villo):
        vrdict = get_villaggio_risorse()
        rv = vrdict[villo]
        ovs = get_other_villaggi(villo)
        for ov in ovs.keys():
            if (not(sotto_attacco(ov))):
                spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-50, dnameArg=ov )
                break



login()
dictvills =  travian_villaggi.getvillaggi()

riepilogdict = get_riepilogo()
risorsedict = get_risorse()
magazzinodict = get_magazzino()
vrdict = get_villaggio_risorse()

print riepilogdict
print risorsedict

print magazzinodict
print vrdict
print sotto_attacco("AA")


print sotto_attacco("AB")
print sotto_attacco("AD")
print sotto_attacco("AC")
travian_villaggi.vaiavillaggio(dictvills, "AD")
do_sposta_tutto("AD")






  
    
        
    
    
          
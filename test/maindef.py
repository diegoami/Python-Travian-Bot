#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids
from travian_risorse import get_risorse, get_magazzino, has_mercanti,get_villaggio_risorse, quantita_trasferire
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi

def do_setup_farm():
    print "Setting farms up..."
    
    allvillaggilinks = travian_carta.get_all_villaggi(int(travian_account.xp_start),int(travian_account.yp_start),5)
    raidlines = []
    for villaggiolink in allvillaggilinks:
        try:
            villaggio =  travian_anavill.get_villaggio(travian_account.start_page+villaggiolink )
            raidlines.append(villaggio)
        except:
            print villaggiolink +" could not be parsed "
            
    raids = travian_raidmap.setupraids(raidlines,int(travian_account.xp_start),int(travian_account.yp_start))  
    print raids


def do_dec():
    try:
        travian_addestra.addestradecurione(t10Arg=1)
    except:
        print "Addestra cavalleria non ha avuto successo "

def do_troops():
    try:
        truppetot = travian_caserma.get_truppe()
        if (truppetot[3] >10):
            effettua_raids()
    except:
        print "Effettua Raids non ha avuto successo "
    try:
        truppetot = travian_caserma.get_truppe()
        if (truppetot[3] < 120):
            pass
        else:
            travian_addestra.addestracavalleria(t5Arg=1)
            travian_addestra.addestrafanti(t1Arg=2)

    except:
        print "Addestra cavalleria non ha avuto successo "
        
    

def do_build():
    try:
        minimo_livello = travian_resdorf.build_random_resource()
    except:
        print "build random resource non ha avuto successo"
    try:
        if (minimo_livello > 0):
            travian_edifici.build_missing_edifici(minimo_livello)
    except:
        print "build missing edifici non ha avuto successo"
        
def do_sposta(villo):
    if (has_mercanti(villo)):
        vrdict = get_villaggio_risorse()
        ovs = get_other_villaggi(villo)
        for ov in ovs.keys():
            qta = quantita_trasferire(vrdict,villo ,ov)
            spediscimerce(r1Arg=qta[0],r2Arg=qta[1], r3Arg=qta[2],r4Arg=qta[3], dnameArg=ov )

def do_all(villo):
    do_sposta(villo)
    do_build()
    do_troops() 
    
def do_all_here():
    do_build()
    do_troops()    

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))
loopcounter = 0
while (1):
   
   
    login()
   
    try:
        dictvills =  travian_villaggi.getvillaggi()
        if (len(dictvills) > 0):
            for vill in dictvills.keys():
               travian_villaggi.vaiavillaggio(dictvills, vill)
               do_all(vill)
        else:
            do_all_here()      
    except:
        print "Loop non ha avuto successo"
    sleepvalue = random.randint(15*60, 18*60)    
    print "Done!\nSleeping ..", sleepvalue
    try:
        print "Loopcounter = "+str(loopcounter)
        if (loopcounter % 200 == 10):
            do_setup_farm()
    
       
    except:
        print "error setting up farms"
    time.sleep(sleepvalue )  
    loopcounter = loopcounter+1  
    
        
    
    
          
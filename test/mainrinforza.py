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
from travian_mail import get_roberto, get_schiva, get_rinforza



ATTACCOBEFORE = 150*60
def devo_spostare():
    attaccoquando = travian_caserma.get_primo_attacco()
    if ((attaccoquando > 0) and (attaccoquando < ATTACCOBEFORE)):
        print "ATTACCO TRA " , attaccoquando
        print "INTERVENTO NECESSARIO !"
        return 1
    elif (attaccoquando > 0):
        print "ATTACCO TRA " , attaccoquando
        print "INTERVENTO NON NECESSARIO !"
        return 0
    else:
        return 0
    
def rinforza_truppe():
    travian_addestra.spedisci_difesa(travian_account.xfuga,travian_account.yfuga)
    
def sposta_se_necessario_solo():
    if (devo_spostare()):
        sposta_truppe()
        
def do_build():
    minimo_livello = travian_resdorf.build_random_resource()

def sposta_se_necessario(villo):
    if (villo.find(travian_account.villo_rinforzo) == -1):
        rinforza_truppe()
            
    travian_addestra.addestrafanti(2,0,0)
    travian_addestra.addestracavalleria(0,0,1)
        
def do_sposta_merce(villo):
   
    vrdict = get_villaggio_risorse()
    ovs = get_other_villaggi(villo)
    for ov in ovs.keys():
        sommamerce = 0
        while (1):
            qta = quantita_trasferire(vrdict,villo ,ov)
            print qta
            sommamerce = qta[0]+qta[1]+qta[2]+qta[3]
            if (sommamerce > 0):
                print "ADESSO SPEDISCO ",qta 
                spediscimerce(r1Arg=qta[0],r2Arg=qta[1], r3Arg=qta[2],r4Arg=qta[3], dnameArg=ov )
                break
            else: 
                break

def do_all(villo):
    sposta_se_necessario(villo)
    
def do_all_here():
    sposta_se_necessario_solo()
    
    

    
accountfile = sys.argv[1]
getaccount(os.path.join("config",accountfile ))
init_coef()
loopcounter = 0
lista_schivaggi=[]
try:
    fileschive=open(os.path.join("config",travian_account.schiva_file ),'r')
    lista_schivaggi=fileschive.readlines()  
except:
    print "COULD NOT OPEN ", travian_account.schiva_file
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
        if ((get_roberto() == 1) and (get_rinforza() ==1)):
            print "ROBERT RINFORZI ATTIVO"
            dictvills =  travian_villaggi.getvillaggi()
            if (len(dictvills) > 0):
                dictvillkeys = dictvills.keys()
                dictvillkeys.sort()
                icounter = 0
                for vill in dictvillkeys:
        
                   schivaggio = lista_schivaggi[icounter]
                   schivaggiosplits = schivaggio.split(" ")
                   travian_account.xfuga = int(schivaggiosplits[1])
                   travian_account.yfuga = int(schivaggiosplits[2])
        
                   travian_villaggi.vaiavillaggio(dictvills, vill)
                   time.sleep(1)  
                   do_all(vill)
                   icounter = icounter + 1
                   
            else:
                do_all_here()      
        else:
            print "ROBERT DISATTIVO!"
    except:
        print "ERROR DONT KNOW WHY"
        print sys.exc_info()
    sleepvalue = random.randint(26*60, 29*60)    
    print "Done!\nSleeping ..", sleepvalue
    time.sleep(sleepvalue )  
    loopcounter = loopcounter+1  
    
    
          
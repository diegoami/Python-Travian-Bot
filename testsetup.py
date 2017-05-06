#!/usr/bin/env python
import time,sys,os,random, string, traceback
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi 
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions



current_villo=""
loopcounter  = 0


def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()



def do_troops():
    try:
        if ((loopcounter % travian_account.frequency == 0) or (travian_schiva.devo_spostare(current_villo))):
            print "EFFETTUO RAID"
            travian_troopactions.effettua_raids(travian_account.methodo_raid)
        else:
            print "SALTO RAID"
        
    except:
        print " ERRORE NELL'EFFETTUARE I RAIDS "
        traceback.print_exc()
    try:
        travian_troopactions.effettua_truppe(current_villo,travian_account.methodo_truppe)
    except:
        print " ERRORE NEL CREARE TRUPPE"
        traceback.print_exc()
        
    try:
        travian_troopactions.effettua_attacchi(current_villo)
    except:
        print " ERRORE NEL CREARE TRUPPE"
        traceback.print_exc()
        
    try:
        print "EFFETTUA RICERCA ?"
        travian_troopactions.effettua_tutte_ricerche(current_villo)
    except:
        print "ERRORE NELL'EFFETTUARE RICERCA"
        traceback.print_exc()
        
     

def do_schiva():
    if ((travian_mail.get_schiva() == 1)):
        try:
            print "ROBERT SCHIVA ATTIVO"
            if (travian_schiva.devo_spostare(current_villo)):
                try:
                    travian_addestra.spedisci_tutto(travian_account.xfuga,travian_account.yfuga)
                except:
                    print "NON E' STATO POSSIBILE SPEDIRE VIA LE TRUPPE"
                    traceback.print_exc()
                try:    
                    travian_sposta.do_sposta_tutto(current_villo, loopcounter)
                except:
                    print "NON E' STATO POSSIBILE SPEDIRE VIA LA MERCE"
                    traceback.print_exc()
                    
        except:
            print "ERRORE NEL LOOP SCHIVA"
            traceback.print_exc()



def do_all(villo):
    travian_troopactions.effettua_dec(villo)
    if (travian_mail.get_festa() == 1):
        travian_party.fai_festa()
    travian_build.do_build(villo)
    do_troops() 

    do_schiva()
    if (villo != ""):
        travian_sposta.do_sposta(villo)
        travian_troopactions.do_rinforza(villo)
        

while (1):
    print "LOOPCOUNTER ",loopcounter
    leggi_config(sys.argv[1])
    travian_login.effettua_login()
    travian_mail.leggi_note()
    try:
        travian_setup.setupfarm_if_necessary(loopcounter, travian_account.raggio_raid)
    except:
        print "SET UP FARM NON HA AVUTO SUCCESSO"
        traceback.print_exc()
        
    if (travian_mail.get_roberto() == 1):
        dictvills =  travian_villaggi.getvillaggi()
        icounter = 0
        villkeys = dictvills.keys()
        villkeys.sort()
        if (len(dictvills) > 0):
            for vill in villkeys:
                try:
                    travian_villaggi.vaiavillaggio(dictvills, vill)
                    current_villo = vill
                    travian_schiva.set_fuga(icounter)
                    travian_effettuaraids.set_coords(icounter)
                    do_all(vill)
                except:
                    print "NON HO POTUTO EFFETTUARE AZIONI SUL VILLO ",vill
                    traceback.print_exc()
                    
                icounter  = icounter + 1
                
        else:
            travian_effettuaraids.set_coords(0)
            do_all("")      

    sleepvalue = random.randint(travian_account.intervallo_min*60, travian_account.intervallo_max*60)    
    print "Done!\nSleeping ..", sleepvalue
    loopcounter = loopcounter+1  
    time.sleep(sleepvalue )
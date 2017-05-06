#!/usr/bin/env python
import time,sys,os,random, string
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo"])

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
    getattr(travian_priorita, travian_account.methodo_setup)()
  
def do_schiva():
    if ((travian_mail.get_schiva() == 1)):
        print "ROBERT SCHIVA ATTIVO"
        if (1):
            travian_addestra.spedisci_tutto(travian_account.xfuga,travian_account.yfuga)
            travian_sposta.do_sposta_tutto(current_villo, loopcounter)


while (1):
    leggi_config(sys.argv[1])
    travian_login.effettua_login()
    travian_mail.leggi_note()
    travian_setup.setupfarm_if_necessary(loopcounter, travian_account.raggio_raid)
    if (travian_mail.get_roberto() == 1):
        dictvills =  travian_villaggi.getvillaggi()
        icounter = 0
        villkeys = dictvills.keys()
        villkeys.sort()
        if (len(dictvills) > 0):
            
            for vill in villkeys:
                if (icounter == 1):
                    travian_villaggi.vaiavillaggio(dictvills, vill)
                    current_villo = vill
                    travian_schiva.set_fuga(icounter)
                    do_schiva()
                icounter  = icounter + 1
        else:
            do_all("")      

    
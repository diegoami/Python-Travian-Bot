#!/usr/bin/env python
import time,sys,os,random, string, traceback
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi 
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions
import travian_messaggi
import logging
import logging.handlers
import travian_party


argfile = sys.argv[1]
#time.sleep(150*60)    
LOGFILE_NAME = 'spia.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')
logging.debug("START")


def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()

current_villo=""
loopcounter  = 0

leggi_config(sys.argv[1])

time.sleep(210*60)

travian_login.effettua_login()
dictvills =  travian_villaggi.getvillaggi()
villkeys = dictvills.keys()
villkeys.sort()
for vill in villkeys:
    try:
        travian_villaggi.vaiavillaggio(dictvills, vill)
        travian_addestra.spediscitruppe(t4Arg=22, xArg=87, yArg=74)
    except:
        traceback.print_exc()     
time.sleep(90*60)    
travian_login.effettua_login()
dictvills =  travian_villaggi.getvillaggi()
villkeys = dictvills.keys()
villkeys.sort()
for vill in villkeys:
    try:
        travian_villaggi.vaiavillaggio(dictvills, vill)
        travian_addestra.spediscitruppe(t4Arg=18, xArg=82, yArg=59)
    except:
        traceback.print_exc()     

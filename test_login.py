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



current_villo=""
loopcounter  = 0
LOGFILE_NAME = '../public_html/travian/'+sys.argv[1]+'.log'
ROLLLOGFILE_NAME = '../public_html/travian/R'+sys.argv[1]+'.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')

rhfdl= logging.handlers.RotatingFileHandler(filename=ROLLLOGFILE_NAME, maxBytes=1000000, backupCount=30);
rhfdl.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
rhfdl.setFormatter(formatter )
logging.getLogger('').addHandler(rhfdl)
farmsetup = 0

def is_in_corso():
    return travian_party.festa_in_corso()

def will_raid():
    return ( farmsetup and (loopcounter % travian_account.frequency == 0) or (travian_schiva.devo_spostare(current_villo)))

def check_festa():    
    cfesta = is_in_corso()  or (not(travian_mail.get_string("IN_CORSO") == 1)  or (travian_schiva.devo_spostare(current_villo)) ) 
    logging.debug("CFESTA ="+str(cfesta))
    return (cfesta)
    
def will_build():
    
    return check_festa() and ((loopcounter % travian_account.build_frequency == 0) or (travian_schiva.devo_spostare(current_villo)))

def will_troop():
    return check_festa() and ((loopcounter % travian_account.troop_frequency == 0) or (travian_schiva.devo_spostare(current_villo)))
    
    

def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()

def do_raids():
     try:
        if (will_raid()):
           
            travian_troopactions.effettua_raids(methodname = travian_account.methodo_raid, villo = current_villo)
            travian_troopactions.effettua_custom_raids(villo = current_villo)
            
        else:
            logging.debug( "SALTO RAID")
     except:
        logging.exception( " ERRORE NELL'EFFETTUARE I RAIDS ")

def do_troops():
   
        
    try:
        if (will_troop()):
            travian_troopactions.effettua_truppe(current_villo,travian_account.methodo_truppe)
    except:
        logging.exception(  " ERRORE NEL CREARE TRUPPE")
        
    try:
        if (will_raid()):
            travian_troopactions.effettua_attacchi(current_villo)
    except:
        logging.exception(  " ERRORE NEL CREARE TRUPPE")
        
    try:
        logging.debug(  "EFFETTUA RICERCA ?")
        
        travian_troopactions.effettua_tutte_ricerche(current_villo)
    except:
        logging.exception(  "ERRORE NELL'EFFETTUARE RICERCA")
        
    try:
        logging.debug(  "EFFETTUA FAKES?")
        
        travian_troopactions.effettua_fakes(current_villo)
    except:
        logging.exception(  "ERRORE NELL'EFFETTUARE FAKES")
     

def do_schiva():
    if ((travian_mail.get_schiva() == 1)):
        try:
            logging.debug( "ROBERT SCHIVA ATTIVO")
            if (travian_schiva.devo_spostare(current_villo)):
                try:
                    travian_addestra.spedisci_tutto(travian_account.xfuga,travian_account.yfuga)
                except:
                    logging.exception(  "NON E' STATO POSSIBILE SPEDIRE VIA LE TRUPPE")
                try:    
                    travian_sposta.do_sposta_tutto(current_villo, loopcounter)
                except:
                    logging.exception(  "NON E' STATO POSSIBILE SPEDIRE VIA LA MERCE")
                    
        except:
            logging.exception(  "ERRORE NEL LOOP SCHIVA")

def do_leggi_messaggi():
    try:
        if ((travian_mail.get_string("LEGGI") == 1)):
           travian_messaggi.leggi_messaggi(travian_account.nachrichten_page) 
    except:
        logging.exception(  "NON HO POTUTO LEGGERE I MESSAGGI")
    


def do_all(villo):
    travian_troopactions.effettua_dec(villo)
    travian_party.fai_feste_possibili(villo)
    if (will_build()):
        travian_build.do_build(villo)
    do_raids()
    do_troops() 

    do_schiva()
    if (villo != ""):
        if (will_build()):
            travian_sposta.do_azioni_mercato(villo)
        if (will_troop()):
            travian_troopactions.do_rinforza(villo)
        


leggi_config(sys.argv[1])
argfile = sys.argv[1]

    
logging.debug("---------------------- START -----------------------------");

travian_login.effettua_login()
travian_mail.leggi_note()
try:
    travian_setup.setupfarm_if_necessary(loopcounter, travian_account.raggio_raid)
    farmsetup = 1
except:
    logging.exception( "SET UP FARM NON HA AVUTO SUCCESSO")
    
if (travian_mail.get_roberto() == 1):
    do_leggi_messaggi()
    if (len(sys.argv) > 2):
        ccount = int(sys.argv[2])
    else:
        ccount = -1
    dictvills =  travian_villaggi.getvillaggi()
    icounter = 0
    villkeys = dictvills.keys()
    villkeys.sort()
    if (len(dictvills) > 0):
        for vill in villkeys:
            try:
                if ((ccount == -1) or (ccount == icounter)):

                    travian_villaggi.vaiavillaggio(dictvills, vill)
                    current_villo = vill
                    travian_schiva.set_fuga(icounter)
                    travian_effettuaraids.set_coords(icounter , vill)
                    do_all(vill)
                else:
                    pass
            except:
                logging.exception("NON HO POTUTO EFFETTUARE AZIONI SUL VILLO "+vill)
                
            icounter  = icounter + 1
            
    else:
        travian_effettuaraids.set_coords(0)
        do_all("")      

logging.debug("---------------------- END ---------------------------");


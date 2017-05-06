#!/usr/bin/env python
import time,sys,os,random, string
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi 
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions

import travian_attacco
import travian_mail
current_villo=""
loopcounter  = 0


        


def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    getattr(travian_priorita, travian_account.methodo_setup)()

leggi_config(sys.argv[1])
travian_login.effettua_login()
travian_mail.leggi_note()
attacchi_stringhe = travian_mail.ritorna_solo_stringa("ATTACCA_")
travian_attacco.leggi_attacchi(attacchi_stringhe)
travian_attacco.fai_generico_attacco()



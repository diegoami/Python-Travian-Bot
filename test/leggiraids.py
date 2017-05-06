#!/usr/bin/env python
import time,sys,os,random, string
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi , travian_ricercafarm
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions

import pickle

current_villo=""
loopcounter  = 0


def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    getattr(travian_priorita, travian_account.methodo_setup)()



leggi_config(sys.argv[1])
travian_login.effettua_login()
travian_mail.leggi_note()
pkl_file = open(travian_account.raids_file, 'rb')

raidlines = pickle.load(pkl_file)
print raidlines
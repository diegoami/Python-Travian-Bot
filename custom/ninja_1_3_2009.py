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
import datetime
import travian_addestra
import travian_party, time_util

LOGFILE_NAME = 'ninja.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')

argfile = sys.argv[1]

amidiff =  datetime.timedelta(hours=6, minutes=0, seconds= 0)

def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()

current_villo=""
loopcounter  = 0

leggi_config(sys.argv[1])

def ninja(arrivaltime, necessarytime, startvillo, func, **args):
    departuretime = arrivaltime - necessarytime - amidiff
    time_util.wait_until(departuretime)
    travian_login.effettua_login()
    dictvills =  travian_villaggi.getvillaggi()
    
    travian_villaggi.vaiavillaggio(dictvills, startvillo)
    funcninja(**args)



ntLegnagoLancere = datetime.timedelta(hours=0, minutes=42, seconds= 51)
ntOstigliaLancere = datetime.timedelta(hours=0, minutes=38, seconds= 20)
amidiff =  datetime.timedelta(hours=6, minutes=0, seconds= 0)

arrivaltime0 = datetime.datetime(2009,3,1,4,7,53)
arrivaltime0b = datetime.datetime(2009,3,1,4,7,54)

arrivaltime1 = datetime.datetime(2009,3,1,4,8,1)
arrivaltime1b = datetime.datetime(2009,3,1,4,8,2)

arrivaltime2 = datetime.datetime(2009,3,1,4,8,7)
arrivaltime2b = datetime.datetime(2009,3,1,4,8,8)



funcninja = getattr(travian_addestra, 'spediscitruppe')

ninja(arrivaltime0 , ntLegnagoLancere, "B1-Legnago", funcninja ,t1Arg=10, xArg=-17, yArg=-233, cArg=2)
ninja(arrivaltime0b , ntOstigliaLancere, "C1-Ostiglia", funcninja ,t1Arg=10, xArg=-17, yArg=-233, cArg=2)
     
ninja(arrivaltime1 , ntLegnagoLancere, "B1-Legnago", funcninja ,t1Arg=800, xArg=-17, yArg=-233, cArg=2)
ninja(arrivaltime1b , ntOstigliaLancere, "C1-Ostiglia", funcninja ,t1Arg=800, xArg=-17, yArg=-233, cArg=2)
ninja(arrivaltime2 , ntLegnagoLancere, "B1-Legnago", funcninja ,t1Arg=800, xArg=-17, yArg=-233, cArg=2)
ninja(arrivaltime2b , ntOstigliaLancere, "C1-Ostiglia", funcninja ,t1Arg=800, xArg=-17, yArg=-233, cArg=2)


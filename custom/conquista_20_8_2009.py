#!/usr/bin/env python


import time,sys,os,random, string, traceback
sys.path.extend(["modules","modules/conquista","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

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
import travian_conquista

LOGFILE_NAME = 'conquista.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')

argfile = "itaccount4.txt"



def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()

current_villo=""
loopcounter  = 0

leggi_config(argfile)



XGO = 49   
YGO = 250

yearGO = 2009
monthGO = 8
dayGO = 21
hourGO = 3
minuteGO = 46

arrival = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)

at3B = datetime.timedelta(hours=11, minutes=33, seconds= 38)
at4A = datetime.timedelta(hours=9, minutes=26, seconds= 43)
at1D = datetime.timedelta(hours=8, minutes=44, seconds= 17)
at1C = datetime.timedelta(hours=8, minutes=31, seconds= 26)

conquista = travian_conquista.conquista(arrival, XGO, YGO)
travian_login.login()
conquista.add_attacco(5,at3B,"3B-Posnan", t1Arg=40,  t9Arg=1,  cArg=3)
conquista.add_attacco(5,at4A,"4A-Hamburg", t3Arg=1000, t6Arg=1000,  t9Arg=2,  cArg=3)
conquista.add_attacco(5,at1D,"1D-Oldenburg", t1Arg=40,  t9Arg=1,  cArg=3)
conquista.add_attacco(5,at1C,"1C-Preetz", t1Arg=40,  t9Arg=1,  cArg=3)


print conquista.dump()
print conquista.get_attacchi()

conquista.esegui()

     

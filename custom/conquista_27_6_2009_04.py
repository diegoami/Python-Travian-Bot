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



XGO = 66    
YGO = 207

yearGO = 2009
monthGO = 6
dayGO = 28
hourGO = 5
minuteGO = 30   

arrival = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)
at1C = datetime.timedelta(hours=7, minutes=9, seconds= 32)
at1A = datetime.timedelta(hours=7, minutes=6, seconds= 39)
at4A = datetime.timedelta(hours=5, minutes=57, seconds= 46)
at5C = datetime.timedelta(hours=4, minutes=6, seconds= 1)
at2B = datetime.timedelta(hours=1, minutes=22, seconds= 28)



conquista = travian_conquista.conquista(arrival, XGO, YGO)
travian_login.login()

#conquista.add_attacco(10,at1C,"1C-Preetz", t1Arg=190, t9Arg=2, cArg=3)
#conquista.add_attacco(5,at1A,"1A-Kiel", t1Arg=160, t3Arg=170, t5Arg=400, t6Arg=60, t9Arg=2, cArg=3)
conquista.add_attacco(-5,at4A,"4A-Hamburg", t3Arg=10000, t6Arg= 4000, t7Arg=600, t8Arg=1000,  cArg=3, kataArg=25)
conquista.add_attacco(10,at5C,"5C-Carlsburg", t1Arg=100, t9Arg=2, cArg=3)
conquista.add_attacco(0,at2B,"2B-Rostock", t1Arg=10000, t6Arg= 2000, t7Arg=300, t8Arg=800, t9Arg=1,   cArg=3, kataArg=25)

print conquista.dump()
print conquista.get_attacchi()

conquista.esegui()

     

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

def ninja(arrivaltime, necessarytime, startvillo, func, **args):
    departuretime = arrivaltime - necessarytime - amidiff
    time_util.wait_until(departuretime)
    travian_login.effettua_login()
    dictvills =  travian_villaggi.getvillaggi()
    
    travian_villaggi.vaiavillaggio(dictvills, startvillo)
    func(**args)

XGO = 75    
YGO = 210

yearGO = 2009
monthGO = 5
dayGO = 26
hourGO = 7
minuteGO = 45   

ntKI = datetime.timedelta(hours=8, minutes=20, seconds= 23)
ntHA = datetime.timedelta(hours=6, minutes=49, seconds= 42)
ntCA = datetime.timedelta(hours=6, minutes=12, seconds= 36)
ntRO = datetime.timedelta(hours=1, minutes=47, seconds= 42)
ntSC = datetime.timedelta(hours=1, minutes=27, seconds= 28)



amidiff =  datetime.timedelta(hours=6, minutes=0, seconds= 0)

atKI = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,4)
atHA = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,4)
atSC = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,8)
atCA = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,12)
atRO = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)

funcninja = getattr(travian_addestra, 'spediscitruppe')
funcfesta = getattr(travian_party, 'fai_festa')

ninja(atKI, ntKI, "1A-Kiel", funcninja ,t1Arg=1800, t3Arg= 1400, t6Arg=500,  t7Arg=120, t9Arg= 1, xArg=XGO , yArg=YGO, cArg=3)
ninja(atHA, ntHA, "4A-Hamburg", funcninja , t1Arg=250,  t3Arg =1300,t6Arg=200, t7Arg=50, t9Arg= 2, xArg=XGO , yArg=YGO, cArg=3)
ninja(atCA, ntCA, "5C-Carlsburg", funcninja , t1Arg=50, t9Arg= 2, xArg=XGO , yArg=YGO, cArg=3)

ninja(atSC, ntSC, "2C-Schwerin", funcninja , t1Arg=40, t5Arg= 150, t9Arg= 1, xArg=XGO , yArg=YGO, cArg=3)
ninja(atRO, ntRO, "2B-Rostock", funcninja, t1Arg=2800,  t6Arg=600, t7Arg=50, t8Arg = 60, t9Arg= 1, xArg=XGO , yArg=YGO, cArg=3, kataArg="25")


     

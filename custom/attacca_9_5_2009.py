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

LOGFILE_NAME = 'attacca.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')

argfile = "itaccount.txt"



def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()


current_villo=""
loopcounter  = 0

leggi_config(argfile )

def ninja(arrivaltime, necessarytime, startvillo, func, **args):
    departuretime = arrivaltime - necessarytime - amidiff
    time_util.wait_until(departuretime)
    travian_login.effettua_login()
    dictvills =  travian_villaggi.getvillaggi()
    
    travian_villaggi.vaiavillaggio(dictvills, startvillo)
    funcninja(**args)

XGO = 56
YGO = -172

yearGO = 2009
monthGO = 5
dayGO = 9
hourGO = 19
minuteGO = 49

nt = datetime.timedelta(hours=17, minutes=53, seconds=17)

#ntRO =  datetime.timedelta(hours=10, minutes=48, seconds= 46)


amidiff =  datetime.timedelta(hours=6, minutes=0, seconds= 0)

#atRO =  datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)

at1 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)
at2 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,1)
at3 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,1)
at4 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,2)
at5 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,2)






funcninja = getattr(travian_addestra, 'spediscitruppe')


#ninja(atRO, ntRO, "2B-Rostock", funcninja ,t1Arg=5000,  t6Arg=700, t7Arg=170, t8Arg=150, t9Arg = 1, xArg=XGO , yArg=YGO, cArg=3, kataArg="25")
ninja(at1, nt, "G1-Buttapietra", funcninja ,  t2Arg=5000, t6Arg=1500, t7Arg=150,  t8Arg=200,  xArg=XGO , yArg=YGO, cArg=3,  kataArg="4", kata2Arg="4")
ninja(at2, nt, "G1-Buttapietra", funcninja ,  t2Arg=500, t6Arg=200, t7Arg=50,  t8Arg=100,  xArg=XGO , yArg=YGO, cArg=3,  kataArg="4", kata2Arg="4")
ninja(at3, nt, "G1-Buttapietra", funcninja ,  t2Arg=100, t6Arg=100, t7Arg=30,  t8Arg=100,  xArg=XGO , yArg=YGO, cArg=3,  kataArg="4", kata2Arg="4")

ninja(at4, nt, "G1-Buttapietra", funcninja ,  t2Arg=100, t6Arg=100, t7Arg=30,  t8Arg=100,  xArg=XGO , yArg=YGO, cArg=3,  kataArg="11", kata2Arg="15")
ninja(at5, nt, "G1-Buttapietra", funcninja ,  t2Arg=100, t6Arg=100, t7Arg=30,  t8Arg=100,  xArg=XGO , yArg=YGO, cArg=3,  kataArg="25", kata2Arg="16")
     

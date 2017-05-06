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

XGO = 28    
YGO = 237

yearGO = 2009
monthGO = 5
dayGO = 20
hourGO = 5
minuteGO = 45   

ntGE = datetime.timedelta(hours=9, minutes=13, seconds= 57)
ntKI = datetime.timedelta(hours=8, minutes=58, seconds= 31)
ntHA = datetime.timedelta(hours=8, minutes=53, seconds= 27)
ntFL = datetime.timedelta(hours=7, minutes=33, seconds= 16)
ntPFA = datetime.timedelta(hours=0, minutes=0, seconds= 0)

amidiff =  datetime.timedelta(hours=6, minutes=0, seconds= 0)

atHA = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,0)
atHA2 = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,8)
atGE = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,8)
atFL = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,12)
atKI = datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO,4)

atPFA =  datetime.datetime(yearGO,monthGO,dayGO,hourGO ,minuteGO-1,0)
funcninja = getattr(travian_addestra, 'spediscitruppe')
funcfesta = getattr(travian_party, 'fai_festa')

#ninja(atLU, ntLU, "4B-Luebeck", funcninja ,t1Arg=200, t5Arg= 200,  t9Arg= 1, xArg=XGO , yArg=YGO, cArg=3)
#ninja(atGE, ntGE, "6C-Gettysburg", funcninja ,  t1Arg=100,  t5Arg=300,   t9Arg=2, xArg=XGO , yArg=YGO, cArg=3)
#ninja(atKI, ntKI, "1A-Kiel", funcninja ,  t1Arg=2000, t3Arg=1000, t6Arg=500, t7Arg=200, t8Arg=200,  t9Arg=1, xArg=XGO , yArg=YGO, cArg=3,  kataArg="25", kata2Arg= "26")
#ninja(atHA, ntHA, "4A-Hamburg", funcninja , t3Arg=8000,   t6Arg=3000,  t7Arg=1000, xArg=XGO , yArg=YGO, cArg=3)
#ninja(atHA2, ntHA, "4A-Hamburg", funcninja , t1Arg=250,   t9Arg=2, xArg=XGO , yArg=YGO, cArg=3)
#ninja(atFL, ntFL, "1B-Flensburg", funcninja ,  t1Arg=100, t9Arg=1, xArg=XGO , yArg=YGO, cArg=3)
ninja(atPFA, ntPFA, "4A-Hamburg", funcfesta)


     

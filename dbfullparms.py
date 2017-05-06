#!/usr/bin/env python
import time,sys,os,random, string, traceback
import MySQLdb

sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi 
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions
import travian_leggireport



current_villo=""
loopcounter  = 0


def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()

leggi_config(sys.argv[1])
maxcarico =  int (sys.argv[2])
maxeff =  int (sys.argv[3])

travian_login.effettua_login()
travian_mail.leggi_note()
conn = MySQLdb.connect (host = "db72a.pair.com",
                            user = "clickit_4",
                            passwd = "ZbdRUGEf",
                            db = "clickit_travianit9")

c=conn.cursor()



c.execute("""SELECT playerdef FROM `FARM_LIST` WHERE CARICO_TOTALE > """+str(maxcarico)+""" AND EFFICIENCY > """+ str(maxeff)+""" AND SERVER_HOME = %s """, (travian_account.start_page,))

playerdefs = c.fetchall()
for playerdef in playerdefs:
    if (travian_mail.get_ask_string(playerdef[0] )):
        print playerdef
c.close()    

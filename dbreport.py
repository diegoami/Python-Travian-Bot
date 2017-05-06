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
howmanypages =  int (sys.argv[2])
startpage =  int (sys.argv[3])


travian_login.effettua_login()

 
allreports = travian_leggireport.get_all_reports(howmanypages,-1, startpage )

for report in allreports:
    try:
        print (travian_account.start_page,report.identif, report.playerdef, report.get_perdite_prezzo(), report.get_bottino_totale(), report.get_rentability(), report.get_efficiency(), report.reporttime)   
        if (report.get_carico_totale() >= 100):
            conn = MySQLdb.connect (host = "db72a.pair.com",
                                        user = "clickit_4",
                                        passwd = "ZbdRUGEf",
                                        db = "clickit_travianit9")
            c = conn.cursor()
            
            c.execute("""SELECT ID FROM BERICHTE WHERE ID = %s """, (report.identif,))
    
            maxid = c.fetchone()
            print "ID ", maxid
            maxidint = 0
            if (maxid != None):
                if (maxid[0] != None):
                    
                    print "FOUND ALREADY "+maxid[0]
            else:
                print "NOT FOUND INSERTING"
            
                c.execute("""INSERT INTO BERICHTE (SERVER_HOME, ID, PLAYERDEF, PERDITE, CARICO, BOTTINO, RENTABILITY, EFFICIENCY, REPORTTIME) VALUES( %s, %s, %s, %s, %s, %s, %s , %s , %s) """, 
                          (travian_account.start_page,report.identif, report.playerdef, report.get_perdite_prezzo(),report.get_carico_totale(), report.get_bottino_totale(), report.get_rentability(), report.get_efficiency(), report.reporttime))   
            
            c.close()   
        else : 
            print "SKIPPING" 
    except:
        print " ERRORE NEL INTERPRETARE IL REPORT "
        traceback.print_exc()

import sys,time, random, string, os
import urllib, urllib2, travian_account,travian_login,travian_info,socket_travian
import travian_url, travian_language, travian_caserma, travian_account, travian_mail
import travian_ricercafarm, travian_raidmap
import pickle, traceback
from sgmllib import SGMLParser
import logging




def setupfarm_if_necessary(loopcounter, raggio_raid):
    
    travian_repeat = int(travian_account.day_refresh*24*60/travian_account.intervallo_min)
    
    logging.debug( "Loopcounter = "+str(loopcounter))
    logging.debug( "Travian Repeat = "+str(travian_repeat - 2) )
    if (os.path.exists(travian_account.raids_file)):
        "pickle file exists, setting up not necessary..."
        pkl_file = open(travian_account.raids_file, 'rb')
    
        raidlines = pickle.load(pkl_file)
        logging.debug( "LETTI RAID ")
        pkl_file.close()

        if ((raidlines != None ) and (len (raidlines.raids) > 0)):
            travian_raidmap.setraids(raidlines)
        else:
            raids = travian_ricercafarm.do_setup_farm(raggio_raid)
            travian_raidmap.save_raids()
        return
            
    else:
        raids = travian_ricercafarm.do_setup_farm(raggio_raid)
        travian_raidmap.save_raids()
        return
    if (loopcounter % travian_repeat  == (travian_repeat - 2) ):
        logging.debug( " SETTING UP FARM ")
        raids = travian_ricercafarm.do_setup_farm(raggio_raid)
        travian_raidmap.save_raids()
   
                
  

    
            
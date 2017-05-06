import sys,time, random, string, traceback
import urllib, urllib2, travian_account,travian_login,travian_info,socket_travian
import travian_url, travian_language, travian_caserma, travian_mail
import travian_raidmap, travian_effettuaraids, travian_addestra, travian_ricercafarm
import travian_villaggi
import travian_attacco
import travian_accademia
import travian_anapla
import travian_anaally
import logging

from sgmllib import SGMLParser
MAX_DIFF = 1000

def effettua_custom_raids(villo):
    casf = villo + "CUSTOM_RAID"
    if ( (travian_mail.get_string(casf) ) ):
        logging.debug( "ROBERTO CUSTOM RAID")
        custarray = travian_mail.guarda_dopo_string(casf )
        for cust in custarray:
            logging.debug( "EXECUTING "+str(cust))
            raid_func = getattr(travian_effettuaraids, cust)
            raid_func()



def effettua_fakes(villo):
    effettua_fakes_gen(villo, "FAKE", t1Arg= 1)
    effettua_fakes_gen(villo, "BFAKE", t2Arg= 1)
    effettua_fakes_gen(villo, "CFAKE", t3Arg= 1)
    effettua_fakes_gen(villo, "DFAKE", t4Arg= 1)
    effettua_fakes_gen(villo, "EFAKE", t5Arg= 1)
    effettua_fakes_gen(villo, "GFAKE", t6Arg= 1)
    effettua_fakes_gen(villo, "HFAKE", t7Arg= 1)
    effettua_fakes_gen(villo, "IFAKE", t8Arg= 1)
    
    effettua_cap_gen(villo, "CAP", t1Arg = 1)


def effettua_fakes_gen(villo, strfake = "FAKE", **args):
    fasf = villo+strfake
    fakearray = travian_mail.guarda_dopo_string(fasf)

    

    for fakeply in fakearray:
        if (" " in fakeply ):
            coords = string.split(fakeply, " ")
            travian_addestra.spediscitruppe(xArg= int(coords[0]), yArg= int(coords[1]), cArg= 3, **args)
            
        else:  
            logging.debug("FAKE  PLAYERS ... "+fakeply )
        
            villi_ids = travian_anapla.get_villi('spieler.php?uid='+fakeply)
            logging.debug("FOUND VILLI "+str(villi_ids ))
    
            for villo in villi_ids:
                logging.debug("FAKE VILLO ... "+villo)
    
                travian_addestra.spediscitruppe(villoArg= villo , cArg= 3, **args)
                time.sleep(0.1)
            
def effettua_cap_gen(villo, strcap = "CAP", **args):
    logging.debug("EFFETTUA_CAP_GEN "+str(villo)+ ","+str(strcap))
    casf = villo+strcap
    caparray = travian_mail.guarda_dopo_string(casf )
    logging.debug("CAP "+str(caparray ))

    for capply in caparray:
        logging.debug("FAKE  CAPITALI  ... "+capply )
        
        players = travian_anaally.get_players('allianz.php?aid='+capply)
        logging.debug("FOUND PLAYERS"+str(players ))

        for player in players[1:]:
            
            capitale = travian_anapla.get_capitale('spieler.php?uid='+player)
            logging.debug("CAPITALE ... "+capitale )
            
            travian_addestra.spediscitruppe(villoArg= capitale , cArg= 3, **args)
            time.sleep(0.1)
            

    
def verify_attacco(villo):
    vasf = villo + "VERIFYATT"
    varray = travian_mail.guarda_dopo_string(vasf)
    
    attacchifuori = travian_caserma.get_attacchifuori()
    for vcont in varray:
        logging.debug("CHECKING "+vcont)
        if (not vcont in attacchifuori):
            logging.debug("WAITING FOR ATTACK ON "+vcont)
            return 0
        
    return 1

def effettua_raids(methodname, villo): 
    try:
        if (verify_attacco(villo)):
            raid_func = getattr(travian_effettuaraids, methodname)
            raid_simple_func= getattr(travian_effettuaraids, methodname+"_simple")
            rasf = villo + "RAID"
            sasf = villo + "SRAID"
            if ((travian_mail.get_raid() == 1) or (travian_mail.get_string(rasf) ) ):
                logging.debug( "ROBERTO RAIDA")
                if (travian_raidmap.available_raids() == 0):
                    travian_ricercafarm.do_setup_farm(travian_account.raggio_raid)
                    loopcounter = 1
               
                
                raid_func(villo)
                
            if (travian_mail.get_string(sasf) or (travian_mail.get_string("SRAID")) ):
                logging.debug( "ROBERTO SIMPLE RAIDS")
    
                raid_simple_func(villo)
        
            logging.debug( "EFFETTUA_RAIDS FINISHED")
        else:
            logging.debug("NECESSARY ATTACK NOT IN PROGRESS")
            
    except:
        logging.exception( "EFFETTUARE RAIDS NON E' STATO POSSIBILE")

    
    
    
def effettua_dec(current_villo):            
    try:
        decustr = current_villo + "DECU"
        if (travian_mail.get_string(decustr ) == 1):
            travian_addestra.addestradecurione(t10Arg=1)
    except:
        logging.exception("FARE DECURIONI NON E' STATO POSSIBILE")




def do_rinforza(villo):
    #rinforza_func = getattr(travian_addestra, "difesa_"+methodname)

    try:
        
        ovs = travian_villaggi.get_other_villaggi(villo)
        for ov in ovs.keys():
            strasf = villo+"T"+ov
            masf = "T"+ov
            strdasf = "DT"+ov
            dasf =  villo+"DT"+ov
            if (travian_mail.get_string(strasf) or travian_mail.get_string(masf) ):
                other_vill = ovs[ov]
                travian_addestra.spedisci_tutto(dnameArg=other_vill.villaggio_nome, cArg=2)
            if (travian_mail.get_string(strdasf) or travian_mail.get_string(dasf) ):
                other_vill = ovs[ov]
                travian_addestra.spedisci_tutto_defteut(dnameArg=other_vill.villaggio_nome, cArg=2)
    
                
    except:
        logging.exception( "RINFORZARE NON E' STATO POSSIBILE")
     
     
def get_maxmiss(villo):
    masf = villo + "MISSING"
   
    marray = travian_mail.guarda_dopo_string(masf)
    if (len(marray) == 0):
        return MAX_DIFF
    else:
        return int(marray[0])
       


def effettua_attacchi(villo): 
    try:
        attacchi_stringhe = travian_mail.ritorna_solo_stringa(villo+"ATTACCA_")
        travian_attacco.leggi_attacchi(attacchi_stringhe)
        maxmiss = get_maxmiss(villo)
        travian_attacco.fai_generico_attacco(villo, maxmiss)
    except:
        logging.exception( "EFFETTUARE ATTACCHI NON E' STATO POSSIBILE")

                
def effettua_truppe(current_villo, methodname):
    if (travian_mail.get_string("TRUPPA") ):
        try:
            logging.debug("TRUPPAGGIO....")
            times = 1
            trlin = travian_mail.guarda_dopo_string("TRUPPA")
            if (len(trlin) > 0 ):
                if (len(trlin[0]) > 0):
                    times = int(trlin[0])
            
            logging.debug("TIMES = "+str(times))
            attstr = current_villo + "XA"
            defstr = current_villo + "XD"
            raidstr = current_villo + "XR"
            palastr = current_villo + "XP"
            scoutstr = current_villo + "XS"
            catastr = current_villo + "XC"
            ariestr = current_villo + "XB"
            cavavastr = current_villo + "XV"
            fai_attacco = travian_mail.get_string(attstr) == 1
            fai_difesa = travian_mail.get_string(defstr ) == 1
            fai_raid = travian_mail.get_string(raidstr) == 1
            fai_pala= travian_mail.get_string(palastr) == 1
    
            fai_scout = travian_mail.get_string(scoutstr) == 1
            fai_cata = travian_mail.get_string(catastr) == 1
            fai_arie = travian_mail.get_string(ariestr) == 1
            fai_cavava = travian_mail.get_string(cavavastr) == 1
            truppe_func = getattr(travian_addestra, methodname)

            for index in range(0,times):
                #logging.debug("ON INDEX "+str(index))

                #logging.debug("TRYING TRUPPE_FUNC..."+" ".join( map(str,[fai_attacco, fai_difesa, fai_raid, fai_pala,fai_scout, fai_cata , fai_arie,fai_cavava ])))
                
                truppe_func(argAtt=fai_attacco, argDef=fai_difesa , argRaid = fai_raid, argPala = fai_pala, argScout = fai_scout, argCata = fai_cata, argArie = fai_arie, argCavava = fai_cavava)
            if (travian_mail.get_string("GRANDE")):
                gtimes = 1

                grlin = travian_mail.guarda_dopo_string("GRANDE")
                if (len(grlin) > 0 ):
                    if (len(grlin[0]) > 0):
                        gtimes = int(grlin[0])
                for index in range(0,gtimes):
                
                    truppe_func(argAtt=fai_attacco, argDef=fai_difesa , argRaid = fai_raid, argPala = fai_pala, argScout = fai_scout, argCata = fai_cata, argArie = fai_arie, argCavava = fai_cavava, argGrande= 1)
                
            logging.debug("EFFETTUA TRUPPE SUCCESSFUL")
    
        except:
            logging.exception( "FARE TRUPPE NON E' STATO POSSIBILE")

        

def effettua_gen_ricerca(villo, prefx, page):
    try:
        masf = villo +prefx
        if (travian_mail.get_string(masf ) ):
            ricarray = travian_mail.guarda_dopo_string(masf)
            for ric in ricarray:
                travian_accademia.fai_gen_ricerca(ric, page)
                
    except:
        logging.exception("RICERCARE NON E' STATO POSSIBILE")


        
def effettua_tutte_ricerche(villo):
    effettua_gen_ricerca(villo, "R",travian_account.accademia_page)
    effettua_gen_ricerca(villo, "F",travian_account.fabbro_page)
    effettua_gen_ricerca(villo, "A",travian_account.armeria_page)
    
            

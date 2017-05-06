import string, datetime, travian_language, travian_caserma, travian_raidmap, travian_addestra, travian_account, time
import logging
    
import travian_mail
import travian_villaggi
ORE_MAX=2
MIN_CHOICE=3

xp = 0
yp = 0
villoraid = ""
   
 
 
def get_dist():
    dasf = villoraid + "DIST"
    rasf = villoraid + "SLOWING"
    
    darray = travian_mail.guarda_dopo_string(dasf)
    if (len(darray) > 0):
        try:
            ddist = float(darray[0])
        
            
            if (travian_mail.get_string(rasf )):
                rist = travian_caserma.get_ultimo_ritorno()
                ddist = min(ddist,rist)
            logging.debug("RETURNING DIST "+str(ddist))
            return ddist
        except: 
            logging.exception( "get_dist() non ho trovato ")
            return 1
    else:
        return travian_account.max_hours
    
def get_att_coeff():
    casf = villoraid + "COEFF"
    carray = travian_mail.guarda_dopo_string(casf)
    if (len(carray) > 0):
        try:
            cff = float(carray[0])
            logging.debug("FOUND COEFF "+str(cff))
            return cff
        except: 
            logging.exception( "get_att_coeff() non ho trovato ")
            return 1
        
    else:
        return travian_account.attack_coeff  

  
def effettua_common(tlist, coeff, mintr, dist):  

    done = 0
    maxtries = 0
    dictvills =  travian_villaggi.getvillaggi()
    while ((done == 0) and (maxtries <= 40)):
        time.sleep(0.25)
        travian_villaggi.vaiavillaggio(dictvills, villoraid)
        truppeact = travian_caserma.get_available_truppe()
        logging.debug("Available troops = "+ str(truppeact))
        sumtr = 0
        for x in range(0,len(tlist)-1):
            truppeact[x] = truppeact[x] * tlist[x]
            sumtr = sumtr+truppeact[x]
        if (sumtr < mintr):
            logging.debug( "NOT ENOUGH TROOPS "+ str( sumtr ))
            return 
        possible_raids= travian_raidmap.get_possible_arg(sumtr , coeff, mintr, dist, villoraid)
        logging.debug( "FOUND "+ str( len(possible_raids)) +str( " POSSIBLE RAIDS "))
        if (len(possible_raids) >= travian_account.raids_length):
            raid_to_try=  possible_raids[0]
            logging.debug( "Raiding ...."+ str(raid_to_try.xp) + " "+str(raid_to_try.yp) )
            tnec = raid_to_try.truppe_necessarie_arg(coeff, mintr, villoraid)
            carga = 4
            if (raid_to_try.is_gallo()):
                carga = 3 
            tclist = tlist[:]
            for x in range(0,len(tclist)-1 ):
                tclist [x] = tclist [x] * tnec 
            if (raid_to_try.verify_proprietario()):
                travian_addestra.spediscitruppe(t1Arg=tclist[0], t2Arg=tclist[1], t3Arg=tclist[2], t4Arg=tclist[3], t5Arg=tclist[4], t6Arg=tclist[5],xArg=str(raid_to_try.xp), yArg=str(raid_to_try.yp), cArg= carga)
                logging.debug("SPEDISCI TRUPPE SUCCESSFUL !!!")
            raid_to_try.start_raid()    
            logging.debug("RAID DONE !!!")
            logging.debug("SAVING RAIDS....")
            travian_raidmap.save_raids()
            logging.debug("SUCCESSFULLY SAVED....")
            maxtries = maxtries + 1
            logging.debug("MAXTRIES=...."+str(maxtries))

        else :
            done = 1
    logging.debug("NO MORE RAIDS POSSIBLE!!!")
    
def effettua_mazze_raids_new():
    logging.debug("EFFETTUA_MAZZE_RAIDS_NEW")
    effettua_common([1,0,0,0,0,0,0],40,2,get_dist()*7)
    logging.debug("EFFETTUA_MAZZE_RAIDS_NEW FINISHED")


def effettua_cav_teuton_new():
    logging.debug("EFFETTUA_CAV_TEUTON_NEW")
    
    effettua_common([0,0,0,0,0,1,0],150,2,get_dist()*9)
    logging.debug("EFFETTUA_CAV_TEUTON_NEW FINISHED")

def effettua_asce_raids_new():
    logging.debug("EFFETTUA_ASCE_RAIDS_NEW")

    effettua_common([0,0,1,0,0,0,0],60,2,get_dist()*6)

    logging.debug("EFFETTUA_ASCE_RAIDS_NEW FINISHED")
    
def effettua_pala_raids_new():
    logging.debug("EFFETTUA_PALA_RAIDS_NEW")

    effettua_common([0,0,0,0,1,0,0],55,2,get_dist()*10)
    logging.debug("EFFETTUA_PALA_RAIDS_NEW FINISHED")

def effettua_fate_raids_new():

    effettua_common([0,0,0,1,0,0,0],90,2,get_dist()*19)
    
def effettua_lanceteut_raids_new():

    effettua_common([0,1,0,0,0,0,0],10,15,get_dist()*7)

def effettua_spade_raids_new():

    effettua_common([0,1,0,0,0,0,0],65,2,get_dist()*7)
def effettua_eduan_raids_new():

    effettua_common([0,0,0,0,0,1,0],140,2,get_dist()*13)

def set_coords(icounter, villo):
   
    global xp
    global yp
    global villoraid
    logging.debug("SETCOORDS "+str(icounter)+ " "+str(villo))
    villoraid  = villo
    curr_coords = travian_villaggi.get_curr_coords(icounter)
    print curr_coords
    xp , yp = curr_coords
    travian_raidmap.raid.xc = int(xp)
    travian_raidmap.raid.yc = int(yp)
    travian_raidmap.raid.ATT_COEFF =  get_att_coeff()
    
    

    
    
def raid_teutoni_simple():
    effettua_mazze_raids_new()
    if (not (travian_mail.get_string("DEFEND"))):
        effettua_pala_raids_new()
        
        
def raid_teutoni_nocav():
    effettua_mazze_raids_new()
    if (not (travian_mail.get_string("DEFEND"))):
        effettua_pala_raids_new()
        effettua_lanceteut_raids_new()    
    if (not (travian_mail.get_string("AATTA"))):
        effettua_asce_raids_new()
    
    
def raid_teutoni(villo):
    
    global villoraid
    villoraid = villo
    logging.debug("RAID_TEUTONI")
    effettua_mazze_raids_new()
    if (not (travian_mail.get_string("AATTA"))):
        effettua_asce_raids_new()
        effettua_cav_teuton_new()
    if (not (travian_mail.get_string("DEFEND"))):
        effettua_pala_raids_new()
        #effettua_lanceteut_raids_new()
    logging.debug("RAID_TEUTONI FINISHED")
    
def raid_galli(villo):

    effettua_fate_raids_new()
    effettua_spade_raids_new()
    effettua_eduan_raids_new()
    
def raid_galli_simple():
    raid_galli()
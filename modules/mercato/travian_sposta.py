import sys,time, random, traceback
import urllib, urllib2, travian_account,travian_login,travian_info,socket_travian
import travian_url
import travian_villaggi
import travian_risorse
import travian_mercato
import travian_mail
import travian_schiva
import logging
import string


from sgmllib import SGMLParser

def puo_spostare(villo):
    spasf = villo + "LASCIA_MERCANTI"
    return (not (travian_mail.get_string(spasf)))

def do_sposta_tutto(current_villo, loopcounter):
    if (not(puo_spostare(current_villo))):
        logging.debug("NON POSSO SPOSTARE DA "+current_villo)
        return
    
    dictvills = travian_villaggi.getvillaggi()
    if (travian_mail.get_string("SPOSTA")):
    
        try:
            if (current_villo != ''):
                villo = current_villo 
                vrdict = travian_risorse.get_villaggio_risorse()
                rv = vrdict[villo]
                ovs = travian_villaggi.get_other_villaggi(villo)
                for ov in ovs.keys():
                    if (not(travian_risorse.sotto_attacco(ov))):
                        travian_villaggi.vaiavillaggio(dictvills, current_villo)
                        ristrasf = travian_risorse.risorse_trasferibili(current_villo)

                        travian_mercato.spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-500, dnameArg=ov ,  maxrisorse= ristrasf)
                        break
                        return
                if (loopcounter > 0):
                    attacchi = travian_schiva.lista_attacchi
                    keymax = max(attacchi , key = lambda x: attacchi.get(x) )
                    travian_villaggi.vaiavillaggio(dictvills, current_villo)
                    ristrasf = travian_risorse.risorse_trasferibili(current_villo)

                    travian_mercato.spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-500, dnameArg=keymax,   maxrisorse= ristrasf)            
        except:
            logging.exception( "DO SPOSTA TUTTO NON HA AVUTO SUCCESSO")
        
       
  

def effettua_spedisci(villo, solograno = 0):
    dictvills = travian_villaggi.getvillaggi()
    if (not(puo_spostare(villo))):
        logging.debug("NON POSSO SPOSTARE DA "+villo)
        return


    fasf = villo+"SPEDISCI"
    if (solograno == 1):
        fasf= villo+"GRANO"    
    if (solograno == 2):
        fasf= villo+"RISORSE"    
        
    sparray = travian_mail.guarda_dopo_string(fasf)
     

    

    
    for spply in sparray:
        if (" " in spply  ):
            coords = string.split(spply , " ")
            vrdict = travian_risorse.get_villaggio_risorse()
            rv = vrdict[villo]
            travian_villaggi.vaiavillaggio(dictvills, villo)
            ristrasf = travian_risorse.risorse_trasferibili(villo)

            if (solograno == 0):
                travian_mercato.spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-50,  maxrisorse= ristrasf, xArg=coords[0], yArg=coords[1])
            elif (solograno == 1):
                travian_mercato.spediscimerce(r4Arg=rv.grano-50,  maxrisorse= ristrasf,xArg=coords[0], yArg=coords[1])
            elif (solograno ==2):
                travian_mercato.spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,maxrisorse= ristrasf, xArg=coords[0], yArg=coords[1])
            

    
        
def do_sposta(villo):
    dictvills = travian_villaggi.getvillaggi()

    if (not(puo_spostare(villo))):
        logging.debug("NON POSSO SPOSTARE DA "+villo)
        return
    try:
        ovs = travian_villaggi.get_other_villaggi(villo)
        for ov in ovs.keys():
            
            strasf = villo+"M"+ov
            masf = "M"+ov
            strgasf = villo+"G"+ov
            if (travian_mail.get_string("PUSH") and (travian_mail.get_string(strasf) or travian_mail.get_string(masf)) ):
                logging.debug("PUSHING")
                vrdict = travian_risorse.get_villaggio_risorse()
                rv = vrdict[villo]
                travian_villaggi.vaiavillaggio(dictvills, villo)
                ristrasf = travian_risorse.risorse_trasferibili(villo)
    
                if (travian_mail.get_string("SALVAFESTA")):
                    logging.debug("SAVING FOR PARTY....")
                    travian_mercato.spediscimerce(r1Arg=rv.legno-6400,r2Arg=rv.argilla-6650, r3Arg=rv.ferro-5940,r4Arg=rv.grano-1390, dnameArg=ov , maxrisorse= ristrasf)
                else:
                    travian_mercato.spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-50, dnameArg=ov , maxrisorse= ristrasf)
                return 
            if (travian_mail.get_string(strgasf)):
                vrdict = travian_risorse.get_villaggio_risorse()
                rv = vrdict[villo]
                grarray = travian_mail.guarda_dopo_string(strgasf+"-")
                
                mingrano = 50
    
                for grl in grarray:
                    if (grl == "X"):
                        mingrano = int(travian_mail.get_string("XGRANO"))
                    else:
                        mingrano=int(grl)
                ristrasf = travian_risorse.risorse_trasferibili(villo)
                travian_villaggi.vaiavillaggio(dictvills, villo)
                travian_mercato.spediscimerce(r4Arg=rv.grano-mingrano, dnameArg=ov,  maxrisorse= ristrasf )
            
        if (travian_mail.get_mercanti() == 1):
            if (1):

                if (travian_risorse.has_mercanti(villo) or (travian_mail.get_string("SEMPRE"))):
                    if (1):
                            
                        vrdict = travian_risorse.get_villaggio_risorse()
                        
                        for ov in ovs.keys():
                            rasf = villo+"R"+ov
                            r2asf = ov+"R"+villo
                            aasf = villo+"A"+ov
                            zasf = ov+"Z"+villo
                          
                            
                            if (travian_mail.get_string(rasf) or travian_mail.get_string(r2asf) or travian_mail.get_string(aasf) or travian_mail.get_string(zasf)):
                                logging.debug(" FOUND COMBINATION "+villo+" TO "+ ov)
                                qta = travian_risorse.quantita_trasferire(vrdict,villo ,ov)
                                logging.debug(" QUANTITA TRASFERIRE "+str(qta))

                                if (qta != None):
                                    travian_villaggi.vaiavillaggio(dictvills, villo)
                                    ristrasf = travian_risorse.risorse_trasferibili(villo)
                                    travian_mercato.spediscimerce(r1Arg=qta[0],r2Arg=qta[1], r3Arg=qta[2],r4Arg=qta[3], dnameArg=ov,  maxrisorse= ristrasf )
    except:
        logging.exception( "DO SPOSTA NON HA AVUTO SUCCESSO")
        
        
def do_azioni_mercato(villo):  
    effettua_spedisci(villo,0)
    effettua_spedisci(villo,1)
    effettua_spedisci(villo,2)
    do_sposta(villo)
    
        
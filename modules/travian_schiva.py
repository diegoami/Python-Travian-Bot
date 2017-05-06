import sys,time, random, string, os
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_url, travian_language, travian_caserma
import travian_mail
import logging
import traceback

ATTACCOBEFORE=40
lista_attacchi=dict()
lista_schivaggi=[]

def setup_schivaggi(filename):
   
    global lista_schivaggi

    try:
        fileschivename = os.path.join("config",filename)
     
        fileschive=open(fileschivename,'r')
     
        lista_schivaggi=fileschive.readlines()  
    except:
        logging.exception( "COULD NOT OPEN "+ filename)



def set_fuga(icounter):
    global lista_schivaggi
    if (icounter < len(lista_schivaggi)):
        schivaggio = lista_schivaggi[icounter]
        print schivaggio
        schivaggiosplits = schivaggio.split(" ")
        travian_account.xfuga = int(schivaggiosplits[1])
        travian_account.yfuga = int(schivaggiosplits[2])
    
def devo_spostare(current_villo):
 
    global lista_attacchi
    stput = current_villo+"IGNORA_SCHIVA"
    if (travian_mail.get_string(stput) == 1):
        logging.debug("STAYING PUT IN "+current_villo)
        return 0
    
    attaccoquando = travian_caserma.get_primo_attacco()
    attaccomax= 24*60*60*5
    if (attaccoquando > 0):
        attaccomax = attaccoquando
    schivasf = current_villo+"TEST_SCHIVA"
    
    if (travian_mail.get_string(schivasf ) == 1):
        logging.info("TESTA SCHIVAGGIO " + str(schivasf))
        return 1
    
    lista_attacchi[current_villo] = attaccomax 
    
    print lista_attacchi
    if ((attaccoquando > 0) and (attaccoquando < ATTACCOBEFORE*60)):
        logging.debug( "ATTACCO TRA " +str( attaccoquando))
        logging.debug( "INTERVENTO NECESSARIO !")
        return 1
    elif (attaccoquando > 0):
        logging.debug( "ATTACCO TRA " + str( attaccoquando))
        logging.debug( "INTERVENTO NON NECESSARIO !")
        return 0
    else:
        return 0
    
#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids, effettua_spade_raids, effettua_eduani_raids, effettua_mazze_raids_new
from travian_risorse import get_risorse, get_magazzino, has_mercanti,get_villaggio_risorse, quantita_trasferire, sotto_attacco
from travian_mercato import spediscimerce
from travian_villaggi import get_other_villaggi
from travian_party import fai_festa
from travian_accademia import fai_ricerca
from travian_mail import get_roberto, get_schiva, get_rinforza, get_raid, leggi_note, get_string, get_mercanti, get_build, get_festa, get_ricerca
import string

RAGGIO_RAID = 2
lista_schivaggi=[]
current_villo=""
ATTACCOBEFORE = 40*60
loopcounter  = 0
lista_attacchi =dict()
travian_raidmap.DONE_COEFF=200
travian_raidmap.DIST_COEFF=40
TRAVIAN_INTERVALLO_MIN=3
TRAVIAN_INTERVALLO_MAX=6

def setup_resources():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '1', string.upper(travian_language.campo_legno) : '2', 
                             string.upper(travian_language.campo_grano) : '3', string.upper(travian_language.miniera_ferro) : '4', 
                             string.upper(travian_language.centro_del_villaggio) : '8'  ,

                             string.upper(travian_language.magazzino) : '18', string.upper(travian_language.granaio) : '22',
                             string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '40',
                             string.upper(travian_language.accademia) : '6', string.upper(travian_language.fabbro) : '8',
                             string.upper(travian_language.scuderia) : '10', string.upper(travian_language.residence) : '15',
                             string.upper(travian_language.esperto_trappole) : '34',    string.upper(travian_language.mulino) : '40' ,
                             string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                             string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                             string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                             string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                             string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                             string.upper(travian_language.ambasciata) : '100000'
                             
                              }
        
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                             string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                             string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                             string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                             string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                             string.upper(travian_language.accademia) : '5', string.upper(travian_language.fabbro) : '3',
                             string.upper(travian_language.scuderia) : '3', string.upper(travian_language.residence) : '1',
                             string.upper(travian_language.esperto_trappole) : '1',    string.upper(travian_language.mulino) : '1' ,
                             string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                             string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                             string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                             string.upper(travian_language.armeria) : '1', string.upper(travian_language.officina) : '20',
                             string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                             string.upper(travian_language.ambasciata) : '1'
                             
                             }



def devo_spostare():
 
    attaccoquando = travian_caserma.get_primo_attacco()
    attaccomax= 24*60*60*5
    if (attaccoquando > 0):
        attaccomax = attaccoquando
            
    
    lista_attacchi[current_villo] = attaccomax 
    if ((attaccoquando > 0) and (attaccoquando < ATTACCOBEFORE)):
        print "ATTACCO TRA " , attaccoquando
        print "INTERVENTO NECESSARIO !"
        return 1
    elif (attaccoquando > 0):
        print "ATTACCO TRA " , attaccoquando
        print "INTERVENTO NON NECESSARIO !"
        return 0
    else:
        return 0
    
def sposta_truppe():
    travian_addestra.spedisci_tutto(travian_account.xfuga,travian_account.yfuga)
    
    
def sposta_se_necessario_solo():
    if (devo_spostare()):
        sposta_truppe()
        do_sposta_tutto()
    
    
def do_setup_farm():
    print "Setting farms up..."
   
    allvillaggilinks = travian_carta.get_all_villaggi(int(travian_account.xp_start),int(travian_account.yp_start),RAGGIO_RAID)
    raidlines = []

    login()
    for villaggiolink in allvillaggilinks:
        try:
            print " PARSING ", villaggiolink 
            villaggio =  travian_anavill.get_villaggio(travian_account.start_page+villaggiolink )
            raidlines.append(villaggio)
        except:
            login()
            print travian_account.start_page+villaggiolink +" could not be parsed "
            print sys.exc_info()
    raids = travian_raidmap.setupraids(raidlines,int(travian_account.xp_start),int(travian_account.yp_start))  
    print raids


def do_dec():
    decustr = current_villo + "DECU"
    if (get_string(decustr ) == 1):
        try:
            travian_addestra.addestradecurione(t10Arg=1)
        except:
            print "Addestra decurione non ha avuto successo "

def do_troops():
    if ((get_raid() == 1)):
        print "ROBERTO RAID"
        if (travian_raidmap.available_raids() == 0):
            do_setup_farm()
            loopcounter = 1
        try:
            truppetot = travian_caserma.get_truppe()
            truppeavail = travian_caserma.get_available_truppe()
            
            if (travian_account.raids_yesno =="yes"):
                if (devo_spostare()):
                    effettua_mazze_raids_new()
                elif (truppeavail[0] > 30):
                    if (get_string("OBIE")):
                        travian_addestra.spediscitruppe(t1Arg=10, xArg=13, yArg=156)
                    effettua_mazze_raids_new()
                    
                
                    
        except:
            print "Effettua Raids non ha avuto successo "
            print sys.exc_info()
            
    attstr = current_villo + "XA"
    defstr = current_villo + "XD"
    if (get_string(attstr) == 1):
        print "FOUND ", attstr
        travian_addestra.addestrafanti(t1Arg=1)       
        
    if (get_string(defstr) == 1):
        print "FOUND ", defstr
        travian_addestra.addestrafanti(t2Arg=1)       
            

def do_build():
    if (get_build() == 1):
        print "BUILD ATTIVO"
        minimo_livello = travian_resdorf.build_random_resource()
        if (get_string("BUILD_NEW")):
            if (minimo_livello > 0):
                travian_edifici.build_missing_edifici(minimo_livello)
        
def do_sposta(villo):
    if (get_mercanti() == 1):
        if (has_mercanti(villo)):
            vrdict = get_villaggio_risorse()
            ovs = get_other_villaggi(villo)
            for ov in ovs.keys():
                qta = quantita_trasferire(vrdict,villo ,ov)
                if (qta != None):
                    spediscimerce(r1Arg=qta[0],r2Arg=qta[1], r3Arg=qta[2],r4Arg=qta[3], dnameArg=ov )

def do_sposta_tutto():
    if (current_villo != ""):
        villo = current_villo 
        vrdict = get_villaggio_risorse()
        rv = vrdict[villo]
        ovs = get_other_villaggi(villo)
        for ov in ovs.keys():
            if (not(sotto_attacco(ov))):
                spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-50, dnameArg=ov )
                break
                return
        if (loopcounter > 0):
            keymax = max(lista_attacchi , key = lambda x: lista_attacchi.get(x) )
            spediscimerce(r1Arg=rv.legno,r2Arg=rv.argilla, r3Arg=rv.ferro,r4Arg=rv.grano-50, dnameArg=keymax  )            
    
def do_schiva():
    print "DO_SCHIVA ?"
    if ((get_schiva() == 1)):
        print "ROBERT SCHIVA ATTIVO"
        sposta_se_necessario_solo()
    
    

def do_all(villo):
    do_dec()
    
    do_build()
    do_troops() 
    if (get_festa() == 1):
        fai_festa()
    if (get_ricerca() == 1):
        fai_ricerca()
    do_schiva()
    do_sposta(villo)
    
def do_all_here():
    do_dec()
    do_build()


    do_troops()
    if (get_festa() == 1):
        fai_festa()
    if (get_ricerca() == 1):
        fai_ricerca()
    do_schiva()

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))
setup_resources()
loopcounter = 0
try:
    fileschive=open(os.path.join("config",travian_account.schiva_file ),'r')
    lista_schivaggi=fileschive.readlines()  
except:
    print "COULD NOT OPEN ", travian_account.schiva_file
while (1):
    
    loggedin = 0
    while (loggedin == 0):
        try:
        
            login()
            loggedin = 1
        except:
            print "Could not login, retrying ...."
            time.sleep(5)  
            
    try:
        print "Loopcounter = "+str(loopcounter)
        if (loopcounter % 1000 == 0):
            if (travian_account.raids_yesno =="yes"):
                if (get_raid()):
                    do_setup_farm()
    except:
        print "error setting up farms"
        print sys.exc_info()
    leggi_note()
    if (get_roberto() == 1):
        dictvills =  travian_villaggi.getvillaggi()
        icounter = 0
        if (len(dictvills) > 0):
            for vill in dictvills.keys():
               travian_villaggi.vaiavillaggio(dictvills, vill)
               current_villo = vill
               schivaggio = lista_schivaggi[icounter]
               schivaggiosplits = schivaggio.split(" ")
               travian_account.xfuga = int(schivaggiosplits[1])
               travian_account.yfuga = int(schivaggiosplits[2])
    
               do_all(vill)
               icounter  = icounter + 1
        else:
            do_all_here()      

    sleepvalue = random.randint(TRAVIAN_INTERVALLO_MIN*60, TRAVIAN_INTERVALLO_MAX*60)    
    print lista_attacchi
    print "Done!\nSleeping ..", sleepvalue
    loopcounter = loopcounter+1  
    

    time.sleep(sleepvalue )
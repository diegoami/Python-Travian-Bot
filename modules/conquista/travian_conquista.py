import time,sys,os,random, string, traceback

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


dictstr = dict({'t1Arg' :  'MAZZE', 't2Arg' :  'LANCIE' , 't3Arg' :  'ASCE' , 
                't4Arg' :  'SPIE', 't5Arg' :  'PALADINI', 't6Arg' :  'CAV TEUTONICA', 
                't7Arg' : 'ARIETI', 't8Arg' : 'CATAPULTE', 't9Arg' : 'SENATORE',
                't10Arg' : 'DECURIONE', 't11Arg' : 'EROE', 'kataArg' : 'OBIETTIVO', 'kata2Arg' : 'OBIETTIVO', 'cArg' : 'ATTACCO'} )
class conquista:
    def __init__(self,arrtime, xg, yg):
        self.arrtime= arrtime
        self.xg = xg
        self.yg = yg
        self.attacchi = []
       
    def __repr__(self):
        return ("conquista arriva alle "+self.tag+",rank="+self.rank+",punti="+self.punti+",membri="+self.membri+")")

    def add_attacco(self, delaysec, durata, villpartenza, **attackargs):
        dicts = travian_villaggi.getvillaggi()
        if (dicts.has_key(villpartenza)):
            delay = datetime.timedelta(seconds=delaysec)
            arrivo = self.arrtime+delay
            attaccoAdd = attacco(arrivo, durata, villpartenza, self.xg, self.yg, **attackargs)
            self.attacchi.append(attaccoAdd)
        else:
            logging.error("VILLO "+villpartenza + " NON ESISTE ")
    
    def dump(self):
        dumptotal = ""
        self.attacchi.sort()
        for attacco in self.attacchi:
            dumptotal = dumptotal +  attacco.dump() + "\n\n"
        return dumptotal
        
    def get_attacchi(self):
        self.attacchi.sort()
        return self.attacchi
    
    def esegui(self):
        self.attacchi.sort()
        for attacco in self.attacchi:
            attacco.esegui()
        
        
class attacco:
    def __init__(self,arrivo, durata, villopartenza , xArg, yArg, **attackargs ):
        self.arrivo = arrivo
        self.durata = durata
        self.partenza = self.arrivo-self.durata
        
        self.villopartenza = villopartenza
        self.xArg = xArg 
        self.yArg = yArg
        self.attackargs = attackargs
        
    def __cmp__(self, other):
        if (other.partenza < self.partenza):
            return 1
        if (other.partenza > self.partenza):
            return -1
        return 0
        
        
    def dump(self):
        attaccostr = ""
        attaccostr = attaccostr + "ARRIVO = "+ str(self.arrivo) +"\n"
        attaccostr = attaccostr + "DURATA = "+ str(self.durata)+"\n"
        attaccostr = attaccostr + "PARTENZA = "+ str(self.partenza)+"\n"
        attaccostr = attaccostr + "villopartenza = "+ str(self.villopartenza)+"\n"
        attaccostr = attaccostr + "XGOAL = "+ str(self.xArg)+"\n"
        attaccostr = attaccostr + "YGOAL = "+ str(self.yArg)+"\n"
        keymap = self.attackargs.keys()
        keymap.sort()
        for attackargkey in keymap:
            
            attaccostr = attaccostr + str(dictstr[attackargkey]) +" = " + str(self.attackargs[attackargkey]) +"\n"
            
        return attaccostr   
        
    def esegui(self):
        time_util.wait_until(self.partenza)
        travian_login.effettua_login()
        dictvills =  travian_villaggi.getvillaggi()
    
        travian_villaggi.vaiavillaggio(dictvills, self.villopartenza)
        travian_addestra.spediscitruppe(xArg= self.xArg, yArg = self.yArg, **self.attackargs)
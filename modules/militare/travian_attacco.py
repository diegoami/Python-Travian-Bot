import string, datetime, travian_language, random
import  travian_account, travian_mail, pickle, travian_caserma
from math import hypot
import travian_addestra
import travian_mail
import logging
attacchi_dafare= []
num_attacchi_fatti = 0
class attacco:
    def __init__(self,nomemetodo, xb, yb):
        self.nomemetodo = nomemetodo
        self.xb = xb
        self.yb = yb
        self.aval_truppe = []
        self.maxdiff = 0
            
        
    def get_tuple_truppe(self):
        self.aval_truppe = travian_caserma.get_available_truppe()
        self.tutte_truppe = travian_caserma.get_tutte_truppe()
        
        diff_truppe =self.tutte_truppe[:]
        for x in range(0,len(diff_truppe) ):
            diff_truppe[x] = diff_truppe[x] - self.aval_truppe[x]
        return diff_truppe
        
    def in_villo(self, villo):
        return self.nomemetodo.find(villo) > -1
    def fai_attacco(self, maxdiff):
        self.maxdiff = maxdiff
        logging.debug( "FAI_ATTACCO")
        
        if (self.nomemetodo.find("ATTACCA_TEUTONE") > -1):
            self.attacca_teutone()
        if (self.nomemetodo.find("ATTACCA_ARIETI_TEUTONE") > -1):
            self.attacca_arieti_teutone()
        if (self.nomemetodo.find("ATTACCA_RAID_TEUTONE") > -1): 
            self.attacca_raid_teutone()
        if (self.nomemetodo.find("ATTACCA_FATE") > -1):
            self.attacca_fata()
        if (self.nomemetodo.find("ATTACCA_GALLO") > -1):
            self.attacca_gallo()
    
    def __repr__(self):
        return "METODO=" + self.nomemetodo + ",XB="+self.xb+",YB="+ self.yb
    def attacca_teutone(self):
        global num_attacchi_fatti
        ma, la, ax, ku, pa, ct, ar, ca, co, de, he, no = self.get_tuple_truppe()
        logging.debug(self.aval_truppe)
        diffact = (ma+ax+ct+ he +ar +ca)
        if diffact < self.maxdiff :
            travian_addestra.spediscitruppe( t1Arg = self.aval_truppe[0], t3Arg = self.aval_truppe[2],  t6Arg = self.aval_truppe[5], t11Arg = self.aval_truppe[10], cArg=3, xArg= self.xb,yArg = self.yb)
            num_attacchi_fatti = num_attacchi_fatti + 1
        else:
            logging.debug( "NON ABBASTANZA TRUPPE !")
            logging.debug( str(diffact) + " > "+ str(self.maxdiff))

        
    def attacca_arieti_teutone(self):
        global num_attacchi_fatti
        ma, la, ax, ku, pa, ct, ar, ca, co, de, he, no = self.get_tuple_truppe()
        logging.debug(self.aval_truppe)
        
        diffact = (ma+ax+ct+ he +ar )
        if diffact < self.maxdiff :
            travian_addestra.spediscitruppe( t1Arg = self.aval_truppe[0], t3Arg = self.aval_truppe[2],  t6Arg = self.aval_truppe[5], t7Arg=self.aval_truppe[6], t11Arg = self.aval_truppe[10], cArg=3, xArg= self.xb,yArg = self.yb)
            num_attacchi_fatti = num_attacchi_fatti + 1
        else:
            logging.debug( "NON ABBASTANZA TRUPPE !")
            logging.debug( str(diffact) + " > "+ str(self.maxdiff))

    def attacca_raid_teutone(self):
        global num_attacchi_fatti
        ma, la, ax, ku, pa, ct, ar, ca, co, de, he, no = self.get_tuple_truppe()
        diffact = (ma+ax+ct+ he )
        if diffact < self.maxdiff :
            travian_addestra.spediscitruppe( t1Arg = self.aval_truppe[0], t3Arg = self.aval_truppe[2], t6Arg = self.aval_truppe[5], t11Arg = self.aval_truppe[10], cArg=4, xArg= self.xb,yArg = self.yb)
            num_attacchi_fatti = num_attacchi_fatti + 1
        else:
            logging.debug( "NON ABBASTANZA TRUPPE !")
            logging.debug( str(diffact) + " > "+ str(self.maxdiff))
        
    def attacca_fata(self):
        global num_attacchi_fatti
       
        la, sp, sc, fa, cd, ca, ar, ca, ct, de, he, no = self.get_tuple_truppe()
        if (fa) < self.maxdiff  :
            travian_addestra.spediscitruppe(t4Arg = self.aval_truppe[3], t11Arg = self.aval_truppe[10], cArg=4, xArg= self.xb,yArg = self.yb)
            num_attacchi_fatti = num_attacchi_fatti + 1

        else:
            logging.debug( "NON ABBASTANZA TRUPPE !")
    
    def attacca_gallo(self):
        global num_attacchi_fatti

        la, sp, sc, fa, cd, ca, ar, ca, ct, de, he, no = self.get_tuple_truppe()
        if (la+ sp +fa +cd +ca +ar +ct+de+he+no) < self.maxdiff  :
            travian_addestra.spediscitruppe( t2Arg = self.aval_truppe[1], t4Arg = self.aval_truppe[3], t5Arg=self.aval_truppe[4], t6Arg = self.aval_truppe[5], t7Arg=self.aval_truppe[6], t8Arg=self.aval_truppe[7] , t10Arg=self.aval_truppe[9], t11Arg = self.aval_truppe[10], cArg=3, xArg= self.xb,yArg = self.yb)
            num_attacchi_fatti = num_attacchi_fatti + 1

        else:
            logging.debug( "NON ABBASTANZA TRUPPE !")

def fai_attacco(nomemetodo, xb, yb):        
    att = attacco(nomemetodo, xb, yb)
    att.attacca_teutone()
 
def prendi_attacco(villo): 
    global attacchi_dafare
    
    if (len(attacchi_dafare) > 0):
        if (villo == ""):
            item = attacchi_dafare.pop(random.randint(0,len(attacchi_dafare)-1))
            return item
        else:
            attacchi_villo = filter(lambda attacco_curr: attacco_curr.in_villo(villo), attacchi_dafare )
            
            if (len(attacchi_villo) > 0):
                item = attacchi_villo.pop(random.randint(0,len(attacchi_villo)-1))
                return item
                
    return None
            


def is_attacco_fatto():
    return (travian_mail.get_string("UNA_TANTUM") and (num_attacchi_fatti > 0))
    
def fai_generico_attacco(villo, maxdiff):
    global attacchi_dafare
   
    if (len(attacchi_dafare) > 0):
        attacco_preso = prendi_attacco(villo)
        if (attacco_preso != None):
            logging.debug( "ATTACCO "+ str( attacco_preso))
            attacco_preso.fai_attacco(maxdiff)
            
def leggi_attacchi(lista_attacchi_note):
    global attacchi_dafare
    
    attacchi_dafare = []
    for nota_attacco in lista_attacchi_note:
        logging.debug( "TRYING TO SPILT "+ str( nota_attacco))
            
        nomemetodo, xb, yb = string.split(nota_attacco," ")
        attacco_nuovo = attacco(nomemetodo, xb, yb)
        attacchi_dafare.append(attacco_nuovo)
    return attacchi_dafare

        
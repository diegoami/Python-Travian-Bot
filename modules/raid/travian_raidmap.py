import string, datetime, travian_language
import travian_account, travian_mail, pickle
import travian_carta, travian_anavill

from math import hypot
rl = None
import logging

DIST_COEEF=18
DONE_COEFF=500
POP_COEFF=8
ALL_COEFF=2
MIN_POP = 1


    
    
class raidlist:
    def __init__(self, raidslines,xb,yb):
        self.raids = []
        for raidline in raidslines:
            try: 
                currentraid = raid(raidline)
                self.raids.append(currentraid)
            except:
                logging.exception( "Could not add: "+raidline)
                
        self.raids.sort()  
        

    def __repr__(self):
        return self.raids.__repr__()
    
    def get_raids(self):
        return self.raids
    
    def sort_dist(self):
        self.raids.sort(self.dist_compare)
        
        
    def get_possible_all(self):
        self.sort_dist()
        possibili_raids = filter(lambda raid: travian_mail.get_ask_string(raid.giocatore), self.raids)
        return possibili_raids
        
    def get_possible_arg(self, units, coeff, mintr, maxdist,villo= ""):
        self.raids.sort()
 
        possibili_raids = filter(lambda raid: raid.is_possible( units, coeff, mintr, maxdist, villo), self.raids )
        
        return possibili_raids
    
    def dist_compare(self,x, y):
        return cmp(x.get_distanza(), y.get_distanza())


class raid:
    xc = 0
    yc = 0
    ATT_COEFF = travian_account.attack_coeff  
    
    def __init__(self,villaggioDati):

        #self.abitanti = int(villaggioDati.abitanti)
        self.giocatore = villaggioDati.proprietario
        #self.villaggio = villaggioDati.nomevillaggio
        #self.alleanza= villaggioDati.alleanza
        #self.puntialleanza = int(villaggioDati.puntialleanza)
        self.popolazione= int(villaggioDati.popolazione)
        #self.crescita= 0
        self.id = ""
        self.tribu = villaggioDati.popolo
        self.xp = int(villaggioDati.xp)
        self.yp = int(villaggioDati.yp)
                             
        #self.distanza = 0
        self.done = 0
        #self.lastraid = None
        
    def get_distanza(self):
        distx = self.xp-raid.xc
        disty = self.yp-raid.yc
        distanza = hypot(distx,disty)
        return distanza
        
    def get_add_coeff(self, villo = ""):
        if (travian_mail.get_ask_string(self.giocatore)):
           giocarr = travian_mail.guarda_dopo_string('*'+self.giocatore+'*')
           
           giocarrvillo = travian_mail.guarda_dopo_string(villo+'*'+self.giocatore+'*')
           giocarr.extend(giocarrvillo)
           if (len(giocarr) > 0):
               if (len(giocarr[0])) > 0:
                   try:
                       gfloat = float(giocarr[0])
                       
                       return gfloat
                   except:
                       logging.exception( "ADD_COEFF non ho trovato, player : "+self.giocatore)
                       return 1
        return 1
        
        
    def calc_priorita(self):
        POP_COEFF =travian_account.pop_coeff
        ALL_COEFF = travian_account.all_coeff
        DONE_COEFF =travian_account.done_coeff
        DIST_COEFF = travian_account.dist_coeff
        priorita = self.done*DONE_COEFF
        
#        if (not (travian_mail.get_ask_string(self.giocatore) )):
        priorita += self.get_distanza() *DIST_COEFF+self.popolazione*POP_COEFF
#        if (not (travian_mail.get_ask_string(self.alleanza) )):
#            priorita += self.puntialleanza*ALL_COEFF
        if (self.is_gallo()):
            priorita = priorita * 1.5
        if (self.is_romano()):
            priorita = priorita * 1.25
        
        return priorita


    def verify_proprietario(self):
        try:
            carte = travian_carta.ricercafarm(self.xp,self.yp, 1)
            if (len(carte)) > 0 :
                villaggio = travian_anavill.get_villaggio(carte[0] )
                return (self.giocatore == villaggio.proprietario )
            else:
                return 0
        except:
            logging.exception( "VERIFY_PRORIETARIO FAILED for "+str(self.xp)+ ","+str(self.yp))
            return 0  
        
        
        
    def is_possible(self,units, coeff, mintr, maxdist, villo=""):
        if (travian_mail.get_ask_string(self.giocatore) or travian_mail.get_ask_string(villo+self.giocatore)):
            #logging.debug("TRYING "+self.giocatore)

            if (self.popolazione > travian_account.max_population):
            #    logging.debug("POPOLAZIONE "+str(self.popolazione))

                return 0
            tnecc = self.truppe_necessarie_arg(coeff, mintr, villo)
            if (tnecc > units):
             #   logging.debug("TRUPPE NECESSARIE "+str(tnecc ))

                return 0 
            distanza = self.get_distanza()
            if (distanza > maxdist):
            #    logging.debug("DISTANZA "+str(distanza ))

                return 0
            
            return 1
        else:
            return 0

    def is_gallo(self):
        return (string.upper(self.tribu) == string.upper(travian_language.galli))

    def is_romano(self):
        return (string.upper(self.tribu) == string.upper(travian_language.romani))
    def truppe_necessarie_arg(self, coeff, mintr, villo = ""): 
        
        tn = max(self.popolazione * raid.ATT_COEFF / coeff,mintr)
        
        if (self.is_gallo() == 1):
            tn = tn*1.5
        if (self.is_romano() == 1):
            tn = tn*1.25

        if (self.popolazione > 100):
            tn = tn * 1.1
        if (self.popolazione > 200):
            tn = tn * 1.1
        if (self.popolazione > 300):
            tn = tn * 1.1
        tn = tn*self.get_add_coeff(villo)
        return tn

    def start_raid(self):
        
        self.done = self.done+1
        

        
    def __repr__(self):
        return ("(giocatore= "+self.giocatore+", popolazione="+str(self.popolazione)+",id = "+str(self.id)+", xp="+str(self.xp)+",yp ="+str(self.yp)+",done = "+str(self.done)+",distanza="+str(self.get_distanza())+")")

    def __cmp__(self, other):
        return cmp(self.calc_priorita(), other.calc_priorita())


def setupraids(raidslines,xb,yb):
    global rl
    rl = raidlist(raidslines,xb,yb)
    return rl

def setraids(rlArg):
    global  rl
    rl = rlArg
    
def getraids():
    return rl 
    
def save_raids():
    logging.debug("SAVE_RAIDS")
    raids = getraids()
    output = open(travian_account.raids_file, 'wb')
    pickle.dump(raids , output)
    output.close()    
    logging.debug("SAVE_RAIDS FINISHED")
    
    
    
def available_raids():
    global rl
    return (rl != None)
    
def get_possible_fata(units):
    global rl
    return rl.get_possible_fata(units)
    
def get_possible_spada(units):
    global rl
    return rl.get_possible_spada(units)

def get_possible_arg(units, coeff, mintr, maxdist,villo= ""):
    global rl
    return rl.get_possible_arg(units, coeff, mintr, maxdist, villo)
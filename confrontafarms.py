#!/usr/bin/env python
import time,sys,os,random, string, traceback
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raidmap, travian_carta, travian_anavill
import travian_login,  travian_effettuaraids , travian_risorse , travian_villaggi , travian_mercato , travian_party , travian_accademia , travian_mail 
import travian_priorita, travian_sposta, travian_schiva
import travian_build, travian_effettuaraids, travian_villaggi 
import travian_setup, travian_party , travian_accademia, travian_mail , travian_troopactions
import travian_messaggi
import logging
import logging.handlers
import travian_party
import urllib, urllib2
import travian_anapla
from sgmllib import SGMLParser



current_villo=""
loopcounter  = 0
LOGFILE_NAME = '../public_html/travian/'+sys.argv[1]+'.log'
ROLLLOGFILE_NAME = '../public_html/travian/R'+sys.argv[1]+'.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',

                    filename=LOGFILE_NAME ,
                    filemode='w')

rhfdl= logging.handlers.RotatingFileHandler(filename=ROLLLOGFILE_NAME, maxBytes=1000000, backupCount=30);
rhfdl.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
rhfdl.setFormatter(formatter )
logging.getLogger('').addHandler(rhfdl)

class playerDati:
    def __init__(self,nome):
        self.nome= nome
        self.abitanti = 0
        self.alleanza= ""
        self.linkplayer = ""
    def __cmp__(self, that):         
        if isinstance(that, playerDati):                 
            return cmp(self.nome,that.nome) 
        
    def __hash__(self):
        return self.nome.__hash__()
    def __repr__(self):                       
        return self.nome+","+str( self.abitanti)+","+self.alleanza +","+self.linkplayer     
    
class travianLeggiFarms(SGMLParser):
    def reset(self):
        #funzione di init
        #Funzione Interna non utilizzare
        SGMLParser.reset(self)
        self.data = []
        self.inplayer = 0
        self.inalleanza = 0
        self.inpop = 0
        self.players = []
        self.linkplayer = ""
        self.plusfound = 0
    def start_td(self, attrs):
        a_tag = [v for k, v in attrs if k=='class']
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("pop") > -1):
                self.inpop = 1
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("uid") > -1):
                self.inplayer = 1
            if (current_tag.find("aid") > -1):
                self.inalleanza = 1
            if (current_tag.find("spieler.php?") > -1):
                if (len(self.players) > 0):
                    self.players[len(self.players)-1].linkplayer=current_tag
                
    def start_span(self, attrs):
        s_tag = [v for k, v in attrs if k=='class']
        if (len(s_tag) > 0):
            current_tag = s_tag[0]
            if (current_tag == "plus"):
                
                self.plusfound = 1
            else:
                self.plusfound = 0
        
    def handle_data(self,text):
        if (len(text.rstrip())) > 0:
            if ((self.inplayer == 1) and (self.plusfound == 0)):
                if (len(text.rstrip()) > 1):
                    myplayer = playerDati(nome = text.rstrip())
                    self.players.append(myplayer)
                
                self.inplayer = 0
            if ((self.inalleanza == 1) and (self.plusfound == 0)):
                if (len(self.players) > 0):
                    self.players[len(self.players)-1].alleanza=text.rstrip()
                    self.inalleanza = 0
                
            elif ((self.inpop == 1) and (self.plusfound == 0)):
                
                if (len(self.players) > 0):
                    try:
                        self.players[len(self.players)-1].abitanti=int(text.rstrip())
                    except:
                        self.players[len(self.players)-1].abitanti=minpop
    
                    self.inpop = 0

    def leggi_players(self):    
        return self.players
def leggi_config(accountfile):
    travian_account.getaccount(os.path.join("config",accountfile ))
   
    travian_schiva.setup_schivaggi(travian_account.schiva_file)
    travian_villaggi.setup_coords(travian_account.coords_file)
    getattr(travian_priorita, travian_account.methodo_setup)()
    travian_risorse.init_coef()


leggi_config(sys.argv[1])
argfile = sys.argv[1]
  
travian_login.effettua_login()
travian_mail.leggi_note()
raggio=int(sys.argv[2])
servername=sys.argv[3]
numvilli = int(sys.argv[4])
minpop = int(sys.argv[5])

maxpop = int(sys.argv[6])
urls = []
for i in range(0,numvilli):
    coord = travian_villaggi.get_curr_coords(i)
    coordx = int(coord[0])
    coordy = int(coord[1])
    url = 'http://travian.ws/analyser.pl?s='+servername+'&q='+coord[0].rstrip()+'%2C+'+coord[1].rstrip()+'%2C+'+str(raggio+1)
    urlpx10 = 'http://travian.ws/analyser.pl?s='+servername+'&q='+str(coordx+10)+'%2C+'+coord[1].rstrip()+'%2C+'+str(raggio+1)
    urlmx10 = 'http://travian.ws/analyser.pl?s='+servername+'&q='+str(coordx-10).rstrip()+'%2C+'+coord[1].rstrip()+'%2C+'+str(raggio+1)
    urlpy10 = 'http://travian.ws/analyser.pl?s='+servername+'&q='+coord[0].rstrip()+'%2C+'+str(coordy+10)+'%2C+'+str(raggio+1)
    urlmy10 = 'http://travian.ws/analyser.pl?s='+servername+'&q='+coord[0].rstrip()+'%2C+'+str(coordy-10)+'%2C+'+str(raggio+1)
    
    if (not (url in urls)):
        urls.append(url)
        urls.append(urlpx10)
        urls.append(urlmx10)
        urls.append(urlpy10)
        urls.append(urlmy10)
            
        
print urls     
#travian_login.effettua_login()
#travian_mail.leggi_note()

allplayers = []
all_asks = travian_mail.ritorna_solo_stringa('*')
print all_asks
for url in urls:
    tlf = travianLeggiFarms()
    tlf.reset()
    html_ca = travian_login.openurl(url )
    test_ca = html_ca.read()
   
    tlf.feed(test_ca)
    players_found = tlf.leggi_players()
    print "PLAYERS FOUND "
    print players_found
    for player in players_found:
        print "PLAYER"
        print player
    
        if ((not(travian_mail.get_ask_string(player.nome ))) and((not(travian_mail.get_ask_string("--"+player.nome ))))):
            #if ((player.abitanti <= maxpop) and (player.abitanti >= minpop)):
            giocatore = travian_anapla.get_giocatore(player.linkplayer)
            
            if (giocatore.popolazione != ""):
                if ((int(giocatore.popolazione) <= maxpop) and (int(giocatore.popolazione)>= minpop)):
                    ask_player = "*"+player.nome+"*"
                    if (not (ask_player in allplayers)):
                        
                        allplayers.append("*"+ask_player+"*")
                    
        
setplayers = set(allplayers)

for sp in setplayers:
    print sp
    
print "---------------------------------------"

all_asks.extend(setplayers)

#print "---------------------------------------EXTENDED-------------------------"

print all_asks
#print "---------------------------------------SORTED-------------------------"

all_asks.sort()

print all_asks    
print "-------------------LISTA SORTED-------------------------------------"
for all_ask in all_asks:
    print all_ask





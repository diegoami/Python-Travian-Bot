#!/usr/bin/env python
"""
TravianBot 0.1 pre Alhpa 1
#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""
#load lib
import sys,time, random, string
import urllib, urllib2, travian_login, socket_travian, time, sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici, travian_anaally
import travian_account,travian_login,socket_travian, travian_language, travian_anapla
from sgmllib import SGMLParser
import logging


ASPETTA_NIENTE=0
ASPETTA_NOMEVILLAGGIO=1
ASPETTA_COORDINATE=2
ASPETTA_POPOLO =3
ASPETTA_ALLEANZA=4
ASPETTA_PROPRIETARIO=5
ASPETTA_ABITANTI=6

class villaggioDati:
    def __init__(self,popolo, alleanza, proprietario, abitanti, nomevillaggio, coordinate,link_proprietario,link_alleanza):
        self.popolo = popolo.strip()
        self.alleanza = alleanza.strip()
        self.proprietario = proprietario.strip()
        self.abitanti = abitanti.strip()
        self.nomevillaggio = nomevillaggio.strip()
        self.coordinate = coordinate
        self.link_proprietario = link_proprietario.strip()
        self.link_alleanza = link_alleanza.strip()
        self.puntialleanza = "0"
        coords=self.coordinate.replace("(","")
        coords=coords.replace(")","")

        (self.xp,self.yp) = string.split(coords,"|")
        giocatore_dati = travian_anapla.get_giocatore(link_proprietario )
        self.add_giocatore_dati(giocatore_dati)
 #       self.popolazione = self.abitanti
 #       self.villaggi = "1" 
        
        #if (self.link_alleanza != ""):
            #alleanza_dati = travian_anaally.get_alleanza(self.link_alleanza )
            #self.puntialleanza = alleanza_dati.punti
        #else:
            #self.puntialleanza = "0"
        #if (self.puntialleanza.strip() == ""):
            #self.puntialleanza = "0"

    def add_giocatore_dati(self, giocatoreDati):

        self.villaggi = giocatoreDati.villaggi 
        self.popolazione = giocatoreDati.popolazione 
        
    def __repr__(self):
        return ("(popolo="+self.popolo+",alleanza="+self.alleanza+",proprietario="+self.proprietario+",abitanti="+self.abitanti+",nomevillaggio="+self.nomevillaggio+",coordinate="+self.coordinate+",xp="+self.xp+",yp="+self.yp+",link_proprietario="+self.link_proprietario+",popolazione="+self.popolazione+",villaggi="+self.villaggi+",puntialleanza="+self.puntialleanza+")")

class travianLeggiVillaggio(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.popolo=""
        self.alleanza=""
        self.proprietario=""
        self.abitanti=""
        self.nomevillaggio=""
        self.coordinate=""
        self.puntialleanza=""
        self.link_proprietario=""
        self.link_alleanza=""
        self.inspan = 0
        self.abitantivillaggio=0
        self.aspetta = ASPETTA_NIENTE
        self.intd = 0
        self.indiv = 0
        self.inh1=0
    def start_td(self,attrs):
        self.intd = 1
    def start_span(self,attrs):
        self.inspan = 1
    def start_h1(self,attrs):
        self.inh1=1
    def end_h1(self):    
        self.inh1=0
    def start_div(self,attrs):
        class_tag = [v for k, v in attrs if k=='id']
        if (self.inh1 == 1):
            self.indiv = 1
            
            if (self.aspetta == ASPETTA_NIENTE):
                self.aspetta = ASPETTA_NOMEVILLAGGIO
 #               elif (self.aspetta == ASPETTA_NOMEVILLAGGIO):
#                    self.aspetta = ASPETTA_COORDINATE
#                elif (self.aspetta == ASPETTA_COORDINATE):
#                    self.aspetta = ASPETTA_NIENTE
#                logging.debug("ASPETTA = "+self.aspetta)
                    
             
    def end_div(self):
        self.indiv = 0     
    def end_td(self):
        self.intd = 0
        
    def end_span(self):
        self.inspan = 0
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("spieler.php?uid") > -1):
                self.link_proprietario= current_tag  
            if (current_tag.find("allianz") > -1):
                self.link_alleanza= current_tag        
             
    def handle_data(self,text):
        
        if (string.upper(travian_language.popolo) == string.upper(text) ):


            self.aspetta = ASPETTA_POPOLO
        elif (string.upper(travian_language.alleanza) == string.upper(text) ):


            self.aspetta = ASPETTA_ALLEANZA

        elif (string.upper(travian_language.proprietario) == string.upper(text) ):


            self.aspetta = ASPETTA_PROPRIETARIO


        elif (string.upper(travian_language.abitanti) == string.upper(text) ):


            self.aspetta = ASPETTA_ABITANTI
            


        elif ((self.intd == 1) and (self.aspetta ==ASPETTA_POPOLO) and (len(text) >0)):


            self.popolo = text

        elif ((self.intd == 1) and (self.aspetta ==ASPETTA_ALLEANZA) and (len(text) >0)):
          

            self.alleanza = text


        elif ((self.intd == 1) and (self.aspetta ==ASPETTA_PROPRIETARIO) and (len(text) >0)):


            self.proprietario = text


        elif ((self.intd == 1) and (self.aspetta ==ASPETTA_ABITANTI) and (len(text) >0)):

            self.abitanti = text
            self.aspetta = ASPETTA_NIENTE

        elif ((self.indiv == 1) and (self.aspetta == ASPETTA_NOMEVILLAGGIO)):


            self.nomevillaggio = text
            self.aspetta = ASPETTA_COORDINATE
        elif (self.aspetta == ASPETTA_COORDINATE):


            self.coordinate = text
            self.aspetta = ASPETTA_NIENTE

                

    def get_villaggio(self):
        return villaggioDati(popolo=self.popolo,alleanza=self.alleanza, proprietario=self.proprietario, coordinate=self.coordinate, nomevillaggio =self.nomevillaggio, abitanti=self.abitanti, link_proprietario=self.link_proprietario,link_alleanza=self.link_alleanza)
     
    
def get_villaggio(url):

    time.sleep(0.2)
    cookie_data=[]
    tlv= travianLeggiVillaggio()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlv .feed(test_ca)
    villaggioread = tlv.get_villaggio()
    logging.debug(villaggioread)
    return villaggioread


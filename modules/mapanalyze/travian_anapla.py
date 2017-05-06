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
import urllib, urllib2, travian_login, socket_travian,  time, sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici
import travian_account,travian_login,socket_travian, travian_language
from sgmllib import SGMLParser
import logging, re


ASPETTA_NIENTE=0
ASPETTA_POPOLO =1
ASPETTA_ALLEANZA=2
ASPETTA_VILLAGGI=3
ASPETTA_POPOLAZIONE=4
ASPETTA_FINITO=5

class giocatoreDati:
    def __init__(self,popolo, alleanza, villaggi, popolazione):
        self.popolo = popolo
        self.alleanza = alleanza
        self.villaggi = villaggi
        self.popolazione = popolazione
       
    def __repr__(self):
        return ("(popolo="+self.popolo+",alleanza="+self.alleanza+",villaggi ="+self.villaggi+",popolazione="+self.popolazione+")")

class travianLeggiGiocatore(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.popolo=""
        self.alleanza=""
        self.villaggi=""
        self.popolazione=""
        self.intd = 0
        self.aspetta = ASPETTA_NIENTE
    def start_td(self,attrs):
        self.intd = 1
    def end_td(self):
        self.intd = 0
        
    def handle_data(self,text):
       
        if (self.aspetta != ASPETTA_FINITO):
            if (string.upper(travian_language.popolo) == string.upper(text) ):
                self.aspetta = ASPETTA_POPOLO
            elif (string.upper(travian_language.alleanza) == string.upper(text) ):
                self.aspetta = ASPETTA_ALLEANZA
            elif (string.upper(travian_language.villaggi) == string.upper(text) ):
                self.aspetta = ASPETTA_VILLAGGI
            elif (string.upper(travian_language.popolazione) == string.upper(text) ):
                self.aspetta = ASPETTA_POPOLAZIONE
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_POPOLO) and (len(text) >0)):
                self.popolo = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_ALLEANZA) and (len(text) >0)):
                self.alleanza = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_VILLAGGI) and (len(text) >0)):
                self.villaggi = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_POPOLAZIONE) and (len(text) >0)):
                self.popolazione = text
                self.aspetta = ASPETTA_FINITO
     

    def get_giocatore(self):
        return giocatoreDati(popolo=self.popolo,alleanza=self.alleanza, villaggi=self.villaggi, popolazione=self.popolazione)
     

class travianLeggiVilli(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.villi=[]
        self.capitale = ""
        self.nextcapitale = 0
        self.currentvillo = ""
    def start_a(self,attrs):
        p = re.compile('karte.php\?d=([0-9]+)\&c=([0-9a-zA-Z]+)')
        a_tag = [v for k, v in attrs if k=='href']
            
        if "karte.php?" in a_tag[0]:
            print a_tag[0]
            self.invillaggio = 1
            m = p.match(a_tag[0])
            if (m != None):
                villo = m.group(1)     
                self.villi.append(villo)
                self.currentvillo = villo
#                if (self.nextcapitale == 1):
#                    self.capitale = villo
#                    self.nextcapitale = 0
            
    def handle_data(self,text):
        if ("(Capitale)" in text):
            self.capitale = self.currentvillo
    
    def get_villi(self):
        return self.villi
    def get_capitale(self):
        return self.capitale

def get_capitale(url):
    cookie_data=[]
   
    tlv= travianLeggiVilli()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlv.feed(test_ca)

    return tlv.get_capitale()   

def get_villi(url):
    cookie_data=[]
   
    tlv= travianLeggiVilli()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlv.feed(test_ca)

    return tlv.get_villi()   
    
def get_giocatore(url):
    cookie_data=[]
   
    tlg= travianLeggiGiocatore()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlg.feed(test_ca)

    return tlg.get_giocatore()
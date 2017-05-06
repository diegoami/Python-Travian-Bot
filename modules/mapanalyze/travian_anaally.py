#!/usr/bin/env python
"""
TravianBot 0.1 pre Alhpa 1
#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""
#load lib
import sys,time, random, string,re
import urllib, urllib2,  socket_travian,  time, sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici

import travian_account,travian_login,socket_travian, travian_language
from sgmllib import SGMLParser
import logging


ASPETTA_NIENTE=0
ASPETTA_TAG=1
ASPETTA_RANK =2
ASPETTA_PUNTI=3
ASPETTA_MEMBRI=4
ASPETTA_FINITO=5


class alleanzaDati:
    def __init__(self,tag, rank, punti, membri):
        self.tag= tag
        self.rank = rank
        self.punti= punti
        self.membri = membri
       
    def __repr__(self):
        return ("(tag="+self.tag+",rank="+self.rank+",punti="+self.punti+",membri="+self.membri+")")

class travianLeggiAlleanza(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.tag=""
        self.rank=""
        self.punti=""
        self.membri=""
        self.intd = 0
        self.aspetta = ASPETTA_NIENTE
    def start_td(self,attrs):
        self.intd = 1
    def end_td(self):
        self.intd = 0
        
    def handle_data(self,text):
        
        if (self.aspetta != ASPETTA_FINITO):
            if (string.upper(travian_language.tag) == string.upper(text) ):
                self.aspetta = ASPETTA_TAG
            elif (string.upper(travian_language.rank) == string.upper(text) ):
                self.aspetta = ASPETTA_RANK
            elif (string.upper(travian_language.punti) == string.upper(text) ):
                self.aspetta = ASPETTA_PUNTI
            elif (string.upper(travian_language.membri) == string.upper(text) ):
                self.aspetta = ASPETTA_MEMBRI
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_TAG) and (len(text) >0)):
                self.tag = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_RANK) and (len(text) >0)):
                self.rank = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_PUNTI) and (len(text) >0)):
                self.punti = text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_MEMBRI) and (len(text) >0)):
                self.membri= text
                self.aspetta = ASPETTA_FINITO
     

    def get_alleanza(self):
        return alleanzaDati(tag=self.tag,punti=self.punti, rank=self.rank, membri=self.membri)


class travianLeggiMembri(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.players=[]

    def start_a(self,attrs):
        p = re.compile('spieler.php\?uid=([0-9]+)')
        a_tag = [v for k, v in attrs if k=='href']
            
        if "spieler.php?" in a_tag[0]:
            
            logging.debug( a_tag[0])
            self.inplayer = 1
            m = p.match(a_tag[0])
            if (m != None):
                player = m.group(1)     
                self.players.append(player)
            
    
    def get_players(self):
        return self.players
    
def get_players(url):
    cookie_data=[]   
    tlm = travianLeggiMembri()
    html_ca = travian_login.openurl(url) 
    test_ca = html_ca.read()  
    tlm.feed(test_ca)
    return tlm.get_players()       
     
    
def get_alleanza(url):
    cookie_data=[]
    tla= travianLeggiAlleanza()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tla.feed(test_ca)
    return tla.get_alleanza()


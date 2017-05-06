#!/usr/bin/env python
"""
TravianBot 0.1 pre Alhpa 1
#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""

import sys,time, random
import urllib, urllib2, travian_account,travian_login,travian_info,socket_travian
import travian_login
from sgmllib import SGMLParser
import logging


class travianSpedisci(SGMLParser):
    def reset(self):
        #funzione di init
        #Funzione Interna non utilizzare
        SGMLParser.reset(self)
        self.data = []
        self.titolo = ""
        self.aggiungi = 0
        self.testo =""
        self.dest = ""
        self.intextarea= 0
    def start_form(self,attrs):
        nome = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        
        if ("msg" in nome):
            logging.info("MSG TROVATO")
            self.aggiungi = 1
            
    def start_textarea(self, attrs):    
        nome = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
       
        cookie_format=[]
        cookie_format.append(nome[0])
        if (len(valore) >0):
            cookie_format.append(valore[0])
        else:
            cookie_format.append(self.titolo)
        
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)

    def start_input(self, attrs):
        nome = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        
        cookie_format=[]
        if (self.aggiungi == 1):
            if (len(nome) >0 ):
                cookie_format.append(nome[0])

                
                if "be" in nome:

                    valore[0]=self.titolo
                if "an" in nome:

        
                    valore[0]=self.dest
                if (len(valore) > 0):
                    cookie_format.append(valore[0])
                else:
                    cookie_format.append("")
                temp_tuple=tuple(cookie_format)
                self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)
      
def spedisci(subject, receiver):  
    cookie_data=[]
    parser=travianSpedisci()
    parser.dest = receiver
    parser.titolo = subject
    html_login = travian_login.openurl(travian_account.mail_page)
    testo_login=html_login.read()
    parser.feed(testo_login)
    parser.get_cookie(cookie_data)
    logging.debug(cookie_data)
    cookie_data = urllib.urlencode(cookie_data)
    logging.debug(travian_account.spedisci_page)
    socket_travian.travian_cookie(cookie_data, travian_account.spedisci_page)
    result = travian_login.openurl(travian_account.spedisci_page).read()
    if (result.find("spam") == -1):
        return 1
    else:
        return 0
        
    if (result.find("spam") > -1):
        return 0
    else:
        return 1
        
    
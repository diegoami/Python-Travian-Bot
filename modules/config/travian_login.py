#!/usr/bin/env python
"""
TravianBot 0.1 pre Alhpa 1
#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""

import sys,time, random
import urllib, urllib2, travian_account,travian_login,socket_travian, traceback
import travian_language
from sgmllib import SGMLParser
import logging


class travianLogin(SGMLParser):
    def reset(self):
        #funzione di init
        #Funzione Interna non utilizzare
        SGMLParser.reset(self)
        self.data = []
    def start_input(self, attrs):
        nome = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        cookie_format=[]
        cookie_format.append(nome[0])
        if "text" in tipo:
            valore[0]=travian_account.login_name
        if "password" in tipo:
            valore[0]=travian_account.login_password
            
            
        cookie_format.append(valore[0])
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)
      
def loginpw(server, account, password):  
    #print server , account, password
    travian_account.login_name = account
    travian_account.login_password =  password
    travian_account.login_page = "http://"+server+"/"
    travian_account.home_page = "http://"+server+"/dorf1.php"
    
    try:
        handle = login()
    except:
        logging.exception( "Could not login, retrying ....")
        time.sleep(5)  

   
    return handle


def effettua_login():
    loggedin = 0
    while (loggedin == 0):
        try:
        
            login()
            loggedin = 1
        except:


            logging.exception("Could not login, retrying ....")
            time.sleep(5)  

def login():
    cookie_data=[]

    parser=travianLogin()
    
    html_login = openurl(travian_account.login_page)
    
    testo_login=html_login.read()
    parser.feed(testo_login)
    parser.get_cookie(cookie_data)

    cookie_data = urllib.urlencode(cookie_data)
    socket_travian.travian_cookie(cookie_data, travian_account.home_page)
    result = openurl(travian_account.home_page).read()
   
    if (result != None):
        if (result.find(travian_language.calcolo) > -1):
            return 1
        else:
            logging.info( "Could not login")
            return 0
    else:
        logging.info( "Could not login")
        return 0
            
            
def openurl(urlarg, values = {}):

    if (urlarg.find('http') > -1):
        url = urlarg
    else:
        url= travian_account.start_page+urlarg
    done = False
    while (not done):
        try:
            values = {}
            headers = { 'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
        
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data, headers)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request )
            done = True
            return response
        except:
            logging.exception(  " Could not connect to "+ url+ ", retrying")
            
            if (urlarg != travian_account.login_page):
                login()
            

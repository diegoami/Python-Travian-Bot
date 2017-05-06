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
import urllib, urllib2, travian_login, socket_travian,  time,  sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici
#load modules
import travian_account,travian_login,socket_travian 
import logging


from sgmllib import SGMLParser

class travian_urlfinder(SGMLParser):
    def reset(self):
        #funzione di init
        #Funzione Interna non utilizzare
        SGMLParser.reset(self)
       
        self.url=""
   
    def start_a(self,attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if "dorf1.php?" in a_tag[0]:
            self.url=a_tag[0]
            
        if "dorf2.php?" in a_tag[0]:
            
            self.url=a_tag[0]

def build_edificio(edificio_name):

    spazi_edificabili = travian_resdorf.get_spazi_edificabili()
    if (len(spazi_edificabili)) > 0 :
        primo_spazio_edificabile = spazi_edificabili[0] 
        linkEdifici = travian_edifici.get_link_edifici(primo_spazio_edificabile.href)
    
        linkBuildEdificio = filter (lambda linkEdificio : string.upper(linkEdificio.title) == string.upper(edificio_name), linkEdifici )    
        if (len(linkBuildEdificio)>0):
            buildRef = linkBuildEdificio[0].href
            travian_login.openurl(buildRef)
            logging.debug( "Success for build page " +str(buildRef))

        else:
            pass
    else:
        logging.debug( "Non esistono spazi edificabili !!!!!")

def upgrade_edificio(edificio_name):    

    edificiLinks = travian_resdorf.get_edifici()
    
    linkEdifici = travian_resdorf.get_link_edificio_from(edificio_name, edificiLinks)
    if (len(linkEdifici)>0):
        linkEdificio = linkEdifici[0]
        buildhref = linkEdificio.href 
        logging.debug("Trying ... %s" + str( buildhref))
        build(buildhref)
        logging.debug("Success!")
       
    else:
        pass
    


def build(build_relurl):
    
    parser_info=travian_urlfinder()
    build_page=build_relurl


    production_page_html=travian_login.openurl(travian_account.home_page)
  

    start_page_html=travian_login.openurl(build_page)
    start_page_testo=start_page_html.read()
    
    parser_info.reset()
    parser_info.feed(start_page_testo)

    if (parser_info.url != ""):
        logging.debug("Parser_info.url = " + parser_info.url) 
        travian_login.openurl(parser_info.url)
        logging.debug("Success ! " + str( build_page))
        return 1
    else:
        logging.debug("Failure !" + str( build_page))
        return 0
        
       

    
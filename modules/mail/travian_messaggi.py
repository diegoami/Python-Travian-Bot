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
import urllib, urllib2, travian_login, socket_travian, travian_info, time, sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici, travian_anaally
import travian_account,travian_login,travian_info,socket_travian, travian_language, travian_anapla
from sgmllib import SGMLParser
import logging


class travianListaMessaggi(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.messaggi=[]
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']

        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("nachrichten.php?id") > -1):
                self.messaggi.append(current_tag )
             
    def get_messaggi(self):    
        return self.messaggi

def get_messaggi(url):

    time.sleep(1)
    cookie_data=[]
    tlv= travianListaMessaggi()
    html_lm = travian_login.openurl(url)
 
    test_lm = html_lm.read()
    tlv.feed(test_lm)
    return tlv.get_messaggi()

def leggi_messaggi(url):
    tutti_messaggi = get_messaggi(url)
    for messaggio in tutti_messaggi:
        time.sleep(0.2)
        
        travian_login.openurl(messaggio)
    


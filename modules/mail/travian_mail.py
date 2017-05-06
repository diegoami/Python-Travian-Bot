from sgmllib import SGMLParser
import urllib2, time, travian_account,  travian_login
import travian_language, string, travian_resdorf
import traceback
import logging

import string


note_text = ""
note_interne = ""
lista_note = []
lista_attacchi =[]
class travian_tieninote(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        self.intextarea = 0
        self.note = ''
    def start_textarea(self, attrs):
        self.intextarea = 1
        logging.info( "IN TEXT AREA")
    def handle_data(self,text):
        
        if (self.intextarea == 1):
            
            self.note = self.note + text
            
    def end_textarea(self):        
        self.intextarea = 0
            
    def dammi_note(self):
        return self.note

def ritorna_solo_stringa(astr):
    global note_text
    global lista_note
    return filter ( lambda x : x.find(astr) > -1, lista_note )




def ha_solo_stringa(astr):

    global note_text
    global lista_note
    fil = filter ( lambda x : x.find(astr) > -1, lista_note )
    if (len(fil) > 0):
        return 1
    else:
        return 0
    
def retrieve_string(astr):
    global note_text
    global lista_note

    fil = filter ( lambda x : x.startswith(astr), lista_note )

    if (len(fil) > 0):
        return fil[0]
    else:
        return None
    
def comincia_solo_stringa(astr):
    global note_text
    global lista_note

    fil = filter ( lambda x : x.startswith(astr), lista_note )

    if (len(fil) > 0):
        return 1
    else:
        return 0
    

def guarda_dopo_string(astr):
    global note_text
    global lista_note
    splicelist = []
    fils = filter ( lambda x : x.startswith(astr), lista_note )
    for fil in fils:
        splicedstr = fil[len(astr):len(fil)]
        splicelist.append(splicedstr)
        
    return splicelist



def leggi_note():
    try:
        global note_text
        global note_interne
        global lista_note        
        cookie_data=[]
        
        html_ca = travian_login.openurl(travian_account.mail_page)
        note_text = html_ca.read()
        
        ttn = travian_tieninote()
        ttn.feed(note_text)
        note_interne = ttn.dammi_note()

        lista_note = string.split( note_interne,'\r\n')
    except:
        logging.exception( "LEGGI NOTE FAILED")

        
       
def get_only_string(stringarg):
    return get_string(stringarg) and not get_ask_string(stringarg)
       
def get_ask_string(stringarg):
    global note_text

    if (note_text.find("*"+stringarg+"*") > -1):
        return 1
    else:
        return 0


def get_string(string_arg):
    
    global note_text
    global lista_note
    return comincia_solo_stringa(string_arg)

def get_roberto():
    return get_string("ROBERT") or get_string("XX")

def get_build():
    return get_string("BUILD")

def get_mercanti():
    return get_string("MERCANTI")

def get_festa():
    return get_string("FESTA")

def get_ricerca():
    return get_string("RICERCA")

def get_build():
    return get_string("BUILD")
    
def get_schiva():
    return get_string("SCHIVA")
    
def get_rinforza():
    return get_string("RINFORZI")

def get_raid():
    return get_string("RAID")

def get_attacco():
    return get_string("ATTACCO")

def get_fake():
    return get_string("FAKE")


import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_url, travian_language, travian_caserma
import logging


from sgmllib import SGMLParser



class travian_ricerca(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        self.foundricerca = []
        self.inricerca = 0
    def __init__(self,ricerca):
        self.whatricerca = ricerca
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if (self.inricerca == 1):
            if (len(a_tag) > 0):
                current_tag = a_tag[0]
                if (current_tag.find("build.php") > -1):
                    self.foundricerca.append(current_tag)
                
    def get_found_ricerca(self):
        if (len(self.foundricerca) >0):
            return self.foundricerca[0]
        else: 
            return ""
        
    def handle_data(self,text):
        if (text == self.whatricerca):
            logging.debug("FOUND RICERCA " + self.whatricerca)
            self.inricerca = 1
        if (text.find(travian_language.sufficienti) > -1 ):
            self.inricerca = 0
        
def fai_ricerca_accademia(ricArg):
    fai_gen_ricerca(ricArg,travian_account.accademia_page)

def fai_ricerca_fabbro(ricArg):
    fai_gen_ricerca(ricArg,travian_account.fabbro_page)

def fai_ricerca_armeria(ricArg):
    fai_gen_ricerca(ricArg,travian_account.armeria_page)

def fai_gen_ricerca(ricArg, pagRicerca):
    
    travianRic = travian_ricerca(ricArg)
   
    
    ricerca_page_html=travian_login.openurl(pagRicerca)
   
    ricerca_page_testo = ricerca_page_html.read()
    travianRic.reset()
    travianRic.feed(ricerca_page_testo)
    ricercaLink = travianRic.get_found_ricerca()
    ricercahref = ricercaLink
    travian_login.openurl(ricercahref)  
                
             
    
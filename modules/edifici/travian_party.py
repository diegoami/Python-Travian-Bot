import traceback
import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_login, travian_language, travian_caserma, travian_risorse
import travian_mail

from sgmllib import SGMLParser
import logging



class travian_municipio(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        self.foundcorso = 0
        self.foundparty = []
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("build.php") > -1):
                self.foundparty.append(current_tag)
    def handle_data(self,text):           
        if (text.find("in corso") > -1):
            self.foundcorso = 1
    
    def get_big_party(self):
        if (len(self.foundparty) >1):
            return self.foundparty[1]
        else: 
            return ""
    def get_found_party(self):
        if (len(self.foundparty) >0):
            return self.foundparty[0]
        else: 
            return ""
    def is_in_corso(self):
        return self.foundcorso
def festa_in_corso():
    travianMun = travian_municipio()
    
    municipio_page_html=travian_login.openurl(travian_account.municipio_page)
    
    municipio_page_testo = municipio_page_html.read()
    
    if (municipio_page_testo.find('party') > -1):
        
        travianMun.reset()
        travianMun.feed(municipio_page_testo)
        incorso = travianMun.is_in_corso()
        logging.debug("FESTA IN CORSO"+str(incorso))
        
        return travianMun.is_in_corso()
    else:
        return 1
    
def fai_feste_possibili(villo):
    if ((travian_mail.get_string("FESTA") == 1) or (travian_mail.get_string(villo+"FESTA") == 1) ):
        fai_festa()
    if ((travian_mail.get_string("PFESTA") == 1) or (travian_mail.get_string(villo+"PFESTA") == 1) ):
        fai_festa(forzapiccola = 1)

    


def fai_festa(forzapiccola=0):
    time.sleep(0.25)
    
    try:
        travianMun = travian_municipio()
        
        municipio_page_html=travian_login.openurl(travian_account.municipio_page)
        
        municipio_page_testo = municipio_page_html.read()
        travianMun.reset()
        travianMun.feed(municipio_page_testo)
        if (travian_risorse.grande_festa_possibile() and (forzapiccola == 0)):
            logging.debug("TENTO  BIG PARTY ")
    
            partyLink = travianMun.get_big_party()
        else:
            logging.debug("TENTO  PICCOLO PARTY ")
    
            partyLink = travianMun.get_found_party()
            
        if (partyLink != ""):
            logging.debug("PARTYLINK = "+partyLink)
            partyhref = partyLink
            travian_login.openurl(partyhref)  
            return 1
        else:
            
            return 0
    except:
        logging.exception("FAI FESTA FAILED")
      
                
             
    
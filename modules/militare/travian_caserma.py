from sgmllib import SGMLParser
import urllib2, time, travian_account,travian_login
import travian_language, travian_func, string
import logging, urllib
import traceback
import socket_travian
import re
class travian_confermacongeda(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
    def start_input(self, attrs):
        name = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        
        cookie_format=[]
        cookie_format.append(name[0])
        cookie_format.append(valore[0])
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)

    def get_cookie(self,cookie):
        cookie.extend(self.data)

class travian_truppe(SGMLParser):
    
    def reset(self):
        SGMLParser.reset(self)
        self.truppe= [0,0,0,0,0,0,0,0,0,0,0,0]
        self.availabletruppe = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.intruppe  = 0
        self.inarrivo = 0
        self.inrinforzi = 0
        self.addtruppe  = 0
        self.addarrivo = 0
        self.truppeindex = 0
        self.notavailable = 0
        self.attacchi = []
        self.intimerspan = 0
        self.eattacco = 0
        self.found_congeda= []
        self.ritorna = [] 
        self.in_congeda = 0
        self.inritorna = 0
            
        self.caserma_tag = ""
        self.attacchifuori = []
        self.inkarte = 0
        self.karteact = ""
   
    def start_a(self, attrs):
        a_tag = [v for k, v in attrs if k=='href']
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("a2b.php?d=") > -1):
                
                self.in_congeda = 1
                self.caserma_tag = current_tag
                
            if (current_tag.find("karte.php?d=") > -1):
                p = re.compile('karte.php\?d=([0-9]+)&c=([0-9a-zA-Z]+)')
                
                m = p.match(current_tag)
                if (m != None):
                    self.karteact= m.group(1)
                    self.inkarte = 1
                    
        
        
    def start_span(self,attrs):
        ids = [v for k, v in attrs if k=='id']
        if (len(ids) >0 ):
            id = ids[0]
            if ((self.inarrivo == 1) and (id.find("timer") > -1)):
                self.addarrivo = 0
                self.inarrivo = 0
                self.intimerspan = 1
            
    def start_td(self, attrs):
        if (self.intruppe ==1):
            self.addtruppe = 1
                   
        else:
            self.addtruppe = 0
            
        if (self.inarrivo ==1):
            self.addarrivo = 1
                   
        else:
            self.addarrivo = 0    
    def handle_data(self,text):
        if (string.upper(travian_language.proprie_truppe) == string.upper(text) ):
     
            self.notavailable = 1
            
        if (string.upper("congeda") == string.upper(text) ):
     
            self.found_congeda.append(self.caserma_tag)
        if (string.upper(travian_language.truppe) == string.upper(text) ):
            self.intruppe = 1
        if (string.upper(travian_language.arrivo) == string.upper(text) ):
            self.inarrivo = 1    
        if ("Rinforzi" in text):
           
            self.inrinforzi = 1    
        if ("Ritorna" in text):
           
            self.inritorna = 1    
        
            
        if (self.addtruppe == 1):
            if (text.find("?") > -1):
                if (self.inrinforzi == 0):
                    self.eattacco = 1
                
            if (text.isdigit()):
                try:
                    self.truppe[self.truppeindex]=self.truppe[self.truppeindex]+int(text)
                    if (self.notavailable == 1):
                        self.availabletruppe[self.truppeindex]=self.availabletruppe[self.truppeindex]+int(text)
                    self.eattacco = 0       
    
                except:
                    logging.exception( text +  " could not be parsed ")

                
            self.truppeindex = self.truppeindex+1
            if (self.truppeindex >= len(self.truppe)):
                self.truppeindex = 0
                self.intruppe = 0
                self.addtruppe= 0
                self.notavailable = 0
                
        if (self.intimerspan == 1):
           
            self.intimerspan = 0
            if (self.eattacco == 1):
                self.attacchi.append(text)   
            if (self.inritorna == 1): 
                self.ritorna.append(text)   
                self.inritorna = 0

        if (self.inkarte == 1):
            self.inkarte = 0
            if (("Attacco" in text) or ("Raid" in text)):
                self.attacchifuori.append(self.karteact)
            
                
    def end_tr(self):    
        self.addtruppe= 0
    def end_table(self):    
        self.inrinforzi = 0

    def get_truppe(self):
        return self.truppe
    
    def link_congeda(self):
        return self.found_congeda
     
    def get_available_truppe(self):
        return self.availabletruppe
    def get_attacchi(self):
        return self.attacchi
    def get_ritorna(self):
        return self.ritorna

    def get_attacchifuori(self):
        return self.attacchifuori
    
    
def get_tca():    
    cookie_data=[]
    tca = travian_truppe()
    html_ca = travian_login.openurl("build.php?id=39&k")
    test_ca = html_ca.read()
    tca.feed(test_ca)
    return tca
    
def get_available_truppe():
    return get_tca().get_available_truppe()

def get_primo_attacco():
    attacchi = get_attacchi()
    logging.debug("ATTACCHI "+str(attacchi))
    if (len(attacchi) > 0):
        attacco = attacchi[0]
        
        atts = attacco.split(":")
        temp = int(atts[0])*3600+int(atts[1])*60+int(atts[2])
        return temp
         
    else:
        return 0
def get_attacchi():
    return get_tca().get_attacchi()

def get_ritorna():

    return get_tca().get_ritorna()

def get_ultimo_ritorno():
    turito = get_ritorna()
    if (len(turito) > 0):
        ultro = turito[len(turito)-1]
        rp = string.split(ultro,":")
        value = (float(rp[0])*3600+float(rp[1])*60+float(rp[2])) / 3600
        return value
    else:
        return 0
    

def get_attacchifuori():
    cookie_data=[]
    tca = travian_truppe()
    html_ca = travian_login.openurl(travian_account.rally_page)
    test_ca = html_ca.read()
    tca .feed(test_ca)
    return tca.get_attacchifuori()

def ha_tutte_le_truppe():
    return get_available_truppe() == get_truppe()
    

def get_tutte_truppe():
    cookie_data=[]
    tca = travian_truppe()
    html_ca = travian_login.openurl("build.php?id=39&k")
 
    test_ca = html_ca.read()
   
    tca .feed(test_ca)
   
    
    return tca.get_truppe()

def get_truppe():
    cookie_data=[]
    tca = travian_truppe()
    html_ca = travian_login.openurl(travian_account.rally_page)
 
    test_ca = html_ca.read()
   
    tca .feed(test_ca)
   
    
    return tca.get_truppe()



def congeda_tutto():
    cookie_data=[]
    tca = travian_truppe()
    html_ca = travian_login.openurl("build.php?id=39&k&j")
    test_ca = html_ca.read()
    tca.feed(test_ca)
    cong_links = tca.link_congeda()
    logging.debug(str(cong_links))
    for cong_link in cong_links:
        new_cookie_data=[]
        html_cc = travian_login.openurl(cong_link)
        gottenresult = html_cc.read()
        tct = travian_confermacongeda()
        tct.feed(gottenresult)
        tct.get_cookie(new_cookie_data)
    
    
        new_cookie_data = urllib.urlencode(new_cookie_data)
        logging.debug(str(new_cookie_data))
        result = socket_travian.travian_cookie(new_cookie_data, "build.php" )
        logging.debug(str(result))
        logging.debug("CONGEDA- SECOND STEP OVER")
    
        
        
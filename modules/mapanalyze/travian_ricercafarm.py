
import sys,time, random, urllib, urllib2
import travian_account,travian_login,travian_info,socket_travian, travian_carta


import travian_anavill, travian_raidmap, travian_account, travian_villaggi, travian_mail
import traceback
import logging


from sgmllib import SGMLParser
class travianRicercaFarm(SGMLParser):
    
    def __init__(self,xp, yp):
        
        self.xp = xp
        self.yp = yp
    def reset(self):
      
        SGMLParser.reset(self)
        self.data = []
        
        
  
    def start_input(self, attrs):
        nome = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        cookie_format=[]
        
        if (len(nome) > 0):
            cookie_format.append(nome[0])
            if "x" in nome:
                valore[0]=self.xp
            if "y" in nome:
                valore[0]=self.yp
            if "duree" in nome:
                valore[0]=120
            if "unit" in nome:
                valore[0]=26
            if "pop_max" in nome:
                valore[0]=110
         
          
            cookie_format.append(valore[0])
            temp_tuple=tuple(cookie_format)
            self.data.append(temp_tuple)
            
        
    def get_cookie(self,cookie):
        cookie_format =[]
        cookie_format.append("unit")
        cookie_format.append("24")
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
        cookie.extend(self.data)
        
    
    
def ricercafarm(x,y):
    cookie_data=[]
    trf = travianRicercaFarm(x,y)
    trf.reset()
    html_ca = travian_login.openurl(travian_account.ricercafarm_page)
 
    test_ca = html_ca.read()
   
    trf.feed(test_ca)
    trf.get_cookie(cookie_data)

    cookie_data = urllib.urlencode(cookie_data)
    result = socket_travian.travian_cookie(cookie_data, travian_account.ricercafarm_page, "rd" )
    if (result != None):
        gottenresult = result.read()
    else:
        return None

def do_setup_farm(raggio_raid):
    logging.debug( "Setting farms up...")
    travian_login.login()
    
    allvillaggilinks = travian_carta.get_villaggi_for_list(travian_villaggi.coords_list,raggio_raid)
    raidlines = []
    for villaggiolink in allvillaggilinks:
        try:
            logging.debug( " PARSING "+str(villaggiolink) )
            
            villaggio =  travian_anavill.get_villaggio(villaggiolink )
            logging.debug(villaggio)
            raidlines.append(villaggio)
        except:
            travian_login.login()
            logging.exception( villaggiolink +str(" could not be parsed "))

    logging.debug(raidlines)
    raids = travian_raidmap.setupraids(raidlines,int(travian_account.xp_start),int(travian_account.yp_start))  
    logging.debug(raids)

    
   
    return  raids


    
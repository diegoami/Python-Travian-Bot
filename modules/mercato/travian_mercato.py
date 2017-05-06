import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_login, travian_language, travian_risorse
import logging

from sgmllib import SGMLParser

r1 = 0
r2 = 0
r3 = 0
r4 = 0
dname = ""
x=""
y=""

class travian_confermamercato(SGMLParser):
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



class travian_spedisci(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        
    def start_input(self, attrs):
        name = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        cookie_format=[]
        cookie_format.append(name[0])
        if "r1" in name:
            valore[0]=str(r1)
        if "r2" in name:
            valore[0]=str(r2)
        if "r3" in name:
            valore[0]=str(r3)
        if "r4" in name:
            valore[0]=str(r4)
        if "dname" in name:
            valore[0]=str(dname)
        if "x" in name:
            valore[0]=str(x)
        if "y" in name:
            valore[0]=str(y)
            
            
     
        cookie_format.append(valore[0])
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)
        
def spediscimerce(r1Arg=0,r2Arg=0,r3Arg=0,r4Arg=0,dnameArg="", maxrisorse=60000, xArg="", yArg=""):
    global r1
    global r2
    global r3
    global r4
    global dname
    global x
    global y
    logging.debug( "Spedisci "+str(r1Arg)+","+str(r2Arg)+","+str(r3Arg)+","+str(r4Arg)+","+str(dnameArg)+","+str(xArg)+","+str(yArg))
        
    r1=travian_risorse.normalizza_quantita(r1Arg)
    r2=travian_risorse.normalizza_quantita(r2Arg)
    r3=travian_risorse.normalizza_quantita(r3Arg)
    r4=travian_risorse.normalizza_quantita(r4Arg)

    while ((r1+r2+r3+r4) > maxrisorse):
        r1 = max(r1 - 250,0)
        r2 = max(r2 - 250,0)
        r3 = max(r3 - 250,0)
        r4 = max(r4 - 250,0)

    dname=dnameArg
    x = xArg
    y = yArg
    logging.debug( "Spedisci Normalizzato "+str(r1)+","+str(r2)+","+str(r3)+","+str(r4)+","+str(dname)+","+str(xArg)+","+str(yArg))
    
    cookie_data=[]
    tca = travian_spedisci()
    tct = travian_confermamercato()
    html_ca = travian_login.openurl(travian_account.mercato_page)
 
    test_ca = html_ca.read()
   
    tca.feed(test_ca)
    tca.get_cookie(cookie_data)

    cookie_data = urllib.urlencode(cookie_data)
    result = socket_travian.travian_cookie(cookie_data, travian_account.mercato_page)
    if (result != None):
        gottenresult = result.read()
        cookie_data=[]
        tct.feed(gottenresult)
        
        tct.get_cookie(cookie_data)
        cookie_data = urllib.urlencode(cookie_data)
       
        result = socket_travian.travian_cookie(cookie_data, travian_account.mercato_page)

    else:
        logging.info(  "result war None")
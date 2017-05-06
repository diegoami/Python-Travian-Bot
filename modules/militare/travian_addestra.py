import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import  travian_language, travian_caserma, travian_mail
import random, time
import logging
import socket_travian

from sgmllib import SGMLParser

t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
t11 = 0
xx = 0
yy = 0
c = 0
kata = 0
dname = ""

class travian_confermatruppe(SGMLParser):
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


class travian_buildtruppe(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        
    def start_input(self, attrs):
        name = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        cookie_format=[]
        cookie_format.append(name[0])
        if "t1" in name:
            valore[0]=str(t1)
        if "t2" in name:
            valore[0]=str(t2)
        if "t3" in name:
            valore[0]=str(t3)
        if "t4" in name:
            valore[0]=str(t4)
        if "t5" in name:
            valore[0]=str(t5)
        if "t6" in name:
            valore[0]=str(t6)
        if "t7" in name:
            valore[0]=str(t7)
        if "t8" in name:
            valore[0]=str(t8)
        if "t9" in name:
            valore[0]=str(t9)
        if "t10" in name:
            valore[0]=str(t10)
        if "t11" in name:
            valore[0]=str(t11)
            
        if "x" in name:
            if (xx != 0):
                valore[0]=str(xx)
        if "y" in name:
            if (yy != 0):
                valore[0]=str(yy)
        if "c" in name:
            valore[0]=str(c)
        
        if "dname" in name:
            valore[0]=str(dname)
     
        cookie_format.append(valore[0])
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)
        
def sumList(L):
    return reduce(lambda x,y:x+y, L)
  
def get_slist():
    
    avail = travian_caserma.get_available_truppe()
   
    slist = sumList(avail[0:-1]) 

    return slist
        
def spedisci_tutto(xArg=0,yArg=0,cArg=4,dnameArg=""):
    slist = get_slist()
    avail = travian_caserma.get_available_truppe()
    if (travian_mail.get_string("EROE") ):
        logging.debug( "EROE RESTA!") 
        avail[10] = 0
    if (slist > 2):
        spediscitruppe(avail[0],avail[1],avail[2], avail[3], avail[4],avail[5],avail[6],avail[7],avail[8],avail[9],avail[10],xArg, yArg, cArg, dnameArg)

def spedisci_tutto_defteut(xArg=0,yArg=0,cArg=4,dnameArg=""):
    slist = get_slist()
    avail = travian_caserma.get_available_truppe()
    if (slist > 2):
        spediscitruppe(0,avail[1],0, avail[3], avail[4],0,0,0,0,0,0,xArg, yArg, cArg, dnameArg)


def spediscitruppe(t1Arg=0,t2Arg=0,t3Arg=0,t4Arg=0,t5Arg=0,t6Arg=0,t7Arg=0,t8Arg=0,t9Arg=0,t10Arg=0,t11Arg=0,xArg=0,yArg=0,cArg=4,dnameArg="", villoArg="", kataArg="", kata2Arg=""):
    logging.debug( "SPEDISCITRUPPE "+' '.join(map (str,[t1Arg,t2Arg,t3Arg,t4Arg,t5Arg,t6Arg,t7Arg, t8Arg, t9Arg, t10Arg,t11Arg,xArg,yArg,cArg,dnameArg, villoArg,kataArg]) )   )
    time.sleep(0.1)
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    global t11
    global xx
    global yy
    global c
    global dname
    global kata
        
    t1=t1Arg
    t2=t2Arg
    t3=t3Arg
    t4=t4Arg
    t5=t5Arg
    t6=t6Arg
    t7=t7Arg
    t8=t8Arg
    t9=t9Arg
    t10=t10Arg
    t11=t11Arg
    kata = kataArg
    
    xx=xArg
    yy=yArg
    c=cArg
    dname = dnameArg

    cookie_data=[]
    tca = travian_buildtruppe()
    tct = travian_confermatruppe()

    if (villoArg == ""):
        urltroops =travian_account.sendtroops_page
    else:
        urltroops = travian_account.sendtroops_page+"?z="+villoArg 
        
    html_ca = travian_login.openurl(urltroops)
        
    logging.debug(urltroops)
    test_ca = html_ca.read()
    tca.feed(test_ca)
    tca.get_cookie(cookie_data)
    
    cookie_data = urllib.urlencode(cookie_data)
    result = socket_travian.travian_cookie(cookie_data, travian_account.sendtroops_page )
    time.sleep(0.2)
    

    if (result != None):
        gottenresult = result.read()
        new_cookie_data=[]
        tct.feed(gottenresult)
        tct.get_cookie(new_cookie_data)
        if (kataArg != ""):
            new_cookie_data.append(('kata', kataArg))
        if (kata2Arg != ""):
            new_cookie_data.append(('kata2', kata2Arg))

        new_cookie_data = urllib.urlencode(new_cookie_data)
        result = socket_travian.travian_cookie(new_cookie_data, travian_account.sendtroops_page )
        
    else:
        logging.debug(" TRAVIAN_COOKIE - KONNTE NICHT SENDEN ")

def addestradecurione(t10Arg = 0):
    logging.debug("ADDESTRADECURIONE = "+str( t10Arg))
    global t10
    t10 = t10Arg
    cookie_data=[]
    tca = travian_buildtruppe()
    html_ca = travian_login.openurl(travian_account.residence_page)
    test_ca = html_ca.read()
    tca .feed(test_ca)
    tca .get_cookie(cookie_data)
    cookie_data = urllib.urlencode(cookie_data)
    socket_travian.travian_cookie(cookie_data, travian_account.build_page )

def addestracavalleria(t4Arg = 0, t5Arg = 0, t6Arg = 0, t3Arg = 0, stable_Arg = ""):
    global t4
    global t3
    global t5
    global t6
    if (stable_Arg == ""):
        stable_Arg = travian_account.stable_page
    logging.debug("ADDESTRACAVALLERIA "+ " ".join( map(str,[t4Arg, t5Arg, t6Arg, t3Arg, stable_Arg])))
    t3 = t3Arg
    t4 = t4Arg
    t5 = t5Arg
    t6 = t6Arg
    cookie_data=[]
    tca = travian_buildtruppe()
    html_ca = travian_login.openurl(stable_Arg )
    test_ca = html_ca.read()
    tca .feed(test_ca)
    tca .get_cookie(cookie_data)
    cookie_data = urllib.urlencode(cookie_data)
    socket_travian.travian_cookie(cookie_data, travian_account.build_page )

def addestraassedio(t7Arg = 0, t8Arg = 0):
    global t7
    global t8
    logging.debug("ADDESTRAASSEDIO "+ " ".join( map(str,[t7Arg, t8Arg])))
    t7 = t7Arg
    t8 = t8Arg
    
    cookie_data=[]
    tca = travian_buildtruppe()
    html_ca = travian_login.openurl('build.php?gid=21')
    test_ca = html_ca.read()
    
    tca .feed(test_ca)
    tca .get_cookie(cookie_data)
    cookie_data = urllib.urlencode(cookie_data)
    socket_travian.travian_cookie(cookie_data, travian_account.build_page )
    
    
    
def addestrafanti(t1Arg = 0, t2Arg = 0, t3Arg = 0, t4Arg = 0, caserma_Arg = ""):
    global t1
    global t2
    global t3
    global t4
    if (caserma_Arg == ""):
        caserma_Arg = travian_account.barracks_page
    logging.debug("ADDESTRAFANTI "+" ".join( map(str,[t1Arg, t2Arg, t3Arg, t4Arg,caserma_Arg])))
    
    t1 = t1Arg
    t2 = t2Arg
    t3 = t3Arg
    t4 = t4Arg
    cookie_data=[]
    tca = travian_buildtruppe()
    html_ca = travian_login.openurl(caserma_Arg)
    test_ca = html_ca.read()
    tca .feed(test_ca)
    tca .get_cookie(cookie_data)
    cookie_data = urllib.urlencode(cookie_data)
    socket_travian.travian_cookie(cookie_data, travian_account.build_page )
    
def truppe_teutoni5(argAtt=0, argDef= 0,argRaid = 0, argPala = 0, argScout = 0):
    if (random.randint(1,5) == 3):
        logging.debug(" RAND YES , TRUPPO")
        truppe_teutoni(argAtt, argDef, argRaid, argPala, argScout)
    else:
        logging.debug( " RAND NO,  NON TRUPPO")
        
def difesa_truppe_teutoni():
    slist = get_slist()
    avail = travian_caserma.get_available_truppe()
    if (slist > 2):
        spediscitruppe(0,avail[1],0, avail[3], avail[4],0,0,0,0,0,0,xArg, yArg, cArg, dnameArg)

def difesa_truppe_galli():
    slist = get_slist()
    avail = travian_caserma.get_available_truppe()
    if (slist > 2):
        spediscitruppe(avail[0],0,avail[2], 0, avail[4],0,0,0,0,0,0,xArg, yArg, cArg, dnameArg)

        
def truppe_teutoni(argAtt=0, argDef= 0,argRaid = 0, argPala = 0, argScout = 0, argCata = 0, argArie = 0, argCavava = 0, argGrande = 0):
    logging.debug("TRUPPE_TEUTONI "+" ".join( map(str,[argAtt, argDef, argRaid, argPala,argScout, argCata, argArie,argCavava ])))

    if (argArie):
        addestraassedio(t7Arg=1)            

    if (argCata):
        addestraassedio(t8Arg=1)
    
    if (argCavava):
        if (argGrande):
            addestracavalleria(t6Arg=1, stable_Arg = "build.php?gid=30")       
        else:
            addestracavalleria(t6Arg=2)            
    
    if (argRaid):
        if (argGrande):
            addestrafanti(t1Arg=3, caserma_Arg = "build.php?gid=29")       
        else:
            addestrafanti(t1Arg=5)  
    if (argAtt):
        addestrafanti(t3Arg=4)       
        
        addestracavalleria(t6Arg=2)       
    if (argDef):
        addestrafanti(t2Arg=4)       
        
    if (argPala):      
        addestracavalleria(t5Arg=2)     
    if (argScout):
        addestrafanti(t4Arg=2)       
        
    
def truppe_galli(argAtt=0, argDef= 0,argRaid = 0, argPala = 0,  argScout = 0, argCata = 0, argArie = 0):
  
    
    if (argRaid):
        addestracavalleria(t4Arg=2)       
    if (argAtt):
        addestrafanti(t2Arg=4)       
        addestrafanti(t2Arg=2, caserma_Arg = "build.php?gid=29")       
        addestracavalleria(t6Arg=2)       
        addestracavalleria(t6Arg=1, stable_Arg = "build.php?gid=30")       
    if (argDef):
        addestrafanti(t1Arg=4)       
       
    if (argScout):
        addestracavalleria(t3Arg=2)       
    if (argPala):
        addestracavalleria(t5Arg=2)       
    if (argCata):
        addestraassedio(t8Arg=1)
    if (argArie):
        addestraassedio(t7Arg=1)
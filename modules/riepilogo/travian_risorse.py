from sgmllib import SGMLParser
import urllib2, time, travian_account, travian_login
import travian_language, string, travian_resdorf
import logging

risorse_dict = {}
MER_TRAN = 750
MER_COEF = 75
MER_COM = 2000
MER_CHK = 1000
MER_MAX = 80000

def init_coef():
    global MER_COEF
    global MER_TRAN
    global MER_COM
    global MER_CHK
    
    
    MER_COEF = int(travian_account.mer_coef)
    MER_TRAN = MER_COEF*10
    MER_COM = MER_TRAN*3
    MER_CHK = MER_TRAN*2
    

class villaggio_risorse:

    
    def __init__(self,villaggioArg, legnoArg, argillaArg, ferroArg, granoArg, lpArg, apArg, fpArg, gpArg):
        self.villaggio = villaggioArg
        
        self.legno = self.parse_string(legnoArg)
        self.argilla = self.parse_string(argillaArg)
        self.ferro = self.parse_string(ferroArg) 
        self.grano = self.parse_string(granoArg)  
        
        self.legnoMax = self.calc_max(self.legno, lpArg)
        self.argillaMax = self.calc_max(self.argilla, apArg)
        self.ferroMax = self.calc_max(self.ferro, fpArg)
        self.granoMax = self.calc_max(self.grano, gpArg)
        
    def parse_string(self, arg):
        result = arg.replace(",","")
        result = result.replace(".","")
        return int(result)
    def calc_max(self, arg, argPer):
        perInt = int(argPer.replace("%",""))
        if (perInt > 0):
            magQuant = arg / perInt * 100
        else:
            magQuant = MER_MAX
        return magQuant
    
    def __repr__(self):
        return ("(legno= "+str(self.legno)+"/"+str(self.legnoMax)+",argilla= "+str(self.argilla)+"/"+str(self.argillaMax)+",  ferro= "+str(self.ferro)+"/"+str(self.ferroMax)+", grano="+str(self.grano)+"/"+str(self.granoMax)+")")


    
class travian_risorse(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.risorse_dict = {}
        self.invillaggio = 0        
        self.inline = 0
        self.invillaggioname= 0
        self.indicerisorsa = 0
        self.currentvillaggio = ""
        self.td = 0
        self.tmpimage = ""
    def start_tr(self, attrs):
        if (self.invillaggio ==1):
            self.inline= 1
            
    def end_tr(self):
       
        self.inline= 0
        self.indicerisorsa= 0
        self.invillaggioname= 0
        self.currentvillaggio = ""
        

    def start_a(self, attrs):
        if ((self.inline == 1) and (self.invillaggioname == 0)):
            self.invillaggioname = 1
   
    def start_table(self, attrs):
        pass
        
        
  
    def end_table(self):
        if (self.invillaggio == 1):
            self.invillaggio = 2

    def start_td(self, attrs):
        self.td = 1
        self.tmpimage = ""

    def end_td(self):
        self.td = 0
        self.invillaggioname == 1
        if ((self.invillaggio == 1) and (self.indicerisorsa > 1)):
             self.risorse_dict[self.currentvillaggio].append(self.tmpimage)
        

    def start_img(self, attrs):
        ids = [v for k, v in attrs if k=='id']
        srcs =[v for k, v in attrs if k=='src']
        titles =[v for k, v in attrs if k=='title']
       
        if ( (self.invillaggio == 1) and (self.indicerisorsa >= 1) and (self.td == 1)):
          
            
            if (len(srcs) > 0):
                
                self.tmpimage = self.tmpimage + srcs[0]
            
    def handle_data(self,text):
       
        if ((string.upper(travian_language.villaggio) == string.upper(text)  ) and (self.invillaggio == 0)):
            self.invillaggio = 1
        elif ( (self.invillaggio == 1) and (self.invillaggioname == 1) and (self.currentvillaggio == "")):
            self.risorse_dict[text] = []
            self.invillaggioname = 0
            self.indicerisorsa = 1
            self.currentvillaggio = text
        elif ( (self.invillaggio == 1) and (self.indicerisorsa >= 1) and (self.td == 1)):
            self.tmpimage = self.tmpimage + text
            #self.risorse_dict[self.currentvillaggio].append(text)
            self.indicerisorsa =  self.indicerisorsa + 1

     
    def get_risorse(self):
        return self.risorse_dict
    
def get_risorse():
    cookie_data=[]
    tca = travian_risorse()
    html_ca = travian_login.openurl(travian_account.risorse_page)
    test_ca = html_ca.read()
    tca.feed(test_ca)
    return tca.get_risorse()


def get_riepilogo():
    cookie_data=[]
    tca = travian_risorse()
    html_ca = travian_login.openurl(travian_account.riepilogo_page)
    test_ca = html_ca.read()
    tca.feed(test_ca)
    return tca.get_risorse()



def get_magazzino():
    cookie_data=[]
    tca = travian_risorse()
    html_ca = travian_login.openurl(travian_account.magazzino_page)
    test_ca = html_ca.read()
    tca.feed(test_ca)
    return tca.get_risorse()

def livello_commerciale():
    linkUfficioCommerciale = travian_resdorf.get_link_edificio(travian_language.ufficio_commerciale)
    if (len(linkUfficioCommerciale)  > 0):
        return linkUfficioCommerciale[0].livello
    else:
        return 0

def livello_municipio():
    linkMunicipio = travian_resdorf.get_link_edificio(travian_language.municipio)
    if (len(linkMunicipio)  > 0):
        return int(linkMunicipio[0].livello)
    else:
        return 0

def grande_festa_possibile():
    return livello_municipio() >= 10
    
def has_municipio():
    linkMunicipio = travian_resdorf.get_link_edificio(travian_language.municipio)
    if (len(linkMunicipio)  > 0):
        return 1
    else:
        return 0
    
def has_mercanti(villo):
    dictrisorse =  get_risorse();
    if (villo in dictrisorse):
        risvillo = dictrisorse[villo] 
        mercanti = risvillo[4]
        disparray = string.split(mercanti, "/")
        
        return (disparray[0]== disparray[1])    
    else:
        return 0
        
def numero_mercanti(villo):
    dictrisorse =  get_risorse();
    if (villo in dictrisorse):
        risvillo = dictrisorse[villo] 
        mercanti = risvillo[4]
        disparray = string.split(mercanti, "/")
        
        return int(disparray[0])    
    else:
        return 0


def get_villaggio_risorse():
    dictrisorse = get_risorse()
    dictmagazzino = get_magazzino()
    dictvillris = {}
    for risorsavill in dictrisorse.keys():
        ari = dictrisorse[risorsavill]   
        arm = dictmagazzino[risorsavill]   
       
        vr = villaggio_risorse(risorsavill, ari[0],ari[1], ari[2], ari[3], arm[0], arm[1], arm[2], arm[4] ) 
        dictvillris[risorsavill] = vr
    return dictvillris 


def sotto_attacco(villo):
    dictriepilogo =  get_riepilogo();
    risvillo = dictriepilogo[villo] 
    risvillfirst = risvillo[0]
    return risvillfirst.find("att1") > -1
    
def quantita_trasferibile():
    mlc = int(livello_commerciale())
    metran = MER_TRAN+mlc*MER_COEF
    return metran

def risorse_trasferibili(villo):
    return quantita_trasferibile()*numero_mercanti(villo)

def normalizza_quantita(quantita):
    if (quantita > 0):
        qta = quantita_trasferibile()
        nummercanti = 0
        while (((nummercanti+1)*qta) <= quantita):
            nummercanti = nummercanti+1
        quantitamerce = nummercanti * qta
        return quantitamerce        
    else: 
        return 0

def quantita_trasferire(dictvills, vln1, vln2):
    print dictvills
    print vln1
    print vln2
    if ((vln1 in dictvills) and (vln2 in dictvills)):
        vr1 = dictvills[vln1]
        vr2 = dictvills[vln2]
        
        trarr = [0,0,0,0]
        diff_legno = vr1.legno-vr2.legno
        diff_argilla = vr1.argilla-vr2.argilla
        diff_ferro = vr1.ferro-vr2.ferro
        diff_grano= vr1.grano-vr2.grano
        
        logging.debug("DIFF MERCE "+str([diff_legno, diff_argilla, diff_ferro, diff_grano]))
        
        mlc = int(livello_commerciale())
        mercom = MER_COM+mlc*MER_COEF
        merchk = MER_CHK+mlc*MER_COEF
        metran = MER_TRAN+mlc*MER_COEF
    
        logging.debug("MERCOM = "+str(mercom))
    
        logging.debug("MERCHK = "+str(merchk))
        logging.debug("METRAN = "+str(metran))

        addedstuff = False
        
        while True:
            logging.debug("IN LOOP")
            if ((diff_legno > mercom) and ((vr2.legno + merchk) < vr2.legnoMax)):
                
                logging.debug(" ADDING LEGNO "+str(metran))
                trarr[0] = trarr[0]+ metran 
                vr2.legno = vr2.legno+metran 
                diff_legno = diff_legno -  metran 
                addedstuff = True
                 
            if ((diff_argilla> mercom ) and ((vr2.argilla+ merchk ) < vr2.argillaMax)):
                logging.debug(" ADDING ARGILLA "+str(metran))
                
                trarr[1] = trarr[1] + metran
                vr2.argilla = vr2.argilla+metran
                diff_argilla = diff_argilla -  metran 

                addedstuff = True
            if ((diff_ferro > mercom ) and ((vr2.ferro + merchk ) < vr2.ferroMax)):
                logging.debug(" ADDING FERRO "+str(metran))

                trarr[2] = trarr[2] + metran 
                vr2.ferro= vr2.ferro+metran 
                diff_ferro = diff_ferro -  metran 

                addedstuff = True
        
            if ((diff_grano > mercom  ) and ((vr2.grano + merchk ) < vr2.granoMax)):
                logging.debug(" ADDING GRANO "+str(metran))

                trarr[3] = trarr[3] + metran 
                vr2.grano= vr2.grano+metran 
                diff_grano = diff_grano -  metran 

                addedstuff = True
                
            if (addedstuff == False):
                break
            else:
                addedstuff = False
                
        logging.debug("TRANSFER MERCE "+str(trarr))
        
        return trarr
    else:
        logging.info( "villo missing , not considered ")
        return None
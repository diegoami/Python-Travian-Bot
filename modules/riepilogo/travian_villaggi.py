import sys,time, random, string,re,os
import urllib, urllib2, travian_account,socket_travian
import travian_login, travian_language
import logging

from sgmllib import SGMLParser

coords_list = []

class linkVillaggio:
    def __init__(self,villaggio_id, villaggio_nome):
        self.villaggio_id= villaggio_id
        self.villaggio_nome= villaggio_nome
        
    def __repr__(self):
        return ("(nome= "+self.villaggio_nome+",  id = "+self.villaggio_id+")")

    
def get_curr_coords(icounter):
    if (icounter < len(coords_list)):
        coord_curr_line = coords_list[icounter].rstrip("\n")
       
        parts = string.split(coord_curr_line, " ")

        villo, xp, yp = parts
    
        return [xp, yp]
    else:
        return [travian_account.xp_start, travian_account.yp_start]

    
def setup_coords(filename):
   
    global coords_list

    try:
        filescoordsname = os.path.join("config",filename)
     
        filecoords=open(filescoordsname ,'r')
     
        coords_list=filecoords.readlines()  
    except:
        logging.exception("COULD NOT OPEN "+ filename)
        print sys.exc_info()

    
class travian_villaggi(SGMLParser):
    def reset(self):
        self.linksfound = 0
        SGMLParser.reset(self)
        self.villaggi = []
        self.villaggidict = dict()
        self.invillaggio = 0
        self.currentid = ""
        
    def start_a(self,attrs):
        if (self.linksfound == 0):
            p = re.compile('\?newdid=([0-9]+)')
            a_tag = [v for k, v in attrs if k=='href']
            
            if "newdid" in a_tag[0]:
                
                self.invillaggio = 1
                m = p.match(a_tag[0])
                self.currentid= m.group(1)
    def handle_data(self,text):
        if (text.find("Links:") > -1):
            self.linksfound = 1
        if (self.linksfound == 0):
            if (self.invillaggio == 1):
                self.invillaggio = 0
                villaggio = linkVillaggio(self.currentid, text)
                self.villaggi.append(villaggio)
                self.villaggidict[text] = villaggio
    def get_villaggi(self):
        return self.villaggidict

def getvillaggi():
    vills = travian_villaggi()
    
    building_page_html=travian_login.openurl(travian_account.building_page)
    
    production_page_testo = building_page_html.read()
    vills .reset()
    vills .feed(production_page_testo)

    return vills.get_villaggi()


def get_other_villaggi(butvill):        
    vills = getvillaggi()
    del vills[butvill]
    return vills
 
def get_villaggio(villarg):   
    vills = getvillaggi()
    return vills[villarg]


def vaiavillaggio(dict, vill_name):
    logging.debug("VAI A VILLAGGIO "+ str( vill_name))
    lvill = dict[vill_name]
    villhref = travian_account.home_page+"?newdid="+str(lvill.villaggio_id)

    travian_login.openurl(villhref)


 
 

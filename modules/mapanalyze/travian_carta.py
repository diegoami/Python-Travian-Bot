
import sys,time, random,string
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_url
from sgmllib import SGMLParser
import logging

allcenters =[]
allvillaggi =[]
alranalyzed = dict()
class travianCarta(SGMLParser):
    
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
            if "xp" in nome:
                valore[0]=self.xp
            if "yp" in nome:
                valore[0]=self.yp
          
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
        
class travianLeggiCarta(SGMLParser):
    def reset(self):
      
        SGMLParser.reset(self)
        self.data = []
        self.images = dict()
        self.areas = dict()
        
    def start_div(self, attrs):
        
        ids = [v for k, v in attrs if k=='id']
        srcs =[v for k, v in attrs if k=='class']
        if (len(ids) > 0 and (len(srcs) > 0 )):
            self.images[ids[0]] = srcs[0]
        
    def start_area(self, attrs):
        ids = [v for k, v in attrs if k=='id']
        hrefs =[v for k, v in attrs if k=='href']    
        if (len(ids) > 0):
            self.areas [ids[0]] = hrefs[0]
    def get_center_village(self):
        villages = []
       
        for imagekey in self.images.keys():
            imagevalue=self.images[imagekey]
            if ('b' in imagevalue):
                karkey = imagekey.replace("i","a")
                
                if (karkey == "a_3_3"):
                    
                    if (self.areas.has_key(karkey)):
                    
                        areavalue = self.areas[karkey]
                        villages.append(areavalue)
        return villages        
    
    def get_villages(self):
        
        
        villages = []
       
        for imagekey in self.images.keys():
            logging.debug("IMAGEKEY "+imagekey)

            imagevalue=self.images[imagekey]
            if ('b' in imagevalue):
                logging.debug("IMAGEVALUE "+imagevalue)
                karkey = imagekey.replace("i","a")
               
                if (self.areas.has_key(karkey)):
                
                    areavalue = self.areas[karkey]
                    villages.append(areavalue)
        return villages        
        
#    def get_villages(self):
#        villages = []
#       
#        for areakey in self.areas.keys():
#        
#            logging.debug("areakey "+areakey)
#            
#            if (self.areas.has_key(karkey)):
#                areavalue = self.areas[karkey]
#                villages.append(areavalue)
#                
#                    
#        return villages

       

  
def ricercafarm(x,y, onlycenter = 0):
    time.sleep(0.3)
    cookie_data=[]
    logging.debug("RICERCAFARM "+str(x)+" "+str(y))
    trf = travianCarta(x,y)
    trf.reset()
    html_ca = travian_login.openurl(travian_account.carta_page)
 
    test_ca = html_ca.read()

    trf.feed(test_ca)
    trf.get_cookie(cookie_data)

    cookie_data = urllib.urlencode(cookie_data)
    logging.debug(travian_account.carta_page)
    result = socket_travian.travian_cookie(cookie_data, travian_account.carta_page)

    if (result != None):
        tlc = travianLeggiCarta()
        tlc.reset()

        tlc.feed(result.read() )
        if (onlycenter == 1):
            return tlc.get_center_village()
        else:
            logging.debug( tlc.get_villages())
            return tlc.get_villages()
    else:
        return None
        
    
def verify(x,y,allcenters):
 #   logging.debug("verifying "+str(x)+ " "+str(y))

    for xa in range(x-3, x+3):
        for ya in range(y-3, y+3):
            found = 0
#            logging.debug("scanning "+ str(xa)+ " "+ str(ya))
            
            for center in allcenters:
#                logging.debug("Trying "+str(center))
                if (center[0]-3 <= xa and center[0]+3 >= xa and center[1]-3 <= ya and center[1]+3 >= ya):
#                    logging.debug("found "+str(center[0])+" "+str(center[1]))
                    found = 1
                    break
            if (found == 0):    
#                logging.debug("not found, will add "+str(x)+ " "+str(y))    
                return 1
#    logging.debug("will not add "+str(x)+ " "+str(y))    
    
    return 0
def ricercafarmrec(x,y,dist):
   
    #logging.debug( " RICERCAFARMREC "+ " ".join([str(x),str( y) ,str( dist)]))
    
    if (dist == 0):
        if not ((x,y) in allcenters):
            if (verify(x,y, allcenters)):
                logging.debug( " APPENDING "+ " ".join([str(x),str( y) ]))
                allcenters.append((x,y))
            
   
       
    else:
        ricercafarmrec(x-7,y,dist-1)
        ricercafarmrec(x+7,y,dist-1)
        ricercafarmrec(x,y-7,dist-1)
        ricercafarmrec(x,y+7,dist-1)
        ricercafarmrec(x,y,dist-1)
        
        
def get_all_centers():
    return allcenters

def get_villages_from_centerlist():
    villages = []
    centers = set(allcenters)
    for center in centers:
        logging.debug("ANALYZING "+str(center))
        villsfound = ricercafarm(center[0], center[1])
        for vill in villsfound:
            if (not(vill in villages)):
                villages.append(vill)
        #logging.debug(  "villages "+ str( villages) )

    return villages

def get_villaggi_for_list(coordlist ,dist):
    global allcenters
    allcenters =[]
    researches=[]
    for coord in coordlist:
        logging.debug("VILLAGGIO = "+str(coord))
        parts = string.split(coord , " ")
        logging.debug("PARTS= "+str(parts))
        
    
        villo, xp, yp = parts
        toresearch = (int(xp),int(yp))
        if (not(toresearch in researches)):
            ricercafarmrec(int(xp),int(yp),dist)
            researches.append(toresearch)
        else:
            logging.debug("SKIPPING THIS ONE ")
    return get_villages_from_centerlist()        
    
def get_all_villaggi(x,y,dist):
    global allcenters
    allcenters =[]
    ricercafarmrec(x,y,dist)
    logging.debug("ALLCENTERS = "+str(allcenters))
    return get_villages_from_centerlist()        


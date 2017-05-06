import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import  travian_language, travian_func
import urllib2, time, travian_account
import logging

from sgmllib import SGMLParser
priorita_dict = {}
massimo_dict = {}
class linkEdificio:
    def __init__(self,area_href, area_title):
        self.href = area_href
        self.title = area_title
        self.nome = ""
        self.livello = -1
        if (self.title.find( travian_language.livello) > -1):
            title_words = string.split(self.title)
            self.livello = string.join(title_words[-1:])
            self.nome  = string.join(title_words[0:-2])
    def __repr__(self):
        if (self.livello == -1):
            return ("(titolo = "+self.title+",  href = "+self.href+")")
        else:
            return ("(edificio= "+self.nome+",livello = "+str(self.livello)+",  href = "+self.href+")")
class linkResource:
    
    
    
    def __init__(self,area_href, area_title):
        self.href = area_href
        self.title = area_title
        self.livello = -1
        self.priorita_risorsa = 10000
        self.nome = ""
                           
                         
        title_words = string.split(self.title)
        if (self.title.find( travian_language.livello) > -1):
            title_words = string.split(self.title)
            self.livello = string.join(title_words[-1:])
            self.nome  = string.join(title_words[0:-2])
            if (priorita_dict.has_key(string.upper(self.nome))):
                self.priorita_risorsa = priorita_dict[string.upper(self.nome)];
                
            else:
                self.priorita_risorsa = 10000
            if (massimo_dict.has_key(string.upper(self.nome))):
                massimo_lev = massimo_dict[string.upper(self.nome)]
              
                if (int(self.livello) >= int(massimo_lev)):
                    self.priorita_risorsa = 10000
                
                
    def calc_priorita(self):            
        return (int(self.livello)+1)*int(self.priorita_risorsa)
    def __repr__(self):
        return ("(nome = "+self.nome+", livello = "+str(self.livello)+", href = "+self.href+",cmpvalue="+str(self.calc_priorita())+")")
    def __cmp__(self, other):
        return cmp(self.calc_priorita(), other.calc_priorita())
    def __str__(self):
        return ("nome = "+self.nome+", livello = "+str(self.livello)+", href = "+self.href)

class travianResource(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.buildurls = []
        self.buildlinks = []

    def start_area(self,attrs):
        area_href = [v for k, v in attrs if k=='href']
        area_title = [v for k, v in attrs if k=='title']
        area_entry = [area_href, area_title]
        linkRes = linkResource(area_href[0], area_title[0])
        self.buildlinks
        foundbefore = filter(lambda buildlink: string.upper(buildlink.title) == string.upper(linkRes.title), self.buildlinks)
        if "build.php?" in area_href[0]:
            self.buildurls.extend(area_entry )
            if (len(foundbefore) == 0):
                self.buildlinks.append(linkRes )
    def get_urls(self):
        return self.buildurls
    def get_links(self):
        self.buildlinks.sort()
        return self.buildlinks
    

class travianBuilding(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.buildurls = []
        self.buildlinks = []

    def start_area(self,attrs):
        area_href = [v for k, v in attrs if k=='href']
        area_title = [v for k, v in attrs if k=='title']
        area_entry = [area_href, area_title]
        linkEdi = linkResource(area_href[0], area_title[0])
        
        if "build.php?" in area_href[0]:
            self.buildurls.extend(area_entry )
            self.buildlinks.append(linkEdi )
            
    def get_urls(self):
        return self.buildurls
    def get_links(self):
        return self.buildlinks

def create_travian_resource():
    travianRes = travianResource()
    
    production_page_html=travian_login.openurl(travian_account.home_page)
    
    production_page_testo = production_page_html.read()
    travianRes.reset()
    travianRes.feed(production_page_testo)
    return travianRes
    
def create_travian_building():
    travianBui = travianBuilding()
    
    building_page_html=travian_login.openurl(travian_account.building_page)
    
    production_page_testo = building_page_html.read()
    travianBui.reset()
    travianBui.feed(production_page_testo)
    return travianBui    
    
def get_resource_urls():
    travianRes  = create_travian_resource()
    return travianRes.get_urls()
        
def get_resource_links():
    travianRes  = create_travian_resource()
    return travianRes.get_links()

def get_building_links():
    travianBui  = create_travian_building()
    return travianBui.get_links()

def get_spazi_edificabili():
    buildingLinks = get_building_links()
    spaziEdificabili = filter(lambda buildlink: string.upper(buildlink.title) == string.upper(travian_language.spazio_edificabile), buildingLinks)    
    return spaziEdificabili 

def get_edifici():
    buildingLinks = get_building_links()
    edifici = filter(lambda buildlink: buildlink.livello > -1, buildingLinks)    
    return edifici

def get_link_edificio(nome):
    edificiLinks = get_edifici()
    edificiTrovaLinks = filter(lambda edificiLink : string.upper(edificiLink.nome) == string.upper(nome), edificiLinks)
    return edificiTrovaLinks 

def get_link_edificio_from(nome, edificiLinks):
    edificiTrovaLinks = filter(lambda edificiLink : string.upper(edificiLink.nome) == string.upper(nome), edificiLinks)
    return edificiTrovaLinks 

def get_all_reslinks():
    reslinks = get_resource_links()
    edificiLinks = get_edifici()
    reslinks.extend(edificiLinks)
    reslinks.sort()
    return reslinks

def build_random_resource():
    
    LINK_SUB_LIST = 5

    LINK_SUB_LIST = travian_account.link_sub_list
    reslinks = get_all_reslinks()
    
    subreslinks = reslinks[:LINK_SUB_LIST]
    logging.debug("RES LINKS ...")
    logging.debug(subreslinks)
    for slink in subreslinks[:]:
        
        time.sleep(1)
        resultbuild = travian_func.build(slink.href) 
        if (resultbuild == 1):
            break
    if (len(subreslinks) > 0):
        return subreslinks[0].livello    
    else:
        return 0

                
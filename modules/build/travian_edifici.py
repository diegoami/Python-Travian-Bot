
from sgmllib import SGMLParser
import urllib2, time, travian_account, travian_login, travian_resdorf
import travian_language, travian_func
import logging

class linkEdificio:
    def __init__(self,area_href, area_title):
        self.href = area_href
        self.title = area_title
    def __repr__(self):
        return ("(nome_edificio= "+self.title+",  href = "+self.href+")")
    
class travian_builder(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.linkedifici = []
        self.inedificio = 0
    def start_h2(self, attrs):
        self.inedificio = 1
    def start_a(self, attrs):
        if (self.inedificio ==2):
            a_tag = [v for k, v in attrs if k=='href']
            self.linkedificio = a_tag[0]
            linkEdi = linkEdificio(self.linkedificio, self.edificio)
            if (self.linkedificio != "#"):
                self.linkedifici.append(linkEdi)
            self.inedificio =0 
    def handle_data(self,text):
         if (self.inedificio == 1):
             self.edificio = text

             self.inedificio = 2
     

    def get_links(self):
        return self.linkedifici
    
    
def get_link_edifici(spazio_link):
    
    trBuilder = travian_builder()
    trBuilder.reset()
    urlfeedpage = spazio_link
    builder_page_html=travian_login.openurl(urlfeedpage)
    
    builder_page_testo = builder_page_html.read()
    trBuilder.feed(builder_page_testo )
    return trBuilder.get_links()

def build_missing_edificio(edl , liv_to_build , nome_edif , minliv):
        
    link_edificio = travian_resdorf.get_link_edificio_from(nome_edif ,edl)
    if (minliv >= liv_to_build):
        if (len(link_edificio ) == 0):
            logging.debug( "Trying to build " + str( nome_edif ))
            travian_func.build_edificio(nome_edif )
    
    
def build_missing_edifici(minlivArg):
    edificiLinks = travian_resdorf.get_edifici()
    
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.magazzino, liv_to_build = 2, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.granaio,liv_to_build = 2, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.mercato,liv_to_build = 3, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.caserma,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.campo_daddestramento,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.accademia,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.fabbro,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.scuderia ,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.residence ,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.esperto_trappole ,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.mulino ,liv_to_build = 6, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.fabbrica_mattoni,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.falegnameria ,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.fonderia ,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.forno ,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.circolo_degli_eroi,liv_to_build = 9, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.ufficio_commerciale,liv_to_build = 10, minliv = minlivArg)
    build_missing_edificio(edl = edificiLinks, nome_edif = travian_language.arena ,liv_to_build = 10, minliv = minlivArg)
        
    

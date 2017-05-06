import sys,time, random, string
import urllib, urllib2, travian_account,travian_login,socket_travian
import travian_url, travian_language, travian_caserma
import travian_resdorf
import logging

from sgmllib import SGMLParser

def setup_resources_inizio():
    print "setup_resources_inizio"
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '3', string.upper(travian_language.campo_legno) : '4', 
                             string.upper(travian_language.campo_grano) : '5', string.upper(travian_language.miniera_ferro) : '6', 
                             string.upper(travian_language.centro_del_villaggio) : '18'  ,

                             string.upper(travian_language.magazzino) : '23', string.upper(travian_language.granaio) : '25',
                             string.upper(travian_language.mercato) : '30', string.upper(travian_language.campo_daddestramento) : '40',
                             string.upper(travian_language.accademia) : '46', string.upper(travian_language.fabbro) : '48',
                             string.upper(travian_language.scuderia) : '50', string.upper(travian_language.residence) : '35',
                             string.upper(travian_language.esperto_trappole) : '44',    string.upper(travian_language.mulino) : '20' ,
                             string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                             string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                             string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                             string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                             string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                             string.upper(travian_language.ambasciata) : '100000'
                             
                              }
        
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                             string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                             string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                             string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                             string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                             string.upper(travian_language.accademia) : '5', string.upper(travian_language.fabbro) : '3',
                             string.upper(travian_language.scuderia) : '3', string.upper(travian_language.residence) : '1',
                             string.upper(travian_language.esperto_trappole) : '1',    string.upper(travian_language.mulino) : '1' ,
                             string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                             string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                             string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                             string.upper(travian_language.armeria) : '1', string.upper(travian_language.officina) : '20',
                             string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                             string.upper(travian_language.ambasciata) : '1'
                             
                             }

def setup_resources_conquista():
    print "setup_resources_inizio"
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '3', string.upper(travian_language.campo_legno) : '4', 
                             string.upper(travian_language.campo_grano) : '5', string.upper(travian_language.miniera_ferro) : '6', 
                             string.upper(travian_language.centro_del_villaggio) : '18'  ,

                             string.upper(travian_language.magazzino) : '23', string.upper(travian_language.granaio) : '25',
                             string.upper(travian_language.mercato) : '30', string.upper(travian_language.campo_daddestramento) : '40',
                             string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '48',
                             string.upper(travian_language.scuderia) : '50', string.upper(travian_language.residence) : '25',
                             string.upper(travian_language.esperto_trappole) : '44',    string.upper(travian_language.mulino) : '20' ,
                             string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                             string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                             string.upper(travian_language.ufficio_commerciale) : '45',  string.upper(travian_language.arena) : '40',
                             string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '3000000000',
                             string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                             string.upper(travian_language.ambasciata) : '100000'
                             
                              }
        
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                             string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                             string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                             string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                             string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                             string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '3',
                             string.upper(travian_language.scuderia) : '3', string.upper(travian_language.residence) : '20',
                             string.upper(travian_language.esperto_trappole) : '1',    string.upper(travian_language.mulino) : '5' ,
                             string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                             string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                             string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                             string.upper(travian_language.armeria) : '1', string.upper(travian_language.officina) : '1',
                             string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                             string.upper(travian_language.ambasciata) : '1'
                             
                             }

def setup_resources_espansione():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '11', 
                         string.upper(travian_language.campo_grano) : '12', string.upper(travian_language.miniera_ferro) : '13', 
                         string.upper(travian_language.centro_del_villaggio) : '5'  ,
                         string.upper(travian_language.magazzino) : '8', string.upper(travian_language.granaio) : '9',
                         string.upper(travian_language.mercato) : '15', string.upper(travian_language.campo_daddestramento) : '35',
                         string.upper(travian_language.accademia) : '25', string.upper(travian_language.fabbro) : '42',
                         string.upper(travian_language.scuderia) : '40', string.upper(travian_language.residence) : '25',
                         string.upper(travian_language.esperto_trappole) : '34',    string.upper(travian_language.mulino) : '20' ,
                         string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                         string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '25',
                         string.upper(travian_language.ufficio_commerciale) : '30',  string.upper(travian_language.arena) : '40',
                         string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                         string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '40',
                         string.upper(travian_language.ambasciata) : '100000'
                         
                          }
    
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                         string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                         string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                         string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                         string.upper(travian_language.accademia) : '10', string.upper(travian_language.fabbro) : '3',
                         string.upper(travian_language.scuderia) : '20', string.upper(travian_language.residence) : '10',
                         string.upper(travian_language.esperto_trappole) : '20',    string.upper(travian_language.mulino) : '5' ,
                         string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                         string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                         string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                         string.upper(travian_language.armeria) : '3', string.upper(travian_language.officina) : '3',
                         string.upper(travian_language.castello) : '10',  string.upper(travian_language.municipio) : '20',
                         string.upper(travian_language.ambasciata) : '1'
                         
                         }
    
                
def setup_resources_villi():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '11', 
                         string.upper(travian_language.campo_grano) : '12', string.upper(travian_language.miniera_ferro) : '13', 
                         string.upper(travian_language.centro_del_villaggio) : '5'  ,
                         string.upper(travian_language.magazzino) : '18', string.upper(travian_language.granaio) : '22',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '40',
                         string.upper(travian_language.accademia) : '28', string.upper(travian_language.fabbro) : '42',
                         string.upper(travian_language.scuderia) : '45', string.upper(travian_language.residence) : '15',
                         string.upper(travian_language.esperto_trappole) : '34',    string.upper(travian_language.mulino) : '40' ,
                         string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                         string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                         string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                         string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                         string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                         string.upper(travian_language.ambasciata) : '100000'
                         
                          }
    
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                         string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                         string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                         string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                         string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '20',
                         string.upper(travian_language.scuderia) : '20', string.upper(travian_language.residence) : '20',
                         string.upper(travian_language.esperto_trappole) : '20',    string.upper(travian_language.mulino) : '5' ,
                         string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                         string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                         string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                         string.upper(travian_language.armeria) : '20', string.upper(travian_language.officina) : '20',
                         string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                         string.upper(travian_language.ambasciata) : '1'
                         
                         }
    
    
def setup_resources_incerto():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '11', 
                         string.upper(travian_language.campo_grano) : '12', string.upper(travian_language.miniera_ferro) : '13', 
                         string.upper(travian_language.centro_del_villaggio) : '5'  ,
                         string.upper(travian_language.magazzino) : '18', string.upper(travian_language.granaio) : '22',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '40',
                         string.upper(travian_language.accademia) : '28', string.upper(travian_language.fabbro) : '1000000',
                         string.upper(travian_language.scuderia) : '45', string.upper(travian_language.residence) : '15',
                         string.upper(travian_language.esperto_trappole) : '1000000',    string.upper(travian_language.mulino) : '40' ,
                         string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                         string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                         string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                         string.upper(travian_language.armeria) : '100000', string.upper(travian_language.officina) : '1000000',
                         string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                         string.upper(travian_language.ambasciata) : '100000'
                         
                          }
    
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                         string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                         string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                         string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                         string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '3',
                         string.upper(travian_language.scuderia) : '20', string.upper(travian_language.residence) : '20',
                         string.upper(travian_language.esperto_trappole) : '1',    string.upper(travian_language.mulino) : '5' ,
                         string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                         string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                         string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                         string.upper(travian_language.armeria) : '1', string.upper(travian_language.officina) : '20',
                         string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                         string.upper(travian_language.ambasciata) : '1'
                         
                         }    
    
def setup_resources_speed():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '11', 
                         string.upper(travian_language.campo_grano) : '12', string.upper(travian_language.miniera_ferro) : '13', 
                         string.upper(travian_language.centro_del_villaggio) : '5'  ,
                         string.upper(travian_language.magazzino) : '18', string.upper(travian_language.granaio) : '22',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '40',
                         string.upper(travian_language.accademia) : '28', string.upper(travian_language.fabbro) : '42',
                         string.upper(travian_language.scuderia) : '45', string.upper(travian_language.residence) : '15',
                         string.upper(travian_language.esperto_trappole) : '34',    string.upper(travian_language.mulino) : '40' ,
                         string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                         string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                         string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                         string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                         string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                         string.upper(travian_language.ambasciata) : '100000'
                         
                          }
    
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                         string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                         string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                         string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                         string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '20',
                         string.upper(travian_language.scuderia) : '20', string.upper(travian_language.residence) : '20',
                         string.upper(travian_language.esperto_trappole) : '20',    string.upper(travian_language.mulino) : '5' ,
                         string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                         string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                         string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                         string.upper(travian_language.armeria) : '20', string.upper(travian_language.officina) : '20',
                         string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '1',
                         string.upper(travian_language.ambasciata) : '1'
                         
                         }    

def setup_resources_capitale():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '11', 
                         string.upper(travian_language.campo_grano) : '12', string.upper(travian_language.miniera_ferro) : '13', 
                         string.upper(travian_language.centro_del_villaggio) : '5'  ,
                         string.upper(travian_language.magazzino) : '18', string.upper(travian_language.granaio) : '22',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '40',
                         string.upper(travian_language.accademia) : '28', string.upper(travian_language.fabbro) : '42',
                         string.upper(travian_language.scuderia) : '45', string.upper(travian_language.residence) : '15',
                         string.upper(travian_language.esperto_trappole) : '54',    string.upper(travian_language.mulino) : '40' ,
                         string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                         string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                         string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                         string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                         string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '44',
                         string.upper(travian_language.ambasciata) : '100000'
                         
                          }
    
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '20', string.upper(travian_language.campo_legno) : '20', 
                         string.upper(travian_language.campo_grano) : '20', string.upper(travian_language.miniera_ferro) : '20', 
                         string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                         string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                         string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                         string.upper(travian_language.accademia) : '20', string.upper(travian_language.fabbro) : '20',
                         string.upper(travian_language.scuderia) : '20', string.upper(travian_language.residence) : '20',
                         string.upper(travian_language.esperto_trappole) : '20',    string.upper(travian_language.mulino) : '5' ,
                         string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                         string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '20',
                         string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                         string.upper(travian_language.armeria) : '20', string.upper(travian_language.officina) : '20',
                         string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                         string.upper(travian_language.ambasciata) : '1'
                         
                         }


def setup_resources_residence():
    travian_resdorf.priorita_dict =  {string.upper(travian_language.campo_argilla) : '21', string.upper(travian_language.campo_legno) : '22', 
                             string.upper(travian_language.campo_grano) : '23', string.upper(travian_language.miniera_ferro) : '24', 
                             string.upper(travian_language.centro_del_villaggio) : '13'  ,

                             string.upper(travian_language.magazzino) : '15', string.upper(travian_language.granaio) : '19',
                             string.upper(travian_language.mercato) : '30', string.upper(travian_language.campo_daddestramento) : '40',
                             string.upper(travian_language.accademia) : '46', string.upper(travian_language.fabbro) : '48',
                             string.upper(travian_language.scuderia) : '50', string.upper(travian_language.residence) : '5',
                             string.upper(travian_language.esperto_trappole) : '44',    string.upper(travian_language.mulino) : '40' ,
                             string.upper(travian_language.fabbrica_mattoni) : '20',    string.upper(travian_language.falegnameria) : '22',
                             string.upper(travian_language.fonderia) : '24' , string.upper(travian_language.circolo_degli_eroi) : '50',
                             string.upper(travian_language.ufficio_commerciale) : '35',  string.upper(travian_language.arena) : '40',
                             string.upper(travian_language.armeria) : '59', string.upper(travian_language.officina) : '300',
                             string.upper(travian_language.castello) : '23', string.upper(travian_language.municipio) : '48',
                             string.upper(travian_language.ambasciata) : '100000'
                             
                              }
        
    travian_resdorf.massimo_dict =  {string.upper(travian_language.campo_argilla) : '10', string.upper(travian_language.campo_legno) : '10', 
                             string.upper(travian_language.campo_grano) : '10', string.upper(travian_language.miniera_ferro) : '10', 
                             string.upper(travian_language.deposito_segreto) : '10' , string.upper(travian_language.centro_del_villaggio) : '20'  ,
                             string.upper(travian_language.magazzino) : '20', string.upper(travian_language.granaio) : '20',
                             string.upper(travian_language.mercato) : '20', string.upper(travian_language.campo_daddestramento) : '20',
                             string.upper(travian_language.accademia) : '5', string.upper(travian_language.fabbro) : '3',
                             string.upper(travian_language.scuderia) : '3', string.upper(travian_language.residence) : '1',
                             string.upper(travian_language.esperto_trappole) : '1',    string.upper(travian_language.mulino) : '1' ,
                             string.upper(travian_language.fabbrica_mattoni) : '5',    string.upper(travian_language.falegnameria) : '5',
                             string.upper(travian_language.fonderia) : '5' ,  string.upper(travian_language.circolo_degli_eroi) : '15',
                             string.upper(travian_language.ufficio_commerciale) : '20',  string.upper(travian_language.arena) : '20',
                             string.upper(travian_language.armeria) : '1', string.upper(travian_language.officina) : '20',
                             string.upper(travian_language.castello) : '20',  string.upper(travian_language.municipio) : '20',
                             string.upper(travian_language.ambasciata) : '1'
                             
                             }

    
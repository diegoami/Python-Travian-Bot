import sys, os
import logging



def setupresources(array_lenguage):
    global campo_argilla
    global campo_legno
    global miniera_ferro
    global campo_grano
    global spazio_edificabile
    
    global magazzino
    global granaio
    global centro_del_villaggio
    global deposito_segreto
    global mercato
    global livello
    global caserma
    global campo_daddestramento
    global accademia
    global fabbro
    global scuderia
    global residence
    global truppe
    global proprie_truppe
    global galli 
    global esperto_trappole
    global mulino
    global fabbrica_mattoni
    global falegnameria
    global fonderia
    global villaggio
    global forno
    global popolo
    global alleanza
    global proprietario
    global abitanti
    global popolazione
    global villaggi
    global tag
    global rank
    global punti
    global membri
    global circolo_degli_eroi
    global ufficio_commerciale
    global officina
    global castello
    global arena
    global armeria
    global municipio
    global ambasciata
    global arrivo
    global calcolo
    global oggetto
    global dataora
    global attaccante
    global perdite
    global bottino
    global difensore
    global prigionieri
    global sufficienti
    global informazioni
    global risorse
    global cavalleria_difesa   
    global legionario
    global combattente
    global romani
    
    


    campo_argilla=array_lenguage[0].rstrip("\n")
    campo_legno=array_lenguage[1].rstrip("\n")
    miniera_ferro=array_lenguage[2].rstrip("\n")
    campo_grano=array_lenguage[3].rstrip("\n")
    spazio_edificabile=array_lenguage[4].rstrip("\n")
    magazzino = array_lenguage[5].rstrip("\n")
    granaio = array_lenguage[6].rstrip("\n")
    centro_del_villaggio = array_lenguage[7].rstrip("\n")
    deposito_segreto = array_lenguage[8].rstrip("\n")
    mercato  = array_lenguage[9].rstrip("\n")
    livello = array_lenguage[10].rstrip("\n")
    caserma = array_lenguage[11].rstrip("\n")
    campo_daddestramento = array_lenguage[12].rstrip("\n")
    accademia = array_lenguage[13].rstrip("\n")
    fabbro = array_lenguage[14].rstrip("\n") 
    scuderia = array_lenguage[15].rstrip("\n") 
    residence = array_lenguage[16].rstrip("\n") 
    truppe = array_lenguage[17].rstrip("\n") 
    proprie_truppe = array_lenguage[18].rstrip("\n") 
    galli = array_lenguage[19].rstrip("\n") 
    esperto_trappole = array_lenguage[20].rstrip("\n") 
    mulino = array_lenguage[21].rstrip("\n") 
    fabbrica_mattoni = array_lenguage[22].rstrip("\n") 
    falegnameria = array_lenguage[23].rstrip("\n") 
    fonderia = array_lenguage[24].rstrip("\n") 
    forno = array_lenguage[25].rstrip("\n") 
    
    villaggio = array_lenguage[26].rstrip("\n") 
    popolo = array_lenguage[27].rstrip("\n") 
    alleanza = array_lenguage[28].rstrip("\n") 
    proprietario = array_lenguage[29].rstrip("\n") 
    abitanti = array_lenguage[30].rstrip("\n") 
    popolazione = array_lenguage[31].rstrip("\n") 
    villaggi = array_lenguage[32].rstrip("\n") 
    tag = array_lenguage[33].rstrip("\n") 
    rank = array_lenguage[34].rstrip("\n") 
    punti  = array_lenguage[35].rstrip("\n") 
    membri = array_lenguage[36].rstrip("\n") 
    circolo_degli_eroi = array_lenguage[37].rstrip("\n") 
    ufficio_commerciale = array_lenguage[38].rstrip("\n") 
    officina = array_lenguage[39].rstrip("\n") 
    castello = array_lenguage[40].rstrip("\n") 
    arena = array_lenguage[41].rstrip("\n") 
    armeria = array_lenguage[42].rstrip("\n") 
    municipio = array_lenguage[43].rstrip("\n") 
    ambasciata = array_lenguage[44].rstrip("\n") 
    arrivo = array_lenguage[45].rstrip("\n") 
    calcolo = array_lenguage[46].rstrip("\n") 
    oggetto = array_lenguage[47].rstrip("\n") 
    dataora = array_lenguage[48].rstrip("\n") 
    attaccante = array_lenguage[49].rstrip("\n") 
    perdite = array_lenguage[50].rstrip("\n") 
    bottino = array_lenguage[51].rstrip("\n") 
    difensore = array_lenguage[52].rstrip("\n") 
    prigionieri = array_lenguage[53].rstrip("\n") 
    sufficienti = array_lenguage[54].rstrip("\n") 
    informazioni = array_lenguage[55].rstrip("\n") 
    risorse = array_lenguage[56].rstrip("\n")
    cavalleria_difesa = array_lenguage[57].rstrip("\n")
    combattente = array_lenguage[58].rstrip("\n")
    legionario = array_lenguage[59].rstrip("\n")
    romani = array_lenguage[60].rstrip("\n") 
    
  
def get_all_nome_edifici():
    all_nome_edifici = [magazzino,granaio,mercato, caserma, campo_daddestramento, accademia, fabbro, scuderia, residence, esperto_trappole, mulino, fabbrica_mattoni, falegnameria, fonderia, forno, circolo_degli_eroi, ufficio_commerciale, arena, castello] 
    return all_nome_edifici  
    

      

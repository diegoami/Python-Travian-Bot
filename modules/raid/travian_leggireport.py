import sys,time, random, string, datetime, traceback
import urllib, urllib2,  socket_travian,  time, sys, travian_account, travian_resdorf
from threading import Timer
import travian_login, travian_resdorf, travian_edifici
import travian_account,travian_login,socket_travian, travian_language,re
from sgmllib import SGMLParser
import logging


ASPETTA_NIENTE=0
ASPETTA_OGGETTO=1
ASPETTA_DATA =2
ASPETTA_ATTACCANTE=3
ASPETTA_TRUPPE_ATTACCO=4
ASPETTA_PERDITE=5
ASPETTA_BOTTINO=6
ASPETTA_DIFENSORE=7
ASPETTA_PRIGIONIERI=9
ASPETTA_INFORMAZIONI=10
ASPETTA_TRUPPE_DIFESA=11

ASPETTA_FINITO=8

class raid_report:
    def __init__(self,oggetto, data, attaccante, truppe_attacco, perdite, bottino, difensore, truppe_difesa, tribu_difesa):
        self.oggetto=string.rstrip(oggetto,"\n")
        self.data=string.rstrip(data,"\n")
        self.attaccante=string.rstrip(attaccante,"\n")
        self.truppe_attacco=truppe_attacco
        self.truppe_difesa=truppe_difesa
        self.perdite = perdite
        self.bottino = bottino
        self.difensore = difensore
        self.tribu_difesa = tribu_difesa
        
        diflista = string.split(self.difensore, " ")
        self.playerdef =  diflista[0]
        datalista = string.split(self.data, " ")
        
        giorno =  datalista[1]
        ora = datalista[3]
        
        giornotupla = string.split(giorno, ".")
        oratupla = string.split(ora, ":")
        self.identif = 0

        
        self.reporttime = datetime.datetime(int(giornotupla[2])+2000, int(giornotupla[1]), int(giornotupla[0]), int(oratupla[0]), int(oratupla[1]), int(oratupla[2])) 
        
    def get_def_fanteria(self):
        if (self.tribu_difesa == "Romani"):
            result = self.truppe_difesa[0]*35+self.truppe_difesa[1]*65+self.truppe_difesa[2]*40+self.truppe_difesa[3]*20+self.truppe_difesa[4]*65+self.truppe_difesa[5]*80+self.truppe_difesa[6]*30+self.truppe_difesa[7]*60
        if (self.tribu_difesa == "Galli"):
            result = self.truppe_difesa[0]*40+self.truppe_difesa[1]*35+self.truppe_difesa[2]*20+self.truppe_difesa[3]*25+self.truppe_difesa[4]*115+self.truppe_difesa[5]*50+self.truppe_difesa[6]*30+self.truppe_difesa[7]*45
        if (self.tribu_difesa == "Teutoni"):
            result = self.truppe_difesa[0]*20+self.truppe_difesa[1]*35+self.truppe_difesa[2]*30+self.truppe_difesa[3]*10+self.truppe_difesa[4]*100+self.truppe_difesa[5]*50+self.truppe_difesa[6]*30+self.truppe_difesa[7]*60
        
        return result
        
    def get_def_cavalleria(self):
        if (self.tribu_difesa == "Romani"):
            result = self.truppe_difesa[0]*50+self.truppe_difesa[1]*35+self.truppe_difesa[2]*25+self.truppe_difesa[3]*10+self.truppe_difesa[4]*50+self.truppe_difesa[5]*105+self.truppe_difesa[6]*75+self.truppe_difesa[7]*10
        if (self.tribu_difesa == "Galli"):
            result = self.truppe_difesa[0]*50+self.truppe_difesa[1]*20+self.truppe_difesa[2]*10+self.truppe_difesa[3]*40+self.truppe_difesa[4]*55+self.truppe_difesa[5]*165+self.truppe_difesa[6]*105+self.truppe_difesa[7]*10
        if (self.tribu_difesa == "Teutoni"):
            result = self.truppe_difesa[0]*5+self.truppe_difesa[1]*60+self.truppe_difesa[2]*30+self.truppe_difesa[3]*5+self.truppe_difesa[4]*40+self.truppe_difesa[5]*75+self.truppe_difesa[6]*80+self.truppe_difesa[7]*10

        return result
    def get_perdite_prezzo(self):
        if (len(self.perdite) > 0):
            result = 250*self.perdite[0]+340*self.perdite[1]+490*self.perdite[2]+360*self.perdite[3]+1005*self.perdite[4]+1425*self.perdite[5]
        else:
            result = 0
        return result 

    def get_difese_totale(self):
        result = self.truppe_difesa[0]+self.truppe_difesa[1]+self.truppe_difesa[2]+self.truppe_difesa[3]+self.truppe_difesa[4]+self.truppe_difesa[5]+self.truppe_difesa[6]
        return result
    
    
    def get_carico_totale(self):
        result = 60*self.truppe_attacco[0]+40*self.truppe_attacco[1]+50*self.truppe_attacco[2]+110*self.truppe_attacco[4]+80*self.truppe_attacco[5]
        return result
    def get_bottino_totale(self):
        if (len(self.bottino) > 0):
            bottino_totale = self.bottino[0]+self.bottino[1]+self.bottino[2]+self.bottino[3]
            return bottino_totale
        else:
            return 0 
    def get_rentability(self):
        botin = self.get_bottino_totale()
        perdidas = self.get_perdite_prezzo()
        if (botin == 0):   
            if (perdidas == 0):
                rentabilidad = 0 
            else:
                rentabilidad = -100
        else:
            rentabilidad = round((botin - perdidas) * 100 / botin)
        return rentabilidad


    def get_efficiency(self):
        botin = self.get_bottino_totale()
        carry = self.get_carico_totale()
        if (carry == 0):   
            eficiencia = 0
        else:
            eficiencia  = round((carry - botin) * 100 / carry)
        return (100 - eficiencia)
    

    
    def dump(self):
        dumpresult = ""
        dumpresult =  "OGGETTO : " + self.oggetto 
        dumpresult +=  "\nDATA/ORA  : " + self.data 
        dumpresult +=  "\nATTACCANTE  : " + self.attaccante
        dumpresult +=  "\nTRUPPE_ATTACCO : " +  str(self.truppe_attacco)
        dumpresult +=  "\nPERDITE: " +  str(self.perdite)
        dumpresult +=  "\nBOTTINO  : " + str(self.bottino)
        dumpresult +=  "\nDIFENSORE  : " + str(self.difensore)
        dumpresult +=  "\nTRUPPE_DIFESA : " +  str(self.truppe_difesa)
        
        dumpresult +=  "\nPREZZO_PERDITE  : " + str(self.get_perdite_prezzo())
        dumpresult +=  "\nCARICO_TOTALE : " + str(self.get_carico_totale())
        dumpresult +=  "\nBOTTINO_TOTALE : " + str(self.get_bottino_totale())
        dumpresult +=  "\nRENTABILITY : " + str(self.get_rentability())
        dumpresult +=  "\nEFFICIENCY : " + str(self.get_efficiency())
        dumpresult +=  "\nTRIBU DIFESA: " + str(self.tribu_difesa)
        dumpresult +=  "\nDEF FANTERIA: " + str(self.get_def_fanteria())
        dumpresult +=  "\nDEF CAVALLERIA: " + str(self.get_def_cavalleria())
        
        return dumpresult
    
    def __repr__(self):
        dumpresult = ""
        dumpresult +=  "," + str(self.playerdef)
        dumpresult +=  "," + str(self.get_perdite_prezzo())
        dumpresult +=  "," + str(self.get_carico_totale())
        dumpresult +=  "," + str(self.get_bottino_totale())
        dumpresult +=  "," + str(self.get_rentability())
        dumpresult +=  "," + str(self.get_efficiency())
        dumpresult +=  "," + str(self.reporttime )
        dumpresult +=  "," + str(self.get_difese_totale())

        dumpresult +=  "," + str(self.tribu_difesa)
        dumpresult +=  "," + str(self.get_def_fanteria())
        dumpresult +=  "," + str(self.get_def_cavalleria())
        return dumpresult
        
    def dump_csv(self,url, identif):
        dumpresult = url
 #       dumpresult += self.data 
#        dumpresult +=  "," + self.attaccante
        dumpresult +=  "," + str(identif)

        dumpresult +=  "," + str(self.playerdef)
        dumpresult +=  "," + str(self.get_perdite_prezzo())
        dumpresult +=  "," + str(self.get_carico_totale())
        dumpresult +=  "," + str(self.get_bottino_totale())
        dumpresult +=  "," + str(self.get_rentability())
        dumpresult +=  "," + str(self.get_efficiency())
        dumpresult +=  "," + str(self.reporttime )
        dumpresult +=  "," + str(self.get_difese_totale())
        dumpresult +=  "," + str(self.tribu_difesa)
        dumpresult +=  "," + str(self.get_def_fanteria())
        dumpresult +=  "," + str(self.get_def_cavalleria())

        
        return dumpresult
    
class travianListaReport(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.berichteList = []
        
    def start_a(self, attrs):
        a_tag =[v for k, v in attrs if k=='href']    
        if (len(a_tag) > 0):
            current_tag = a_tag[0]
            if (current_tag.find("berichte.php?id") > -1):
                self.berichteList.append(current_tag)
                
    def get_berichte_list(self):
        return self.berichteList
        

        

class travianLeggiReport(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.oggetto=""
        self.data=""
        self.attaccante=""
        self.truppe_attacco=[]
        self.truppe_difesa=[]
        self.perdite = []
        self.bottino = []
        self.difensore = ""
        self.aspetta = ASPETTA_NIENTE
        self.intd = 0
        self.tribu_difesa = ""
    def start_td(self,attrs):
        self.intd = 1
        
    def start_img(self, attrs):
#        if (self.aspetta ==ASPETTA_TRUPPE_DIFESA):
        titles =[v for k, v in attrs if k=='title']
        if (len(titles) > 0):
            currenttitle = titles[0]
            if (string.upper(currenttitle) == string.upper(travian_language.legionario)):
                self.tribu_difesa = "Romani"
            if (string.upper(currenttitle) == string.upper(travian_language.cavalleria_difesa)):
                self.tribu_difesa = "Galli"
            if (string.upper(currenttitle) == string.upper(travian_language.combattente)):
                self.tribu_difesa = "Teutoni"
                
               
        
    def start_tr(self,attrs):
        if (self.aspetta ==ASPETTA_TRUPPE_DIFESA):
           
            self.aspetta = ASPETTA_FINITO

    def end_td(self):
        self.intd = 0
        
    def handle_data(self,text):
        
     
        if (self.aspetta != ASPETTA_FINITO):
            if (string.upper(travian_language.oggetto) == string.upper(text) ):
                self.aspetta = ASPETTA_OGGETTO
            elif (string.upper(travian_language.dataora) == string.upper(text) ):
                self.aspetta = ASPETTA_DATA
            elif (string.upper(travian_language.attaccante) == string.upper(text) ) and (self.aspetta == ASPETTA_DATA) :
                self.aspetta = ASPETTA_ATTACCANTE
            elif (string.upper(travian_language.truppe) == string.upper(text) and (self.aspetta == ASPETTA_ATTACCANTE) ):
                self.aspetta = ASPETTA_TRUPPE_ATTACCO
            elif (string.upper(travian_language.perdite) == string.upper(text) and (self.aspetta == ASPETTA_TRUPPE_ATTACCO) ):
                self.aspetta = ASPETTA_PERDITE
            elif (string.upper(travian_language.prigionieri) == string.upper(text) and (self.aspetta == ASPETTA_TRUPPE_ATTACCO) ):
                self.aspetta = ASPETTA_PRIGIONIERI
    
            elif ((string.upper(travian_language.bottino) == string.upper(text) or string.upper(travian_language.risorse) == string.upper(text) )and ((self.aspetta == ASPETTA_PERDITE ) or (self.aspetta == ASPETTA_PRIGIONIERI) or (self.aspetta == ASPETTA_INFORMAZIONI) )):
                self.aspetta = ASPETTA_BOTTINO
            elif (string.upper(travian_language.informazioni) == string.upper(text) and ((self.aspetta == ASPETTA_PERDITE ) or (self.aspetta == ASPETTA_PRIGIONIERI) )):
                self.aspetta = ASPETTA_INFORMAZIONI
            elif (string.upper(travian_language.difensore) == string.upper(text) and (self.aspetta in [ ASPETTA_BOTTINO, ASPETTA_INFORMAZIONI ]) ):
                
                self.aspetta = ASPETTA_DIFENSORE
            elif (string.upper(travian_language.truppe) == string.upper(text) and (self.aspetta in [ ASPETTA_DIFENSORE ]) ):
                
                self.aspetta = ASPETTA_TRUPPE_DIFESA

            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_OGGETTO) and (len(text) >0)):
                self.oggetto += text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_DATA) and (len(text) >0)):
                self.data += text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_ATTACCANTE) and (len(text) >0)):
                self.attaccante += text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_DIFENSORE) and (len(text) >0)):
                self.difensore += text
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_TRUPPE_ATTACCO) and (len(text) >0)):
                self.truppe_attacco.append(int(text))
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_PERDITE) and (len(text) >0)):
                if (len(self.perdite) <  len(self.truppe_attacco)):
                
                    self.perdite .append(int(text))
                    
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_BOTTINO) and (len(text) >0)):
                if (len(self.bottino) < 3):
                    if ('|' in text ):
                        self.bottino.append(int(text.rstrip(' ').rstrip('|')))
                elif (len(self.bottino) == 3):
                    self.bottino.append(int(text))
                        
            elif ((self.intd == 1) and (self.aspetta ==ASPETTA_TRUPPE_DIFESA) and (len(text) >0)):
                if (not("?" in text)): 
                    self.truppe_difesa.append(int(text))
                else:
                    self.truppe_difesa.append(1000)

    def get_report_int(self):
  
        
        rr = raid_report(self.oggetto, self.data, self.attaccante, self.truppe_attacco, self.perdite, self.bottino,self.difensore, self.truppe_difesa, self.tribu_difesa)
        return rr
     
    
def get_report(url):
    cookie_data=[]
    tlr= travianLeggiReport()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlr.feed(test_ca)
    return tlr.get_report_int()

def get_lista_report(url):
    cookie_data=[]
    tlr= travianListaReport()
    html_ca = travian_login.openurl(url)
 
    test_ca = html_ca.read()
   
    tlr.feed(test_ca)
    return tlr.get_berichte_list()


def get_lista_berichte(howmany,id, startindex = 0):
    lista_reports = []
    
    for i in range(startindex,howmany):
        
        url = "berichte.php?s="+str(i*10)+"&t=" +str(id)
        glr = get_lista_report(url )
        lista_reports.extend(glr)
    return lista_reports

def get_lista_all_report(howmany, startindex = 0):
    return get_lista_berichte(howmany,3,startindex)
        
def get_lista_all_spiate(howmany):
    return get_lista_berichte(howmany,4)
        
def get_reports(lista_report, lastseen):
    print lista_report
    #lista_report = travian_leggireport.get_lista_report('http://s9.travian.it/berichte.php?t=3')
    all_reports = []
    
    for report_url in lista_report:
        time.sleep(0.1)
        p = re.compile('(.*)\?id=([0-9]+)')
        m = p.match(report_url)
        identif= int(m.group(2))
        if (lastseen == identif):
            
            return all_reports
        try:
            report_raid = get_report(report_url)
            report_raid.identif = identif

            all_reports.append(report_raid)
        except:

            logging.debug( report_url +", Could not be parsed " )
    return all_reports
    
def get_all_reports(tadalist, lastseen, startindex = 0):
    lista_report = get_lista_all_report(tadalist,startindex)
    return get_reports(lista_report, lastseen)
    
def get_all_spiate(tadalist, lastseen):
    lista_spiate = get_lista_all_spiate(tadalist)
    return get_reports(lista_spiate, lastseen)

def print_all_reports(tadalist, lastseen, startindex = 0):    

    lista_report = get_lista_all_report(tadalist, startindex )
    #lista_report = travian_leggireport.get_lista_report('http://s9.travian.it/berichte.php?t=3')
    
    
    for report_url in lista_report:
        time.sleep(0.1)
        p = re.compile('(.*)\?id=([0-9]+)')
        m = p.match(report_url)
        identif= int(m.group(2))
        if (lastseen == identif):
            
            return
        
        report_raid = get_report(report_url)
        
        try:
            print report_raid.dump_csv(report_url, identif)
        except:

            logging.debug( report_url +", Could not be parsed " )
    

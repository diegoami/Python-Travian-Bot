#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
TravianBot 0.1 pre Alhpa 1

#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""
import sys,os
import travian_language
import logging

login_name=""
login_password=""
login_page=""
home_page=""
build_page_root=""
start_page=""
file_coda=""
build_page=""
file_language=""
building_page=""
barracks_page=""
stable_page=""
rally_page=""
build_page=""
sendtroops_page=""
raids_file=""
trappola_page=""
residence_page=""
risorse_page=""
mercato_page=""
magazzino_page=""
carta_page=""
xp_start=""
yp_start=""
raids_yesno=""
riepilogo_page=""
xfuga=""
yfuga=""
schiva_file=""
mer_coef=""
mail_page=""
municipio_page=""
fake_file=""
spedisci_page=""
accademia_page=""
villo_rinforzo=""
max_hours=2.0
raggio_raid=5
done_coeff=200
dist_coeff=40
intervallo_min=8
intervallo_max=11
day_refresh=2
methodo_raid=""
methodo_truppe=""
methodo_setup=""
attack_coeff=30
all_coeff=2
pop_coeff=8
min_pop=10
link_sub_list=5
coords_file=""
frequency=1
fabbro_page=""
armeria_page=""
raids_length=3
max_population=250
dbhost=""
dbuser=""
dbpasswd=""
db=""
nachrichten_page=""
build_frequency=1
troop_frequency=1

#schivadict

def getaccount(account_file):
    global login_name
    global login_password
    global login_page
    global home_page
    global build_page_root
    global start_page
    global file_coda
    global file_language
    global building_page
    global barracks_page
    global stable_page
    global rally_page
    global build_page
    global sendtroops_page
    global raids_file
    global trappola_page
    global residence_page
    global risorse_page
    global mercato_page
    global magazzino_page
    global carta_page
    global xp_start
    global yp_start
    global raids_yesno
    global riepilogo_page
    global xfuga
    global yfuga
    global schiva_file
    global mer_coef
    global mail_page
    global municipio_page
    global fake_file
    global spedisci_page
    global accademia_page
    global villo_rinforzo 
    global max_hours
    global raggio_raid
    global done_coeff
    global dist_coeff
    global intervallo_min
    global intervallo_max
    global day_refresh
    global methodo_raid
    global methodo_truppe
    global methodo_setup
    global attack_coeff
    global all_coeff
    global pop_coeff
    global min_pop
    global link_sub_list
    global coords_file
    global frequency
    global fabbro_page
    global armeria_page
    global raids_length
    global max_population
    global dbhost
    global dbuser
    global dbpasswd
    global db
    global nachrichten_page
    global build_frequency
    global troop_frequency
    
         
    account_array=[]
    
    try:
        file=open(account_file,'r')
    except:
        account_error(account_file)
    lista_variabili=file.readlines()
    if len(lista_variabili)<9:
        account_error(account_file)
#    if lista_variabili[0].split(" ")[0]!="login_name" and lista_variabili[1].split(" ")[0]!="login_password" and lista_variabili[2].split(" ")[0]!="login_page" and lista_variabili[3].split(" ")[0]!="home_page" and lista_variabili[4].split(" ")[0]!="build_page_root" and lista_variabili[5].split(" ")[0]!="start_page" and lista_variabili[6].split(" ")[0]!="queue_file" and lista_variabili[7].split(" ")[0]!="lenguage":
#        account_error(account_file)
#    else:
    for i in range(len(lista_variabili)):
        
    
        account_array.append(lista_variabili[i].split(" ")[1].strip())
    login_name=account_array[0]
    login_password=account_array[1]
    login_page=account_array[2]
    home_page=account_array[3]
    build_page_root=account_array[4]
    start_page=account_array[5]
    file_coda=account_array[6]
    file_language = os.path.join("lenguages",account_array[7])
    
    f=open(file_language,'r')

    array_lenguage=f.readlines()
    
    travian_language.setupresources(array_lenguage)
    building_page=account_array[8]
    barracks_page=account_array[9]
    stable_page=account_array[10]
    rally_page=account_array[11]
    build_page=account_array[12]
    sendtroops_page=account_array[13]
    raids_file=account_array[14]
    trappola_page=account_array[15]
    residence_page=account_array[16]
    risorse_page=account_array[17]
    mercato_page=account_array[18]
    magazzino_page=account_array[19]
    carta_page=account_array[20]
    xp_start=account_array[21]
    yp_start=account_array[22]
    raids_yesno=account_array[23]
    riepilogo_page=account_array[24]
    xfuga=account_array[25]
    yfuga=account_array[26]
    schiva_file=account_array[27]

    mer_coef=account_array[28]
    mail_page=account_array[29]
    municipio_page=account_array[30]
    fake_file=account_array[31]
    spedisci_page= account_array[32]
    accademia_page= account_array[33]
    villo_rinforzo = account_array[34]
    max_hours = float(account_array[35])
    raggio_raid = float(account_array[36])
    done_coeff = float(account_array[37])
    dist_coeff = float(account_array[38])
    intervallo_min = float(account_array[39])
    intervallo_max = float(account_array[40])
    day_refresh = float(account_array[41])
    methodo_raid = account_array[42]
    methodo_truppe = account_array[43]
    methodo_setup= account_array[44]
    attack_coeff = float(account_array[45])
    all_coeff = float(account_array[46])
    pop_coeff = float(account_array[47])
    min_pop = float(account_array[48])
    link_sub_list = int(account_array[49])
    coords_file = account_array[50]
    frequency = int(account_array[51])
    fabbro_page = account_array[52]
    armeria_page = account_array[53]
    raids_length = int(account_array[54])
    max_population = int(account_array[55])
    dbost = account_array[56]
    dbuser = account_array[57]
    dbpasswd = account_array[58]
    db = account_array[59]
    nachrichten_page = account_array[60]
    build_frequency = int(account_array[61])
    troop_frequency = int(account_array[62])
    
    
    logging.info( "Config read")
def account_error(account_file):
    logging.error("Account Error! Check your  file " + str(account_file))
    sys.exit()

    
def get_raids():
    file_raids = os.path.join("raids",raids_file)
    f=open(file_raids ,'r')
   
    array_raids=f.readlines()
    travian_raid.setupraids (array_raids)
    

    
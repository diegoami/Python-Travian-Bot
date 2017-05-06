#!/usr/bin/env python
import time,sys,os,random
sys.path.extend(["modules","modules/build","modules/common","modules/config","modules/edifici","modules/mail","modules/mapanalyze","modules/mercato","modules/militare","modules/raid","modules/riepilogo","../jspicklelib"])

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma
from travian_account import getaccount
from travian_login import login 

from travian_risorse import get_risorse
from travian_mercato import spediscimerce
from travian_caserma import get_attacchi, get_primo_attacco
import travian_mail



accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))
login()
travian_mail.leggi_note()
print travian_mail.note_interne
print travian_mail.lista_note
print travian_mail.get_string("BUILD_NEW")
print travian_mail.get_string("FESTA")
print travian_mail.get_string("ROBERTO")
print travian_mail.get_string("SCHIVA")
print travian_mail.get_string("MERDA")
print travian_mail.get_string("B2-CereaSegheria")









    
  
    
        
    
    
          
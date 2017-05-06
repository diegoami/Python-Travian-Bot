#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raid, travian_party
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids
from travian_risorse import get_risorse
from travian_mercato import spediscimerce
from travian_accademia import fai_ricerca



accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))



login()
dictvills =  travian_villaggi.getvillaggi()
travian_villaggi.vaiavillaggio(dictvills, "AF")

fai_ricerca()


    
  
    
        
    
    
          
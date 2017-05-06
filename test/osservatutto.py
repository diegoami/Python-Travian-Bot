#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_edifici, travian_villaggi, travian_addestra, travian_caserma, travian_raid
from travian_account import getaccount
from travian_login import login 
from travian_effettuaraids import effettua_raids
from travian_risorse import get_risorse
from travian_mercato import spediscimerce
from travian_caserma import get_attacchi, get_primo_attacco



accountfile = sys.argv[1]
getaccount(os.path.join("config",accountfile ))
login()
travian_addestra.spedisci_tutto(travian_account.xfuga,travian_account.yfuga)


    
  
    
        
    
    
          
#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_villaggi
import travian_addestra, travian_caserma
from travian_account import getaccount
from travian_login import login 

    
    

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))

login()
dictvills =  travian_villaggi.getvillaggi()


    

   
    
    
          
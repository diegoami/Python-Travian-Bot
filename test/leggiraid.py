#!/usr/bin/env python
import time,sys,os,random
sys.path.append("modules")
sys.path.append("libs")

import travian_account, travian_resdorf, travian_language, travian_func, travian_villaggi
import travian_addestra, travian_caserma, travian_raid
from travian_account import getaccount
from travian_login import login 

    
    

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))


login()
travian_addestra.addestracavalleria(t4Arg=1)
truppeact = travian_caserma.get_available_truppe()
possible_raids = travian_raid.get_possible_raids(truppeact)
if (len(possibile_raids) > 0):
    randraidIndex = random.randrange(len(possible_raids)/3-1)
    raid_to_try=  possible_raids[randraidIndex]
    travian_addestra.spediscitruppe(t4Arg=raid_to_try.truppe_necessarie(), xArg=str(raid_to_try.xp), yArg=str(raid_to_try.yp))


   
    
    
          
#!/usr/bin/env python
"""
TravianBot 0.1 pre Alhpa 1
#
# (C) Riotinfo 2006
#
# Distribute under the terms of the PSF license.
"""
import time,sys,os,random
#add modules subdir to path
sys.path.append("modules")
sys.path.append("libs")

#import modules
import travian_account, travian_func, travian_resdorf, travian_language,travian_edifici
from travian_account import getaccount
from travian_login import login 


print "Load account setting..."

accountfile = sys.argv[1]
print accountfile
getaccount(os.path.join("config",accountfile ))
print "Done!\nLogin..."

travian_language.printcrap()
login()

#links_edificabili = travian_resdorf.get_spazi_edificabili()
#primo_link_edif = links_edificabili[0].href
#print primo_link_edif
#print travian_edifici.get_link_edifici(primo_link_edif )

links_edifici= travian_resdorf.get_edifici()
print links_edifici
links_magazzino = travian_resdorf.get_link_edificio(travian_language.magazzino)
print links_magazzino
#travian_func.build_edificio(travian_language.granaio)
travian_func.upgrade_edificio(travian_language.centro_del_villaggio)


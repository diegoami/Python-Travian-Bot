from sgmllib import SGMLParser
import urllib2, urllib, time, travian_account, travian_info, travian_login, socket_travian
import travian_language, string
import logging


t99 = 0

class travian_trapper(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        
    def start_input(self, attrs):
        name = [v for k, v in attrs if k=='name']
        valore =[v for k, v in attrs if k=='value']
        tipo =[v for k, v in attrs if k=='type']
        cookie_format=[]
        cookie_format.append(name[0])
        if "t99" in name:
            valore[0]=str(t99)
     
        cookie_format.append(valore[0])
        temp_tuple=tuple(cookie_format)
        self.data.append(temp_tuple)
    def get_cookie(self,cookie):
        cookie.extend(self.data)
    
        
def costruiscitrappole(t99Arg=0):
    t99 = t99Arg
    cookie_data=[]
    tct = travian_trapper()
    html_tr = travian_login.openurl(travian_account.trappola_page)
    test_ct = html_tr.read()
   
    tct.feed(test_ct )
    tct.get_cookie(cookie_data)
    
    cookie_data = urllib.urlencode(cookie_data)
    result = socket_travian.travian_cookie(cookie_data, travian_account.trappola_page)
    
   

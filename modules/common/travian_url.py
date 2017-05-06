import urllib, urllib2, time, travian_account, travian_login, traceback
import logging

def openurl(urlarg, values = {}):
    print urlarg
    if (urlarg.find('http') > -1):
        url = urlarg
    else:
        url= travian_account.start_page+urlarg
    done = False
    while (not done):
        try:
            values = {}
            headers = { 'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
        
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data, headers)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request )
            done = True
            return response
        except:
            logging.exception(" Could not connect to "+string( url)+ ", retrying")

            time.sleep(1)

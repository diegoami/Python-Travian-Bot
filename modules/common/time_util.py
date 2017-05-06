import sys,time, random, string, datetime
import logging


def wait_until(targettime ):
    logging.debug("WAITING FOR TIME : "+str( targettime))

#    targettime = datetime.datetime(year,month,day,hour, min , sec )
    done = 0
    
    while (not done):
        if ( datetime.datetime.now() <targettime):
            difftime = datetime.datetime.now() - targettime
            diffseconds = difftime.seconds
            if (diffseconds % 5 == 0):
                logging.debug("NOW = "+str(  datetime.datetime.now()))
            time.sleep(.8)
        else:
            logging.debug("TARGET TIME REACHED ! "+str( targettime))
            done = 1
        


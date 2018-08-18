#!/usr/bin/python3

import os, time, logging, errno, sys, transferLabData
from subprocess import Popen

#Log file setting
logging.basicConfig(filename="WTSensors_Log.txt", level=logging.DEBUG)
logger = logging.getLogger()

while True:
    try:
        print("Starting...")
        time.sleep(3)
        logging.info("Starting")
        p = Popen("python " + transferLabData.py, shell=True)
        p.wait()
#        os.execv('transferLabData.py', ['None'])

    except KeyboardInterrupt:
        print("Stopping (User)")
        logging.info("Stopped by User")
        break
    
    except IOError as e:
        if e.errno == errno.EPIPE:
            logger.debug("IOERROR", exc_info=True)
            print("IO Error")
            continue
    
    except Exception:
            logger.debug("Other Error", exc_info=True)
            print("Stopping (Exception)")
            break
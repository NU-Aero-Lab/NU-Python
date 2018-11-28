#!/usr/bin/python3

import time, logging, errno, sys, transferLabData
from subprocess import Popen

#Get Logger
logger = logging.getLogger('executer')

while True:
    try:
        print("Executing transferLabData.py ...")
        time.sleep(1)
        logger.info("Starting (WTPYSensor2)")
        p = Popen("sudo python3.5 " + "transferLabData.py", shell=True)
        p.wait()

    except IOError as e:
        if e.errno == errno.EPIPE:
            logger.debug("IOError", exc_info=True)
            print("Executer: IO Error")
            continue
    
    except Exception:
            logger.debug("Other Error", exc_info=True)
            print("Executer: Exception! Check Log File")
            continue
    
    except KeyboardInterrupt:
        print("Stopping (User)(WTPYSensor2)")
        logger.info("Executer: Stopped by User")
        break
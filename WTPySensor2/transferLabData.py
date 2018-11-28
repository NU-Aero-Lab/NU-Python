import sys, logging, errno
#from rsc import RscDataHandler
from data_transfer import DataTransfer
from enviroHat import EnviroHatDataHandler
from hrtbt import HeartBeat
from tunnelLogger import setlogger

def main():
    #Get Logger
    logger = logging.getLogger('transferLabData')
    
    # Create the data handler, and transferer, then send data!
#    rscSensor = RscDataHandler(1)
    enviroSensor = EnviroHatDataHandler(1)
#    heart = HeartBeat(5)
    dataTrans = DataTransfer()
    while True:
            try:
#                if (not rscSensor.dataReady) and (not rscSensor.running):
#                    rscSensor.start()
#                elif rscSensor.dataReady:
#                    pres, temp = rscSensor.getData()
#                    dataTrans.sendData("MWTP",pres)
#                    dataTrans.sendData("MWTT",temp)
#                    dataTrans.sendData("SWTP",rscSensor.stdev())
#                    dataTrans.sendData("UWTP",rscSensor.max())
#                    dataTrans.sendData("LWTP",rscSensor.min())
#                    dataTrans.sendData("NWTP",rscSensor.size())
#
                if (not enviroSensor.dataReady) and (not enviroSensor.running):
                    enviroSensor.start()
                elif enviroSensor.dataReady:
                    pres, temp = enviroSensor.getData()
                    dataTrans.sendData("LAP2",pres)
                    dataTrans.sendData("LAT2",temp)
                        
#                if (not heart.dataReady) and (not heart.running):
#                        heart.start()
#                elif heart.dataReady:
#                        dataTrans.sendData("BET2", heart.beat())
            
            except TypeError:
                logger.debug("TypeError", exc_info = True) 
                continue

            except IOError as e:
                if e.errno == errno.EPIPE:
                    print("IO Error")
                    logger.debug("IOError", exc_info = True)
                    break
            
            except KeyboardInterrupt:
                print("Stopping (User)")
                logger.info("Stopped by User (KeyboardInterrupt")
                break

            except Exception:
                    logger.debug("Other Error", exc_info = True)
                    print("Stopping (Other Exception)")
                    break

if __name__ == '__main__':
    main()
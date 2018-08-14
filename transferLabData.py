import sys, logging
from rsc import RscDataHandler
from data_transfer import DataTransfer
from enviroHat import EnviroHatDataHandler
from hrtbt import HeartBeat

def main():
    #Log file setting
    logging.basicConfig(filename="WTSensors_Log.txt", level=logging.DEBUG)
    logger = logging.getLogger()
    # Create the data handler, and transferer, then send data!
    rscSensor = RscDataHandler(1)
    enviroSensor = EnviroHatDataHandler(1)
    heart = HeartBeat(5)
    dataTrans = DataTransfer()
    try:
            while True:
                if (not rscSensor.dataReady) and (not rscSensor.running):
                    rscSensor.start()
                elif rscSensor.dataReady:
                    pres, temp = rscSensor.getData()
                    dataTrans.sendData("MWTP",pres)
                    dataTrans.sendData("MWTT",temp)

                if (not enviroSensor.dataReady) and (not enviroSensor.running):
                    enviroSensor.start()
                elif enviroSensor.dataReady:
                    pres, temp = enviroSensor.getData()
                    dataTrans.sendData("LATP",pres)
                    dataTrans.sendData("LATT",temp)
                    
                if (not heart.dataReady) and (not heart.running):
                    heart.start()
                elif heart.dataReady:
                    dataTrans.sendData("BEAT", heart.beat())
    except Exception:
            logger.debug("Error from transferLabData", exc_info=True)
        
if __name__ == '__main__':
    main()

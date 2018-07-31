import sys
from rsc import RscDataHandler
from data_transfer import DataTransfer
from enviroHat import EnviroHatDataHandler
from hrtbt import HeartBeat

def main():

    # Create the data handler, and transferer, then send data!
    rscSensor = RscDataHandler(0.15)
    enviroSensor = EnviroHatDataHandler(1)
    dataTrans = DataTransfer()
    while True:
        if (not rscSensor.dataReady) and (not rscSensor.running):
            rscSensor.start()
        elif rscSensor.dataReady:
        #    print("Data ready, collected " + str(rscSensor.len()) + " samples")
            pres, temp = rscSensor.getData()
            dataTrans.sendData("MWTP",pres)
            dataTrans.sendData("MWTT",temp)

        if (not enviroSensor.dataReady) and (not enviroSensor.running):
            enviroSensor.start()
        elif enviroSensor.dataReady:
        #    print("Data ready, collected " + str(enviroSensor.len()) + " samples")
            pres, temp = enviroSensor.getData()
            dataTrans.sendData("LATP",pres)
            dataTrans.sendData("LATT",temp)

        
if __name__ == '__main__':
    main()

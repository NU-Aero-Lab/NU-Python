import logging, errno, time

class setlogger():

    #Root Logger
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)
    # log file handler
    fh = logging.FileHandler('LOG_WT_SENSORS.txt')
    # Format the log message
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    rootLogger.addHandler(fh)
    #Other Logger Setting (formats, etc. for future)
    loggerT = logging.getLogger('transferLabData')
    loggerE = logging.getLogger('executer')


import inspect
import logging


def customlogger(loglevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # Kõik logid salvestatakse eraldi faili:
    # filehandler = logging.FileHandler("{0}.log".format(loggername), mode='w')
    # Logid salvestatakse ühte faili
    filehandler = logging.FileHandler("automation.log", mode='a')
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger

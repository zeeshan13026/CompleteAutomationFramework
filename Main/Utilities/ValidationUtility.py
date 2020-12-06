#We are using print
#We want all print statement in one file(Log File)
#Assert need to used in test cases to Pass/Fail
#Get all print statements in html report
import datetime
import inspect
import logging
import os

log_file_path = None
logger= None
class ValidationUtility():

    def __init__(self, driver):
        self.driver = driver

    def getLogger(self):
        global log_file_path
        curr_time = datetime.datetime.now()
        curr = str(curr_time).replace("-", "_").replace(" ", "_").replace(":", "_")
        log_file = os.getcwd() + "/../Main/Logs/" + curr.split(".")[0] + "logfile.log"

        if log_file_path == None:
            log_file_path = log_file
        else:
            pass
            #Use previous file name

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def validateTestStep(self, condition, message):

        if condition:
            self.getLogger().info(message)
            assert True
        else:
            self.getLogger().error(message)
            assert False


import configparser
import os

class ReadConfiguration():

    # conf = None
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(os.getcwd() + "/../MainResources/Conf/Configuration.ini")

    def getApplicationUrl(self):

        return self.conf["BROWSER"]["url"]

    def getMaximizeBrowser(self):

        return self.conf["BROWSER"]["maximizeBrowser"]

    def getImplicitWait(self):

        return self.conf["BROWSER"]["implicitWait"]

    def getPath(self):
        return self.conf["PATH"]["test_data"]


import json
import os

from Main.DataProviders.ReadConfiguration import ReadConfiguration


class ReadLoginCredentials():
    def __init__(self):
        objReadConfiguration = ReadConfiguration()
        data = open(os.getcwd() + objReadConfiguration.getPath()+"LoginCredentials.json")
        self.json_data = json.load(data)

    def getUserName(self):

        return self.json_data["UserName"]

    def getPassword(self):

        return self.json_data["Password"]


class JavaScriptUtility():

    def __init__(self, driver):
        self.driver = driver

    def ScrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def ClickOnElement(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def GetTextBoxValue(self, element):
        return self.driver.execute_script("return arguments[0].value", element)

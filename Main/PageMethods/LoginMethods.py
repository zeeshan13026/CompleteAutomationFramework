from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Main.DataProviders.ReadLoginCredentials  import ReadLoginCredentials
from Main.PageObjects.LoginPage import LoginPage
from Main.Utilities.JavaScriptUtility import JavaScriptUtility
from Main.Utilities.ValidationUtility import ValidationUtility


class LoginMethods:
    objReadLoginCredencial = None
    objLoginpage = None

    def __init__(self, driver):
        self.driver = driver
        self.objReadLoginCredencial = ReadLoginCredentials()
        self.objLoginpage = LoginPage(self.driver)
        self.objValidationUtility = ValidationUtility(self.driver)
        self.objJavaScriptUtility = JavaScriptUtility(self.driver)


    def LoginToApplication(self):
        self.objLoginpage.getUserName().send_keys(self.objReadLoginCredencial.getUserName())
        #self.objValidationUtility.getLogger().info(self.objLoginpage.getUserNameTextBox().text)
        actual_value = self.objReadLoginCredencial.getUserName()
        expected_value = self.objJavaScriptUtility.GetTextBoxValue(self.objLoginpage.getUserNameTextBox())
        self.objValidationUtility.validateTestStep(actual_value == expected_value, "Value entered in username is:"+actual_value)


        self.objLoginpage.getPassword().send_keys(self.objReadLoginCredencial.getPassword())
        #self.objValidationUtility.getLogger().info(self.objLoginpage.getPassword().text)
        actual_value = self.objReadLoginCredencial.getPassword()
        expected_value = self.objJavaScriptUtility.GetTextBoxValue(self.objLoginpage.getPasswordTextBox())
        self.objValidationUtility.validateTestStep(actual_value == expected_value,"Value entered in Password is"+actual_value)


        self.objLoginpage.getLogin().click()
        self.objValidationUtility.validateTestStep(True,"User click on Login button")

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.objLoginpage.loggedUser))
        #self.objValidationUtility.getLogger().info("you are logged in with:" + self.objLoginpage.getLoggedUser().text)
        actual_value = self.objReadLoginCredencial.getUserName() # dd12
        expected_value = self.objLoginpage.getLoggedUser().text #user Name: dd12
        self.objValidationUtility.validateTestStep(actual_value == expected_value, "User is able to login")




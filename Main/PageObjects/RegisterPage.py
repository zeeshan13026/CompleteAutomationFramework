from selenium.webdriver.common.by import By
class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID, "firstname")
    lastname  = (By.ID, "lastname")
    username  = (By.ID, "userName")
    password  = (By.ID, "password")

    def getFirstName(self):
        return self.driver.find_element(*self.firstname)

    def getLastName(self):
        return self.driver.find_element(*self.lastname)

    def getUserName(self):
        return self.driver.find_element(*self.username)

    def getPassword(self):
        return self.driver.find_element(*self.password)
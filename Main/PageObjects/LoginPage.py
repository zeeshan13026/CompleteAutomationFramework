from selenium.webdriver.common.by import By


class LoginPage():

    # driver = None
    def __init__(self, driver):
        self.driver = driver

    userName = (By.ID, "userName")
    userNameTextBox = (By.XPATH, "//input[@type='text']")

    password = (By.ID, "password")
    passwordTextBox = (By.ID, "password")

    loginButton = (By.ID, "login")

    newUser = (By.ID, "newUser")
    loggedUser = (By.ID, "userName-value")

    def getUserName(self):
        return self.driver.find_element(*self.userName)

    def getUserNameTextBox(self):
        return self.driver.find_element(*self.userNameTextBox)

    def getPassword(self):
        return self.driver.find_element(*self.password)

    def getPasswordTextBox(self):
        return self.driver.find_element(*self.passwordTextBox)

    def getLogin(self):
        return self.driver.find_element(*self.loginButton)

    def getNewUser(self):
        return self.driver.find_element(*self.newUser)

    def getLoggedUser(self):
        return self.driver.find_element(*self.loggedUser)

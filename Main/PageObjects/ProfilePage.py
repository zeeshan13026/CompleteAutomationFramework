from selenium.webdriver.common.by import By


class ProfilePage():

    def __init__(self, driver):
        self.driver = driver

    gotostore       = (By.ID, "gotoStore")
    deleteaccount   = (By.XPATH, "//button[text()='Delete Account']")
    deleteallbooks  = (By.XPATH, "//button[text()='Delete All Books']")


    def getGoToStore(self):
        return self.driver.find_element(*self.gotostore)


    def getDeleteAccount(self):
        return self.driver.find_element(*self.deleteaccount)

    def getDeleteAllBooks(self):
        return self.driver.find_element(*self.deleteallbooks)
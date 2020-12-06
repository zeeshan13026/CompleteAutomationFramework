import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Main.BaseClass.BaseClass import BaseClass
from Main.DataProviders.ReadLoginCredentials import ReadLoginCredentials
from Main.PageMethods.LoginMethods import LoginMethods
from Main.PageObjects.LoginPage import LoginPage


class Testbookstore_login(BaseClass):

    @pytest.mark.browserValue("Chrome")
    def test_login(self):
        # objReadLoginCredential = ReadLoginCredentials()
        # objLoginPage = LoginPage(self.driver)
        # self.open_application()
        #
        # objLoginPage.getUserName().send_keys(objReadLoginCredential.getUserName())
        # # self.driver.find_element_by_id("userName").send_keys(objReadLoginCredential.getusername())
        # # objLoginPage.getUserName().send_keys(objReadLoginCredential.getUserName())
        #
        # value = objLoginPage.getUserNameTextBox()
        # print(value.text)
        #
        # objLoginPage.getPassword().send_keys(objReadLoginCredential.getPassword())
        # print(objLoginPage.getPasswordTextBox().text)
        #
        # objLoginPage.getLogin().click()
        # profile = self.driver.window_handles[0]
        # # profile = driver.find_element_by_xpath("//label[@id='userName-value']")
        # self.driver.switch_to.window(profile)
        #
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "userName-value")))
        # print("you are logged in with:" + self.driver.find_element_by_xpath("//label[@id='userName-value']").text)

        objLoginMethods = LoginMethods(self.driver)

        self.open_application()

        objLoginMethods.LoginToApplication()

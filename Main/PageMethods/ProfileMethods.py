import time

from Main.PageObjects.ProfilePage import ProfilePage
from Main.Utilities.ActionChainUtility import ActionChainUtility


class ProfileMethods():

    def __init__(self, driver):
        self.driver = driver
        self.objProfilePage = ProfilePage(self.driver)
        self.objActionChainUtility = ActionChainUtility(self.driver)


    def OpenProfilePage(self):
        self.objActionChainUtility.ScrollToElement(self.objProfilePage.getGoToAPI())

        self.objProfilePage.getProfilePage().click()

    def ClickGoToStore(self):
        self.objActionChainUtility.ScrollToElement(self.objProfilePage.getGoToAPI())

        self.objProfilePage.getGoToStore().click()

    def DeleteAllBooks(self):
        self.objActionChainUtility.ScrollToElement(self.objProfilePage.getGoToAPI())

        self.objProfilePage.getDeleteAllBooks().click()

        self.objProfilePage.getDeleteAllBooksPopUpOK().click()

        time.sleep(2)

        self.driver.switch_to.alert.accept()



from datetime import time

from Main.PageObjects.BooksPage import BooksPage
from Main.Utilities.ActionChainUtility import ActionChainUtility
from Main.Utilities.JavaScriptUtility import JavaScriptUtility
from Main.Utilities.ValidationUtility import ValidationUtility


class BooksMethods:

    def __init__(self, driver):
        self.driver = driver
        self.objBooksPage = BooksPage(self.driver)
        self.objJavaScriptUtility = JavaScriptUtility(self.driver)
        self.objActionChainUtility = ActionChainUtility(self.driver)
        self.objValidationUtility = ValidationUtility(self.driver)

    def searchBook(self, bookName):
        self.objBooksPage.getSearchBox().send_keys(bookName)
        expected_value = self.objJavaScriptUtility.GetTextBoxValue(self.objBooksPage.getSearchBox())
        self.objValidationUtility.validateTestStep(expected_value == bookName,
                                                   "Book is search in search box:" + bookName)

    def SelectGitPocketGuide(self):
        self.objBooksPage.getGitPocketGuide().click()
        time.sleep(2)
        print("book details are : ", self.objBooksPage.getBookDetails()[0].text)
        self.objValidationUtility.validateTestStep(True, "User clicked on GitPocketGuide book")

    def SelectWebAPIWithNet(self):
        self.objBooksPage.getWebAPIwithNet().click()
        time.sleep(2)
        print("book details are : ", self.objBooksPage.getBookDetails()[0].text)
        self.objValidationUtility.validateTestStep(True, "User clicked on WebAPIWithNet book")

    def ClickGoToBookStore(self):
        self.objActionChainUtility.ScrollToElement(self.objBooksPage.getBookStore())
        self.objBooksPage.getBackToBookStore().click()
        self.objValidationUtility.validateTestStep(True, "User click on Go To Store")

    def ClickAddToMyCollection(self):
        self.objActionChainUtility.ScrollToElement(self.objBooksPage.getBookStore())
        self.objBooksPage.getAddToMyCollection().click()

    def VerifyBookAdded(self):
        time.sleep(2)
        # Book added to your collection.
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def VerifyBookAlreadyPresent(self):
        time.sleep(2)
        # Book already present in the your collection!
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

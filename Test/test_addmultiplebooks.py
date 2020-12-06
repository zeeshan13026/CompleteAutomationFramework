import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Main.BaseClass.BaseClass import BaseClass
from Main.DataProviders.ReadLoginCredentials import ReadLoginCredentials
from Main.PageMethods.BooksMethods import BooksMethods
from Main.PageMethods.LoginMethods import LoginMethods
from Main.PageMethods.ProfileMethods import ProfileMethods


class Testbookstore_addmultiplebooks(BaseClass):

    @pytest.mark.browserValue("Chrome")
    def test_addmultiplebooks(self):
        objProfileMethods = ProfileMethods(self.driver)
        objBooksMethods = BooksMethods(self.driver)
        objLoginMethods = LoginMethods(self.driver)

        self.open_application()

        objLoginMethods.LoginToApplication()

        objProfileMethods.DeleteAllBooks()

        objProfileMethods.ClickGoToStore()

        objBooksMethods.SearchBook("Git Pocket Guide")

        objBooksMethods.SelectGitPocketGuide()

        objBooksMethods.ClickAddToMyCollection()

        objBooksMethods.VerifyBookAdded()

        objBooksMethods.ClickGoToBookStore()

        objBooksMethods.SearchBook("Designing Evolvable Web APIs with ASP.NET")

        objBooksMethods.SelectWebAPIWithNet()

        objBooksMethods.ClickAddToMyCollection()

        objBooksMethods.VerifyBookAdded()

        objProfileMethods.OpenProfilePage()

        list = []
        collection = self.driver.find_elements_by_xpath("//div[@class='col-12 mt-4 col-md-6']/div")
        for books in collection:
            if books.text not in list:
                list.append(books.text)
                print(str(list) + "Book has already been added")
        time.sleep(2)









#Entire below code shifted to PageMethod folder
        # self.open_application()
        # objReadLoginCredentials = ReadLoginCredentials()
        #
        # self.driver.find_element_by_id("userName").send_keys(objReadLoginCredentials.getUserName())
        # value = self.driver.find_element_by_xpath("//input[@type='text']")
        # print(value.text)
        #
        # self.driver.find_element_by_id("password").send_keys(objReadLoginCredentials.getPassword())
        # print(self.driver.find_element_by_id("password").text)
        #
        # self.driver.find_element_by_id("login").click()
        # profile = self.driver.window_handles[0]
        # #profile = driver.find_element_by_xpath("//label[@id='userName-value']")
        # self.driver.switch_to.window(profile)
        #
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID,"userName-value")))
        # print("you are logged in with:" + self.driver.find_element_by_xpath("//label[@id='userName-value']").text)
        #
        # store_button = self.driver.find_element_by_id("gotoStore")
        # time.sleep(2)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",store_button)
        # self.driver.find_element_by_id("gotoStore").click()
        #
        # book_store = self.driver.window_handles[0]
        # self.driver.switch_to.window(book_store)
        # time.sleep(2)
        # self.driver.find_element_by_id("searchBox").send_keys("Git Pocket Guide")
        # time.sleep(2)
        # #book= driver.find_element_by_id("see-book-Git Pocket Guide")
        # #WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.ID, "book")))
        # self.driver.find_element_by_id("see-book-Git Pocket Guide").click()
        # child_window = self.driver.window_handles[0]
        # self.driver.switch_to.window(child_window)
        # content = self.driver.find_elements_by_xpath("//div[@class='profile-wrapper']/div")
        # for element in content:
        #     if element.text == "9781449325862":
        #         print(element.text + "following book id has been added")
        #         break
        # add_to_your_collection = self.driver.find_element_by_xpath("//div[@class='text-left fullButton']/following-sibling :: div/button")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_your_collection)
        # time.sleep(2)
        # self.driver.execute_script("arguments[0].click();",add_to_your_collection)
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        #
        # self.driver.find_element_by_xpath("//div[@class='text-left fullButton']/button").click()
        # book_store = self.driver.window_handles[0]
        # self.driver.switch_to.window(book_store)
        # time.sleep(2)
        #
        # self.driver.find_element_by_id("searchBox").send_keys("Designing Evolvable Web APIs with ASP.NET")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//span[@id='see-book-Designing Evolvable Web APIs with ASP.NET']/a").click()
        # book_store = self.driver.window_handles[0]
        # self.driver.switch_to.window(book_store)
        # content = self.driver.find_elements_by_xpath("//div[@class='profile-wrapper']/div")
        # for element1 in content:
        #     if element1.text == "9781449337711":
        #         print(element1.text + "following book id has been added")
        #         break
        # add_to_your_collection = self.driver.find_element_by_xpath("//div[@class='text-left fullButton']/following-sibling :: div/button")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_your_collection)
        # time.sleep(2)
        # self.driver.execute_script("arguments[0].click();",add_to_your_collection)
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        # time.sleep(2)
        #
        # self.driver.find_element_by_xpath("//span[text()='Profile']").click()
        # list = []
        # collection = self.driver.find_elements_by_xpath("//div[@class='col-12 mt-4 col-md-6']/div")
        # for books in collection:
        #     if books.text not in list:
        #         list.append(books.text)
        #         print(str(list) + "Book has already been added")
        # time.sleep(2)
        # self.driver.quit()

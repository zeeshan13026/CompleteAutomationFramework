import pytest

from Main.BaseClass.BaseClass import BaseClass


class Testbookstore_signup(BaseClass):

    @pytest.mark.browserValue("Chrome")
    def test_signup(self):
        self.open_application()
        self.driver.find_element_by_id("newUser").click()
        self.driver.switch_to.active_element

        self.driver.find_element_by_id("firstname").send_keys("naveen")
        print(self.driver.find_element_by_id("firstname").text)
        self.driver.find_element_by_id("lastname").send_keys("guwalani")
        print(self.driver.find_element_by_id("lastname").text)
        self.driver.find_element_by_id("userName").send_keys("niks12")
        print(self.driver.find_element_by_id("userName").text)
        self.driver.find_element_by_id("password").send_keys("Navtika@20")

        self.driver.quit()

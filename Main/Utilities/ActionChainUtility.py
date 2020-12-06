from selenium.webdriver import ActionChains


class ActionChainUtility():

    def __init__(self, driver):
        self.driver =driver

    def ScrollToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
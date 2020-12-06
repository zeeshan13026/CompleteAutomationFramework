from selenium.webdriver.common.by import By


class BooksPage():

    def __init__(self,driver):
        self.driver = driver


    searchbox = (By.ID, "searchBox")
    gitpocketguide = (By.ID, "see-book-Git Pocket Guide")


    def getSearchBox(self):
        return self.driver.find_element(*self.searchbox)

    def getGitPocketGuide(self):
        return self.driver.find_element(*self.gitpocketguide)

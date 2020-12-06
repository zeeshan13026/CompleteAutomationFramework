import pytest

#It is an abstract class
from Main.DataProviders.ReadConfiguration import ReadConfiguration


@pytest.mark.usefixtures("baseDriver")
class BaseClass():
# A virtual driver has been created here
     def open_application(self):
#         self.driver.maximize_window()
#         self.driver.get("https://demoqa.com/login")
#         self.driver.implicitly_wait(5)

#Reading all this from configuration file
        objReadConfiguration = ReadConfiguration()
        if objReadConfiguration.getMaximizeBrowser() == "True":
            self.driver.maximize_window()
        self.driver.get(objReadConfiguration.getApplicationUrl())
        self.driver.implicitly_wait(objReadConfiguration.getImplicitWait())

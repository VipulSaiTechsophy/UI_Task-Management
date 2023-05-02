import time

from Base.ActionsPage import ActionPage
from Utilities.configReader import readConfig
from selenium.webdriver.common.by import By


class loginPage(ActionPage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    userName_Id = "username"
    password_Id = "password"
    login_id = "kc-login"

    profile_Xpath = "//header/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/button[1]/div[1]/*[1]"
    logOut_Xpath = "//body/div[@id='basic-menu']/div[3]/ul[1]/li[1]"

    teamTasks_Xpath = "//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h5[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]"
    my_Tasks_XPath = "//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h5[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]"


    def loginTask(self):
        self.log.info("*******__Login to Task Management__********")
        self.log.info("__Enter UserName__")

        self.sendKeys(self.userName_Id, "ID", readConfig("login credentials", "username"))
        self.log.info("__Enter Password__")

        self.log.info("__Click on Login__")
        self.sendKeys(self.password_Id, "ID", readConfig("login credentials", "password"))

        self.click(self.login_id, "ID")

        exp_title = self.getPageName()
        Actual_title = "Task Management"

        if Actual_title == exp_title:
            assert True
            self.log.info("__Login successfull__")
        else:
            self.log.info("__login Failed__")
            assert False



    def log_in_out_Task_Management(self, taskType):
        if taskType == "login":
            self.loginTask()
        elif taskType == "loginout":
            self.loginTask()
            self.click(self.profile_Xpath, "XPATH")
            time.sleep(2)
            self.click(self.logOut_Xpath, "XPATH")
            self.log.info("__Logged Out__")
            time.sleep(3)
            self.close_driver()
        elif taskType == "logout":
            self.click(self.profile_Xpath, "XPATH")
            time.sleep(2)
            self.click(self.logOut_Xpath, "XPATH")
            self.log.info("__Logged Out__")
            time.sleep(3)
            self.close_driver()

        else:
            self.log.info("invalid option has been provided for the parameter")
















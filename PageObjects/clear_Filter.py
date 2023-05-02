import time
from Base.ActionsPage import ActionPage
from selenium.common.exceptions import InvalidSessionIdException
from Utilities.configReader import readConfig
import string
import random

class clearfilter_myTask(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    value = "1"


    click_filter_xpath = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[3]/button[1]"

    click_column_xpath = "//div[@id='filtering-select']"
    taskId = "//*[@id='menu-']/div[3]/ul/li[1]"
    taskName = "//*[@id='menu-']/div[3]/ul/li[2]"
    assigne = "//*[@id='menu-']/div[3]/ul/li[3]"
    priority = "//*[@id='menu-']/div[3]/ul/li[4]"
    dueData = "//*[@id='menu-']/div[3]/ul/li[5]"
    status = "//*[@id='menu-']/div[3]/ul/li[6]"
    reference = "//*[@id='menu-']/div[3]/ul/li[7]"
    subTasks = "//*[@id='menu-']/div[3]/ul/li[8]"
    Filter_value = "filtering-value"
    clickOnFilter =  "//button[@id='filteringBtn-TM']"
    clickOnClear_XPATH = "//body/div[@id='simple-popover']/div[3]/div[2]/button[1]"


    def clear_Filter(self):
        time.sleep(1)
        self.click(self.click_filter_xpath, "XPATH")
        self.log.info("****__Clicking on Filter in My Tasks page__****")
        self.click(self.click_column_xpath, "XPATH")
        self.log.info("***__Click on column dropdown**")
        self.click(self.taskId, "XPATH")
        self.log.info("**__select_column**")
        self.sendKeys(self.Filter_value, "ID", self.value)
        self.log.info("Enter Value as "+self.value)
        time.sleep(1)
        self.click(self.clickOnFilter, "XPATH")
        time.sleep(1)
        self.click(self.clickOnClear_XPATH, "XPATH")
        self.log.info("clicked on clear")
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)


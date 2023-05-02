import time
from Base.ActionsPage import ActionPage
from Utilities.configReader import readConfig
import string
import random

class filter_myTask(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_Value = "1"
    task_Value = "a"
    assignee_Value = "bhavya"
    priority_Value = "low"


    click_filter_xpath = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[3]/button[1]"

    click_column_xpath = "//div[@id='filtering-select']"
    taskId = "//*[@id='menu-']/div[3]/ul/li[1]"
    taskName = "//*[@id='menu-']/div[3]/ul/li[2]"
    assigne = "//*[@id='menu-']/div[3]/ul/li[3]"
    priority = "//*[@id='menu-']/div[3]/ul/li[5]"
    dueData = "//*[@id='menu-']/div[3]/ul/li[4]"
    status = "//*[@id='menu-']/div[3]/ul/li[6]"
    reference = "//*[@id='menu-']/div[3]/ul/li[7]"
    subTasks = "//*[@id='menu-']/div[3]/ul/li[8]"
    Filter_value = "//input[@id='filtering-value']"
    assigne_filter_dropdown = "//input[@id='assignee']"
    clickonFilter = "//button[@id='filteringBtn-TM']"
    clickOnClear_XPATH = "//body/div[@id='simple-popover']/div[3]/div[2]/button[1]"
    close_filter = "//body/div[@id='simple-popover']/div[3]/div[1]/button[1]/*[1]"

    # id = "//body/div[@id='menu-']/div[3]/ul[1]/li[1]"
    # taskname = "//body/div[@id='menu-']/div[3]/ul[1]/li[2]"
    # Assignee = "//body/div[@id='menu-']/div[3]/ul[1]/li[3]"
    # prioriiey = "//body/div[@id='menu-']/div[3]/ul[1]/li[5]"

    def filters(self):
        # self.click(self.click_filter_xpath, "XPATH")
        # self.log.info("****__Clicking on Filter in My Tasks page__****")
        # self.click(self.click_column_xpath, "XPATH")
        # self.log.info("***__Click on column dropdown**")
        # self.click(self.taskId, "XPATH")
        # self.log.info("**__select_column**")
        # self.clear_textfield(self.Filter_value,"XPATH")
        # time.sleep(0.5)
        # self.sendKeys(self.Filter_value, "XPATH", self.id_Value)
        # self.log.info("**Enter Value**")
        # self.click(self.clickonFilter, "XPATH")
        # self.log.info("****Click 0n Filter****")
        # # self.click(self.close_filter, "XPATH")
        # time.sleep(5)
        # self.click(self.close_filter, "XPATH")
        # time.sleep(1)
        #
        # self.click(self.click_filter_xpath, "XPATH")
        # self.log.info("****__Clicking on Filter in My Tasks page__****")
        # self.click(self.click_column_xpath, "XPATH")
        # self.log.info("***__Click on column dropdown**")
        # self.click(self.taskName, "XPATH")
        # self.log.info("**__select_column**")
        # self.clear_textfield(self.Filter_value,"XPATH")
        # time.sleep(0.5)
        # self.sendKeys(self.Filter_value, "XPATH", self.task_Value)
        # self.log.info("**Enter Value**")
        # self.click(self.clickonFilter, "XPATH")
        # self.log.info("****Click 0n Filter****")
        # # self.click(self.close_filter, "XPATH")
        # time.sleep(5)
        # self.click(self.close_filter, "XPATH")
        # time.sleep(1)

        self.click(self.click_filter_xpath, "XPATH")
        self.log.info("****__Clicking on Filter in My Tasks page__****")
        self.click(self.click_column_xpath, "XPATH")
        self.log.info("***__Click on column dropdown**")
        self.click(self.assigne, "XPATH")
        self.log.info("**__select_column**")
        time.sleep(0.5)
        self.filteruseactionswithsendkeys(self.assigne_filter_dropdown, self.assignee_Value, "XPATH")
        self.log.info("**Enter Value**")
        self.click(self.clickonFilter, "XPATH")
        self.log.info("****Click 0n Filter****")
        # self.click(self.close_filter, "XPATH")
        time.sleep(5)
        self.click(self.close_filter, "XPATH")
        time.sleep(1)

        self.click(self.click_filter_xpath, "XPATH")
        self.log.info("****__Clicking on Filter in My Tasks page__****")
        self.click(self.click_column_xpath, "XPATH")
        self.log.info("***__Click on column dropdown**")
        self.click(self.priority, "XPATH")
        self.log.info("**__select_column**")
        time.sleep(0.5)
        self.sendKeys(self.Filter_value, "XPATH", self.priority_Value)
        self.log.info("**Enter Value**")
        self.click(self.clickonFilter, "XPATH")
        self.log.info("****Click 0n Filter****")
        # self.click(self.close_filter, "XPATH")
        time.sleep(5)
        self.click(self.close_filter, "XPATH")
        time.sleep(1)
    #
    # def clear_Filter(self):
    #     self.click(self.click_filter_xpath, "XPATH")
    #     self.log.info("****__Clicking on Filter in My Tasks page__****")
    #     self.click(self.click_column_xpath, "XPATH")
    #     self.log.info("***__Click on column dropdown**")
    #     self.click(self.taskId, "XPATH")
    #     self.log.info("**__select_column**")
    #     self.sendKeys(self.Filter_value, "ID", self.value)
    #     self.log.info("**Enter Value**")
    #     self.click(self.clickOnClear_XPATH, "XPATH")

import time
from Base.ActionsPage import ActionPage
from Utilities.configReader import readConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException


import string
import random

class createTask_mytask(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Random_Name = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for x in range(10))
    Random_DESC = ''.join(random.choice(string.ascii_lowercase) for x in range(50))
    Random_Num =  ''.join(random.choice(string.digits) for x in range(10))




    clickOnCreateTask_XPath = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[3]/button[2]"
    add_Task_Name_XPATH = "//input[@id='Task-Name']"
    name = 'Santosh'
    # To Validate the uploaded file
    file_text_XPATH = "/html/body/div[2]/div[3]/div/form/div[1]/div[2]/div/div[9]/div/div[1]"
    exp_text = "LKW0022111113BC57FCF.pdf"
    file_path = 'LKW0022111113BC57FCF.pdf'

    add_Description_XPATH = "//textarea[@id='Description-ID']"
    #Assignee
    assignee_Dropdown = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]"
    assignetxtfield = "//input[@id='assignee']"
    assigne_name = "Sai Vips"
    # Responsible
    responsible_Drpdown = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    responsible_textfield = "//input[@id='Responsible']"
    responsibe_name = "bhavya bhavya"
    priority_Drpdwn = "//div[@id='priority']"
    progress_Drpdwn = "//div[@id='progress']"
    startdate_ID = "start-Date"
    enddateID = "//input[@id='end-Date']"
    Edate = "//*[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng']"
    followup_ID = "//input[@id='follow-up']"
    estimated_ID = "estimated-time"
    # note_ID = "note-ID"
    # upload_click_xpath = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[8]/div[1]/label[1]"
    create_task_XPATH = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    close_createtask_XPATH = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/*[1]"

    ele_list_xpath = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]"
    Task_success_msg_XPATH = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]"
    exp_taskmsg = "Task created successfully"

    button = "//tbody/tr[1]/td[1]/button[1]/*[1]"

    def my_Tasks(self):
        time.sleep(1)
        self.click(self.clickOnCreateTask_XPath, "XPATH")
        self.log.info("Clicked On Create Task")
        time.sleep(3)
        self.sendKeys(self.add_Task_Name_XPATH, "XPATH", self.Random_Name)
        self.log.info("Added task name")
        time.sleep(2)
        self.sendKeys(self.add_Description_XPATH, "XPATH", self.Random_DESC)
        self.log.info("Added description")
        time.sleep(2)

        # #  To find the list of elements
        # # self.click(self.assignee_Dropdown, "XPATH")
        # # self.listofdrpdwn(self.ele_list_xpath, "XPATH")
        # # time.sleep(10)
        #

        self.useactionswithsendkeys(self.assignee_Dropdown,self.assignetxtfield, self.assigne_name, "XPATH")
        self.log.info("Assignee selected")
        time.sleep(2)
        # self.useactionswithsendkeys(self.responsible_Drpdown,self.responsible_textfield,self.responsibe_name, "XPATH")

        # self.useactions(self.priority_Drpdwn, "XPATH")
        # time.sleep(2)
        # self.useactions(self.responsible_Drpdown, "XPATH")
        # time.sleep(2)
        # self.useactions(self.progress_Drpdwn, "XPATH")
        # time.sleep(2)

        # #
        # self.sendKeys(self.startdate_ID, "ID", "0110199980125")
        # self.click(self.enddateID, "ID")
        # self.exec_scr("SCRIPT",self.enddateID, "2023-03-29")
        # self.click(self.Edate, "XPATH")
        # End Date
        # self.click(self.Edate, "XPATH")
        # element = self.driver.find_element(By.XPATH, self.enddateID)
        # self.driver.execute_script("arguments[0].removeAttribute('type')", element)
        # new_element = self.driver.find_element(By.XPATH, self.enddateID)
        # self.driver.execute_script("arguments[0].setAttribute('value','22/03/2023, 12:30')", new_element)
        # time.sleep(3)
        # FollowUpDate
        # self.sendKeys(self.followup_ID, "ID", "101220291121")
        # element = self.driver.find_element(By.XPATH, self.followup_ID)
        # self.driver.execute_script("arguments[0].removeAttribute('type')", element)
        # new_element = self.driver.find_element(By.XPATH, self.followup_ID)
        # self.driver.execute_script("arguments[0].setAttribute('value','22/03/2023, 12:30')", new_element)
        # time.sleep(3)
        # #
        time.sleep(1)
        self.sendKeys(self.estimated_ID, "ID", 24)
        self.log.info("Estimate added")
        time.sleep(1)
        # try:
        self.click(self.create_task_XPATH, "XPATH")
        # except Exception as e:
        #     print(e)
        self.log.info("Clicked on Create Task")
        # tt = self.driver.find_element(By.XPATH, "MuiAlert-message css-1xsto0d")
        # mes1 = tt.text
        # print(mes1)
        # MES = str(mes1)
        # ex_mes = "Task created successfully"
        # if MES == ex_mes:
        #     assert True
        # else:
        #     assert False
        # time.sleep(9)
        # self.click(self.close_createtask_XPATH, "XPATH")
        # self.get_Text(self.Task_success_msg_XPATH, "XPATH", self.exp_taskmsg)

        # element = self.driver.find_element(By.XPATH, self.Task_success_msg_XPATH)
        # gettext = element.text
        # print(gettext)
        # print(self.Random_Name)
        # if gettext == self.Random_Name:
        #     print("Task created")
        #     assert True
        # else:
        #     print("Failed to create Task")
        #     assert False










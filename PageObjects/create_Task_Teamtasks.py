import time
from Base.ActionsPage import ActionPage
from Utilities.configReader import readConfig
import string
import random

class createTask_Teamtask(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Random_Name = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for x in range(10))
    Random_DESC = ''.join(random.choice(string.ascii_lowercase) for x in range(50))
    Random_Num =  ''.join(random.choice(string.digits) for x in range(2))

    # To Validate the uploaded file
    file_text_XPATH = "/html/body/div[2]/div[3]/div/form/div[1]/div[2]/div/div[9]/div/div[1]"
    exp_text = "LKW0022111113BC57FCF.pdf"
    file_path = 'LKW0022111113BC57FCF.pdf'


    click_on_Teamtasks = "//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h5[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]"

    click_on_createTask_XPath = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]"

    add_Task_Name_XPATH = "//input[@id='Task-Name']"
    name = 'Santosh'
    add_Description_XPATH = "//textarea[@id='Description-ID']"
    #Assignee
    assignee_Dropdown = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]"
    assigne_textfield = "//input[@id='assignee']"
    assigne_name = "Sai Vips"
    #Responsible
    responsible_Drpdown = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    responsible_textfield = "//input[@id='Responsible']"
    responsible_name = "bhavya bhavya"
    priority_Drpdwn = "//div[@id='priority']"
    progress_Drpdwn = "//div[@id='progress']"
    startdate_ID = "start-Date"
    enddateID = "end-Date"
    followup_ID = "follow-up"
    estimated_ID = "estimated-time"
    note_ID = "note-ID"
    upload_click_xpath = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[8]/div[1]/label[1]/div[1]/span[1]"
    create_task_XPATH = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    close_create_task = "//body/div[2]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/*[1]"



    def team_Tasks(self):
        time.sleep(1)
        self.click(self.click_on_Teamtasks, "XPATH")
        self.log.info("Clicked on Team task")
        time.sleep(1)
        self.click(self.click_on_createTask_XPath, "XPATH")
        self.log.info("Clicked on create task")
        time.sleep(2)
        # self.click(self.add_Task_Name_ID, "XPATH")
        self.sendKeys(self.add_Task_Name_XPATH, "XPATH", self.Random_Name)
        self.log.info("Added task name")
        time.sleep(2)
        self.sendKeys(self.add_Description_XPATH, "XPATH", self.Random_DESC)
        self.log.info("Added description")
        time.sleep(2)
        self.useactionswithsendkeys(self.assignee_Dropdown, self.assigne_textfield, self.assigne_name, "XPATH")
        self.log.info("Added assignee")
        time.sleep(2)
        # self.useactionswithsendkeys(self.responsible_Drpdown, self.responsible_textfield, self.responsible_name, 'XPATH')
        # time.sleep(2)
        # self.useactions(self.priority_Drpdwn, "XPATH")
        # time.sleep(2)
        # self.useactions(self.responsible_Drpdown, "XPATH")
        # time.sleep(2)
        # self.useactions(self.progress_Drpdwn, "XPATH")
        # time.sleep(2)

        # self.sendKeys(self.startdate_ID, "ID", "0110199980125")
        # time.sleep(0.5)
        # self.sendKeys(self.enddateID, "ID", "1012202911212")
        # time.sleep(0.5)
        # self.sendKeys(self.followup_ID, "ID", "3111201111512")
        # time.sleep(0.5)

        self.sendKeys(self.estimated_ID, "ID", 48)
        self.log.info("Added estimate")
        # self.sendKeys(self.note_ID, "ID", self.Random_DESC)
        # time.sleep(2)

        # self.uploadfile(self.upload_click_xpath, "XPATH", self.file_path)
        # self.log.info("Clicked on upload file")
        # time.sleep(10)
        # self.get_Text(self.file_text_XPATH, "XPATH", self.exp_text)

        # try:
        self.click(self.create_task_XPATH, "XPATH")
        # except Exception as e:
        #     print(e)
        # time.sleep(1)
        # self.click(self.close_create_task, "XPATH")


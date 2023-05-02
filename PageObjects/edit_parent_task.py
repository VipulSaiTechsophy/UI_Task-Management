import time
import random
import string
from Base.ActionsPage import ActionPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Edit_parent_task(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver =  driver

    Random_Name = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for x in range(10))
    Random_DESC = ''.join(random.choice(string.ascii_lowercase) for x in range(50))
    Random_Num =  ''.join(random.choice(string.digits) for x in range(10))

    assigne_value = "Bhavya"

    #     Details
    task_id_XPATH = "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-1332tfs']"
    # Relations
    arrow_button = "//tbody/tr[1]/td[1]/button[1]/*[1]"
    relations_clmn_ID = "simple-tab-2"
    add_Existing_parent_XPATH = "//*[@id='simple-tabpanel-2']/div/p/div/div/button[1]"
    addExistingParent_Drpdwn_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    addExistingparent_textfield_XPATH = "//input[@id='parentTasks']"
    clickYesTo_AddexistingPar_Xpath = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    clickNoTo_AddexistingPar_Xpath = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    add_New_child_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/button[2]"
    add_Existing_Child_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/button[3]"
    add_Existing_Child_Drpdwn_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    add_Existingchild_Textfield = "//input[@id='childTasks']"
    clickYesToAddExistingChild_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    clickNoToAddExistingChild_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[2]/*[1]"

    msg_addexistingpar_succ_XPATH = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[4]/div[1]/div[2]"
    exp_msg_addexistingpar_succ = "Task updated successfully"

    msg_addexispar_fai_XPATH = "//div[contains(text(),'This parent task already has a child task')]"
    exp_msg_addexis_fail = "This parent task already has a child task"

    # To ADd new child
    add_Task_Name_XPATH = "//input[@id='Task-Name']"
    name = 'Santosh'
    add_Description_XPATH = "//textarea[@id='Description-ID']"
    # Assignee
    assignee_Dropdown   = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    assignee_textfield = "//input[@id='assignee']"
    assignee_name = "Sai Vips"

    estimated_ID = "estimated-time"
    create_task_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"

    # Close EDit Task
    close_EditTask_XPATH = "//body/div[2]/div[3]/div[1]/div[2]/button[1]"




    # def clickOndetails(self):
    #     self.click(self.task_id_XPATH, "XPATH")
    #     self.log.info("__Clicked on TaskId to edit task__")


    def clickOnRelations(self):
        # self.click(self.arrow_button, "XPATH")
        # self.log.info("Clicked on arrow button")
        try:
            arr_button = self.driver.find_element(By.XPATH, self.arrow_button)
            if arr_button.is_displayed():
                print("The Task is already a parent task")
                self.click(self.task_id_XPATH, "XPATH")
                self.log.info("Clicked on task id")
                self.click(self.relations_clmn_ID, "ID")
                self.log.info("Clicked on relations")
                time.sleep(2)
                self.click(self.add_Existing_parent_XPATH, "XPATH")
                self.log.info("Clicked on Add existing parent")
                time.sleep(1)
                self.chkenabled(self.addExistingParent_Drpdwn_XPATH, "XPATH")
                self.log.info("Check add existing parent is enabled or not")
                time.sleep(0.5)
                self.click(self.addExistingparent_textfield_XPATH, "XPATH")
                self.log.info("clicked on add existing parent")
                self.useactions(self.addExistingParent_Drpdwn_XPATH, "XPATH")
                self.log.info("selected add existing parent dropdown")
                time.sleep(1)
                self.log.info("Selected Parent")
                self.click(self.clickYesTo_AddexistingPar_Xpath, "XPATH")
                self.log.info("Save to Add parent")
                time.sleep(0.5)
                self.click(self.clickNoTo_AddexistingPar_Xpath, "XPATH")
                # self.log.info("Cancel to Add Parent")

                # ADD NEW CHILD
                self.click(self.add_New_child_XPATH, "XPATH")
                self.log.info("Add New Child")
                time.sleep(2)
                self.sendKeys(self.add_Task_Name_XPATH, "XPATH", self.Random_Name)
                self.log.info("Add Task Name")
                time.sleep(2)
                self.sendKeys(self.add_Description_XPATH, "XPATH", self.Random_DESC)
                self.log.info("Add Task Description")
                time.sleep(2)

                self.useactionswithsendkeys(self.assignee_Dropdown, self.assignee_textfield, self.assignee_name,
                                            "XPATH")
                time.sleep(2)
                self.log.info("select Assignee")
                # self.useactions(self.priority_Drpdwn, "XPATH")
                # time.sleep(2)
                # self.log.info("Select Priority")
                # self.useactionswithsendkeys(self.responsible_Drpdown, self.responsible_textfield, self.responsible_name,
                #                             "XPATH")
                # time.sleep(2)
                # self.log.info("Select responsible")
                # self.useactions(self.status_Drpdwn, "XPATH")
                # time.sleep(2)
                # self.log.info("select status")

                # self.sendKeys(self.startdate_ID, "ID", "0110199980125")
                # self.sendKeys(self.enddateID, "ID", "1012202911212")
                # self.sendKeys(self.followup_ID, "ID", "1211201111512")

                self.sendKeys(self.estimated_ID, "ID", 40)
                # self.sendKeys(self.note_ID, "ID", self.Random_DESC)
                time.sleep(2)
                # self.uploadfile(self.upload_click_xpath, "XPATH", self.file_path)
                # self.log.info("Clicked on upload file")
                # time.sleep(10)
                # self.get_Text(self.file_text_XPATH, "XPATH", self.exp_text)
                # time.sleep(2)
                # try:
                self.click(self.create_task_XPATH, "XPATH")
                # except Exception as e:
                #     print(e)
                # time.sleep(1)
                self.log.info("Clicked on Create Task")
                # self.click(self.close_createtask_XPATH, "XPATH")

                #     ADD EXISTING CHILD
                self.click(self.task_id_XPATH, "XPATH")
                self.log.info("Clicked on task id")
                self.click(self.relations_clmn_ID, "ID")
                self.log.info("Clicked on relations")
                time.sleep(2)
                self.click(self.add_Existing_Child_XPATH, "XPATH")
                self.log.info(" Add existing child")
                time.sleep(2)
                self.chkenabled(self.add_Existing_Child_Drpdwn_XPATH, "XPATH")
                self.click(self.add_Existingchild_Textfield, "XPATH")
                self.useactions(self.add_Existingchild_Textfield, "XPATH")
                self.log.info("Added existing child")
                time.sleep(1)
                self.click(self.clickYesToAddExistingChild_XPATH, "XPATH")
                self.log.info("Save Existing child")
                time.sleep(1)
                # self.click(self.clickNoToAddExistingChild_XPATH, "XPATH")
                # self.log.info("Cancel Existing child")
                time.sleep(1)
                # self.click(self.close_EditTask_XPATH, "XPATH")
                # self.log.info("Clicked on close edit task")
            else:
                print("This is Individual task")
        except NoSuchElementException as e:
            print(e)
            pass



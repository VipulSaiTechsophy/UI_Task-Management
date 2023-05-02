import time
import random
import string
from Base.ActionsPage import ActionPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class edit_task(ActionPage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver =  driver

    Random_Name = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for x in range(10))
    Random_DESC = ''.join(random.choice(string.ascii_lowercase) for x in range(50))
    Random_Num =  ''.join(random.choice(string.digits) for x in range(10))

    assigne_value = "Akhil"

    # Details
    task_id_XPATH = "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-1332tfs']"
    edit_Task_btn_XPATH = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[7]/button[1]"
    assigne_drpdwn = "//input[@id='assignee']"
    # Details
    assigne_dropdown = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    referrance_XPATH = "//input[@id='referrance']"
    editTask_btn = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[8]/button[1]"
    note_ID  =  "note-ID"
    send_note_XPATH = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[10]/div[1]/div[1]/div[1]/button[1]/*[1]"

    # UPDATE TASK
    Task_Name_Id = "Task-Name"
    Desc_ID = "Description-ID"
    Assignee_Drpdwn = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    Responsible_Drpdwn = "//div[@id='responsible']"
    start_Date_ID = "start-Date"
    End_Date_ID = "end-Date"
    Priority_XPATH = "//div[@id='priority']"
    Progress_XPath = "//div[@id='progress']"
    estimated_time_SKeys_ID = "estimated-time"
    follow_up_ID = "follow-up"
    update_btn_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    close_updatetask_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/*[1]"

    # Add Documents in Document column
    document_column_ID = "simple-tab-1"
    add_Doc_btn__XPATH = "//body/div[2]/div[3]/div[2]/div[3]/div[1]/p[1]/div[1]/div[1]/button[1]"
    click_on_upload = "//body/div[2]/div[3]/div[2]/div[3]/div[1]/p[1]/div[1]/div[1]/label[1]/div[1]/span[1]"
    file_text_AddDoc = "//*[@id='simple-tabpanel-1']/div/p/div/div[2]/div/div[1]"

    # Relations
    arrow_button ="//tbody/tr[1]/td[1]/button[1]/*[1]"
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

    # History
    history_column_ID = "simple-tab-3"
    close_EditTask_XPATH = "//body/div[2]/div[3]/div[1]/div[2]/button[1]"

    # To Create Task in Add New child in Relations
    add_Task_Name_XPATH = "//input[@id='Task-Name']"
    name = 'Santosh'
    add_Description_XPATH = "//textarea[@id='Description-ID']"
        #Assignee
    assignee_Dropdown   = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    assignee_textfield = "//input[@id='assignee']"
    assignee_name = "Sai Vips"
    #     responsible
    responsible_Drpdown = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    responsible_textfield = "//input[@id='Responsible']"
    responsible_name = "bhavya bhavya"
    priority_Drpdwn = "//div[@id='priority']"
    status_Drpdwn = "//div[@id='progress']"
    startdate_ID = "start-Date"
    enddateID = "end-Date"
    followup_ID = "follow-up"
    estimated_ID = "estimated-time"
    upload_click_xpath = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[8]/div[1]/label[1]/div[1]/span[1]"
    create_task_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    close_createtask_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/*[1]"

    # To Validate the uploaded file
    file_text_XPATH = "/html/body/div[3]/div[3]/div/form/div[1]/div[2]/div/div[9]/div/div[1]"
    exp_text = "LKW0022111113BC57FCF.pdf"
    file_path = "LKW0022111113BC57FCF.pdf"

    def clickOndetails(self):
        self.click(self.task_id_XPATH, "XPATH")
        self.log.info("__Clicked on TaskId to edit task__")
    def details(self):
        # self.useactions(self.assigne_dropdown, "XPATH")
        self.click(self.referrance_XPATH, "XPATH")
        self.log.info("clicked on reference")
        self.useactions(self.referrance_XPATH, "XPATH")
        self.log.info("selected reference")
        time.sleep(1)
        self.sendKeys(self.note_ID, "ID", self.Random_DESC)
        self.log.info("Add Note")
        time.sleep(0.5)
        self.click(self.send_note_XPATH, "XPATH")
        self.log.info("click on send note")
        time.sleep(1)

        # UPDATE TASK
        self.click(self.editTask_btn, "XPATH")
        self.log.info("Clicked on edit task")
        # time.sleep(1)
        # self.sendKeys(self.Task_Name_Id, "ID", self.Random_Name)
        # self.sendKeys(self.Desc_ID, "ID", self.Random_DESC)
        # self.useactions(self.Assignee_Drpdwn, "XPATH")
        # self.useactions(self.Responsible_Drpdwn, "XPATH")
        # self.sendKeys(self.End_Date_ID, "ID", "1012202911212")
        # self.useactions(self.Priority_XPATH, "XPATH")
        # self.useactions(self.Progress_XPath, "XPATH")
        # self.sendKeys(self.estimated_time_SKeys_ID, "ID", "24")
        # self.sendKeys(self.follow_up_ID, "ID", "1012202911212")
        self.click(self.update_btn_XPATH, "XPATH")
        self.log.info("Updated task")
        time.sleep(2)
        # self.click(self.close_updatetask_XPATH, "XPATH")


    def clickOnDocuments(self):
        time.sleep(2)
        self.click(self.document_column_ID, "ID")
        self.log.info("clicked on documents column")
        time.sleep(2)
        self.click(self.add_Doc_btn__XPATH, "XPATH")
        self.log.info("click on add document")
        time.sleep(2)
        # self.uploadfile(self.click_on_upload, "XPATH", self.file_path)
        time.sleep(5)
        self.log.info("Clicked on Upload documents")
        self.get_Text(self.file_text_AddDoc, "XPATH", self.exp_text)
        time.sleep(2)


    def clickOnRelations(self):
        try:
            arr_button = self.driver.find_element(By.XPATH, self.arrow_button)
            if arr_button.is_displayed():
                print("The Task is already a parent task")
                self.click(self.task_id_XPATH, "XPATH")
                self.log.info("Clicked on task ID")
                self.click(self.relations_clmn_ID, "ID")
                self.log.info("Clicked on relations")
                time.sleep(2)
                self.click(self.add_Existing_parent_XPATH, "XPATH")
                self.log.info("Clicked on add existing parent")
                time.sleep(1)
                self.chkenabled(self.addExistingParent_Drpdwn_XPATH, "XPATH")
                self.log.info("Checked add existing parent is enabled")
                time.sleep(0.5)
                self.click(self.addExistingparent_textfield_XPATH, "XPATH")
                self.log.info("Clicked on add existing parent")
                self.useactions(self.addExistingParent_Drpdwn_XPATH, "XPATH")
                self.log.info("add existing parent dropdown is selected")
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
                self.log.info("Clicked on create task")
                # except Exception as e:
                #     print(e)
                # time.sleep(1)
                self.log.info("Clicked on Create Task")
                # self.click(self.close_createtask_XPATH, "XPATH")

                #     ADD EXISTING CHILD

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
                self.click(self.close_EditTask_XPATH, "XPATH")
                self.log.info("Clicked on edit task")
            else:
                print("This is Individual task")
        except NoSuchElementException as e:
            print(e)
            pass
        # ADD Existing parent
        self.click(self.task_id_XPATH, "XPATH")
        self.log.info("Clicked on task id")
        self.click(self.relations_clmn_ID, "ID")
        self.log.info("Clicked on relations")
        time.sleep(2)
        self.click(self.add_Existing_parent_XPATH, "XPATH")
        self.log.info("Clicked on add existing parent")
        time.sleep(1)
        self.chkenabled(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        self.log.info("Checked add existing parent is enabled or not")
        time.sleep(0.5)
        self.click(self.addExistingparent_textfield_XPATH, "XPATH")
        self.log.info("Clicked on add existing parent")
        self.useactions(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        self.log.info("Selected add existing parent dropdown")
        time.sleep(1)
        self.log.info("Selected Parent")
        self.click(self.clickYesTo_AddexistingPar_Xpath, "XPATH")
        self.log.info("Save to Add parent")
        time.sleep(0.5)


    def add_Existing_Parent(self):
        self.click(self.add_Existing_parent_XPATH, "XPATH")
        time.sleep(1)
        self.chkenabled(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        time.sleep(0.5)
        self.click(self.addExistingparent_textfield_XPATH, "XPATH")
        self.useactions(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        time.sleep(1)
        self.log.info("Selected Parent")
        self.click(self.clickYesTo_AddexistingPar_Xpath, "XPATH")
        self.log.info("Save to Add parent")
        time.sleep(0.5)

        if self.get_Text(self.msg_addexistingpar_succ_XPATH, "XPATH", self.exp_msg_addexistingpar_succ):
            print("Added existing parent")
            # self.driver.refresh()
            self.click(self.close_EditTask_XPATH,"XPATH")
            # # self.log("Add existing parent succesfull")
            # time.sleep(1)
            assert None

        else:
            self.get_Text(self.msg_addexispar_fai_XPATH,"XPATH", self.exp_msg_addexis_fail)
            print("Failed to Add existing parent")
            # self.get_textValue(self.msg_addexispar_fai_XPATH,"XPATH") == self.exp_msg_addexis_fail
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

            self.useactionswithsendkeys(self.assignee_Dropdown,self.assignee_textfield, self.assignee_name, "XPATH")
            time.sleep(2)
            self.log.info("select Assignee")
            # self.useactions(self.priority_Drpdwn, "XPATH")
            # time.sleep(2)
            # self.log.info("Select Priority")
            self.useactionswithsendkeys(self.responsible_Drpdown,self.responsible_textfield, self.responsible_name, "XPATH")
            time.sleep(2)
            self.log.info("Select responsible")
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

    def clickOnHistory(self):
        self.click(self.history_column_ID, "ID")
        time.sleep(1)
    def close_EditTask(self):
        self.click(self.close_EditTask_XPATH , "XPATH")





import time
import random
import string
from Base.ActionsPage import ActionPage

class edit_subTask(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver =  driver


    Random_Name = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for x in range(10))
    Random_DESC = ''.join(random.choice(string.ascii_lowercase) for x in range(50))
    Random_Num =  ''.join(random.choice(string.digits) for x in range(10))

    click_subtask_downarrow_XPATH = "//*[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-1j7qk7u']"
    subtask_click_XPATH = "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium css-nkqn03']"

    # Details
    # assigne_dropdown = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    referrance_textfield = "//input[@id='referrance']"
    Referrance_dropdown = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[7]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    editTask_btn = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[8]/button[1]"
    note_ID  =  "note-ID"
    snd_note_XPATH = "//body/div[2]/div[3]/div[2]/div[2]/div[1]/p[1]/div[1]/div[10]/div[1]/div[1]/div[1]/button[1]/*[1]"

# UPDATE TASK
    Task_Name_Id = "Task-Name"
    Desc_ID = "Description-ID"
    Assignee_Drpdwn = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    Assignee_txtfld = "//input[@id='assignee']"
    Assignee_Value = "bhavya bhavya"

    Responsible_Drpdwn = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]"
    Resonsible_txtfld = "//input[@id='Responsible']"
    Responsible_Value = "bhavya"

    start_Date_ID = "start-Date"
    End_Date_ID = "end-Date"
    Priority_XPATH = "//div[@id='priority']"
    Progress_XPath = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/div[1]"
    estimated_time_SKeys_ID = "estimated-time"
    followup_ID = "follow-up"
    update_btn_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    close_updatetask_XPATH = "//body/div[3]/div[3]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]/*[1]"

    # DOCUMENTS
    document_column_ID = "simple-tab-1"
    add_Doc_btn__XPATH = "//body/div[2]/div[3]/div[2]/div[3]/div[1]/p[1]/div[1]/div[1]/button[1]"
    click_on_upload = "//body/div[2]/div[3]/div[2]/div[3]/div[1]/p[1]/div[1]/div[1]/label[1]/div[1]/span[1]"
    file_text_AddDoc = "/html/body/div[2]/div[3]/div[2]/div[3]/div/p/div/div[2]/div/div[1]"
    exp_text = "LKW0022111113BC57FCF.pdf"
    file_path = "LKW0022111113BC57FCF.pdf"

    # RELATIONS
    relations_clmn_ID = "simple-tab-2"
    add_Existing_parent_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/button[1]"
    add_Existingparent_txtfld_XPATH = "//input[@id='parentTasks']"
    addExistingParent_Drpdwn_XPATH = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    clickYesTo_AddexistingPar_Xpath = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[1]/*[1]"
    clickNoTo_AddexistingPar_Xpath = "//body/div[2]/div[3]/div[2]/div[4]/div[1]/p[1]/div[1]/div[1]/div[1]/button[2]/*[1]"

    # HISTORY
    history_column_ID = "simple-tab-3"
    # CLOSE EDIT TASK
    close_EditTask_XPATH = "//body/div[2]/div[3]/div[1]/div[2]/button[1]/*[1]"


    def editSubTask(self):
        self.click(self.click_subtask_downarrow_XPATH, "XPATH")
        self.log.info("Clicked on task having subtask")
        self.click(self.subtask_click_XPATH, "XPATH")
        self.log.info(" Clicked on subtask")
        time.sleep(1)
    def details(self):
        # self.useactions(self.assigne_dropdown, "XPATH")
        self.click(self.referrance_textfield, "XPATH")
        self.log.info("Click on reference")
        self.useactions(self.Referrance_dropdown, "XPATH")
        self.log.info("Added reference")
        time.sleep(1)
        self.sendKeys(self.note_ID, "ID", self.Random_DESC)
        self.log.info("Added note in text field")
        time.sleep(0.5)
        self.click(self.snd_note_XPATH, "XPATH")
        self.log.info("sent note in text field")
        time.sleep(1)

        # UPDATE TASK
        self.click(self.editTask_btn, "XPATH")
        self.log.info("Click on edit or update task")
        time.sleep(1)
        self.sendKeys(self.Task_Name_Id, "ID", self.Random_Name)
        self.log.info("Added Task name")
        self.sendKeys(self.Desc_ID, "ID", self.Random_DESC)
        self.log.info("Added Description")
        # self.useactionswithsendkeys(self.Assignee_txtfld,self.Assignee_txtfld, self.Assignee_Value, "XPATH")
        # # self.useactions(self.Assignee_Drpdwn, "XPATH")
        # self.log.info("Added assignee")
        # self.useactionswithsendkeys(self.Resonsible_txtfld, self.Resonsible_txtfld, self.Responsible_Value, "XPATH")
        # # self.useactions(self.Responsible_Drpdwn, "XPATH")
        # self.log.info("Added responsible")
        # self.sendKeys(self.End_Date_ID, "ID", "1012202911212")
        # self.log.info("Added End Date")
        # self.useactions(self.Priority_XPATH, "XPATH")
        # self.log.info("Added priority")
        # self.useactions(self.Progress_XPath, "XPATH")
        # self.log.info("Added status")
        # self.sendKeys(self.estimated_time_SKeys_ID, "ID", "8")
        # self.log.info("Added Estimate time")
        # self.sendKeys(self.followup_ID, "ID", "1012202911212")
        # self.log.info("Added follow up ID")
        self.click(self.update_btn_XPATH, "XPATH")
        self.log.info("updated button")
        # self.click(self.close_updatetask_XPATH, "XPATH")
        # self.log.info("Closed update task")




    def clickOnDocuments(self):
        time.sleep(2)
        self.click(self.document_column_ID, "ID")
        self.log.info("Clicked on Documents section")
        time.sleep(2)
        self.click(self.add_Doc_btn__XPATH, "XPATH")
        self.log.info("Clicked on Add Documents")
        time.sleep(2)
        self.uploadfile(self.click_on_upload, "XPATH", self.file_path)
        time.sleep(5)
        self.log.info("Clicked on Upload documents")
        self.get_Text(self.file_text_AddDoc, "XPATH", self.exp_text)
        self.log.info("validated document name")
        time.sleep(2)

    def clickOnRelations(self):
        self.click(self.relations_clmn_ID, "ID")
        self.log.info("Clicked on Relations")
        time.sleep(2)

    def add_Existing_Parent(self):
        self.click(self.add_Existing_parent_XPATH, "XPATH")
        self.log.info("Clicked on Add existing parent")
        time.sleep(2)
        self.chkenabled(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        self.log.info("Dropdown button is enabled")
        time.sleep(2)
        self.click(self.add_Existingparent_txtfld_XPATH ,"XPATH")
        self.log.info("Clicked on Add existing parent")
        self.useactions(self.addExistingParent_Drpdwn_XPATH, "XPATH")
        time.sleep(2)
        self.log.info("Selected Parent")
        self.click(self.clickYesTo_AddexistingPar_Xpath, "XPATH")
        self.log.info("Save to Add parent")
        time.sleep(1)

        # self.click(self.clickNoTo_AddexistingPar_Xpath, "XPATH")
        # self.log.info("Cancel to Add Parent")

    def clickOnHistory(self):
        try:
            self.click(self.click_subtask_downarrow_XPATH, "XPATH")
            self.log.info("Clicked on task having subtask")
            self.click(self.subtask_click_XPATH, "XPATH")
            self.log.info(" Clicked on subtask")
        except Exception :
            pass
        self.click(self.history_column_ID, "ID")
        self.log.info("Clicked on History")
        time.sleep(1)
    def close_EditTask(self):
        self.click(self.close_EditTask_XPATH , "XPATH")
        self.log.info("Closed Edit Task")
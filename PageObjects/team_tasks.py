import time
import random
import string
from Base.ActionsPage import ActionPage

class TeamTasks(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =  driver

    team_task_XPATH = "//header/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h5[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[2]"
    card_name_XPATH = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]"

    overdue_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]"
    overdue_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    exit_overdue_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    new_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]"
    new_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]"
    exit_new_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    onHold_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]"
    onHold_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/button[1]"
    exit_onHold_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    inProgress_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]"
    inProgress_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/button[1]"
    exit_inProgress_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    completed_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]"
    completed_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/button[1]"
    exit_completed_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    responsible_btn_XPATH = "//button[@id='simple-tab-1']"
    card_name_r_XPATH = "/html[1]/body[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]"

    r_overdue_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]"
    r_overdue_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/button[1]"
    r_exit_overdue_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    r_new_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]"
    r_new_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/button[1]"
    r_exit_new_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    r_onHold_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]"
    r_onHold_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/button[1]"
    r_exit_onHold_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    r_inProgress_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]"
    r_inProgress_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/button[1]"
    r_exit_inProgress_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"

    r_completed_name_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]"
    r_completed_btn_XPATH = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[4]/button[1]"
    r_exit_completed_XPATH ="//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/button[1]/*[1]"




    def clickOnTeamTasks(self):
        self.click(self.team_task_XPATH, "XPATH")
        time.sleep(1)
    def owned(self):
        self.get_textValue(self.card_name_XPATH, "XPATH")

        self.get_textValue(self.overdue_name_XPATH, "XPATH")
        self.click(self.overdue_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.exit_overdue_XPATH, "XPATH")

        self.get_textValue(self.new_name_XPATH, "XPATH")
        self.click(self.new_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.exit_new_XPATH, "XPATH")

        self.get_textValue(self.onHold_name_XPATH, "XPATH")
        self.click(self.onHold_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.exit_onHold_XPATH, "XPATH")

        self.get_textValue(self.inProgress_name_XPATH, "XPATH")
        self.click(self.inProgress_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.exit_inProgress_XPATH, "XPATH")

        self.get_textValue(self.completed_name_XPATH, "XPATH")
        self.click(self.completed_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.exit_completed_XPATH, "XPATH")

        time.sleep(3)

    def responsible(self):
        self.click(self.responsible_btn_XPATH, "XPATH")
        time.sleep(1)

        self.get_textValue(self.r_overdue_name_XPATH, "XPATH")
        self.click(self.r_overdue_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.r_exit_overdue_XPATH, "XPATH")

        self.get_textValue(self.r_new_name_XPATH, "XPATH")
        self.click(self.r_new_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.r_exit_new_XPATH, "XPATH")

        self.get_textValue(self.r_onHold_name_XPATH, "XPATH")
        self.click(self.r_onHold_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.r_exit_onHold_XPATH, "XPATH")

        self.get_textValue(self.r_inProgress_name_XPATH, "XPATH")
        self.click(self.r_inProgress_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.r_exit_inProgress_btn_XPATH, "XPATH")

        self.get_textValue(self.r_completed_name_XPATH, "XPATH")
        self.click(self.r_completed_btn_XPATH, "XPATH")
        time.sleep(2)
        self.click(self.r_exit_completed_XPATH, "XPATH")







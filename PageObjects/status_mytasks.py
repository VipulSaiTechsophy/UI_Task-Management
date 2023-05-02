import time

from Base.ActionsPage import ActionPage

class StatusMyTasks(ActionPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver =  driver

    overdue_button = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[2]"
    new_button = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[3]"
    onHold_button = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[4]"
    inprogress_button = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[5]"
    Completed_button ="//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[6]"
    total_button = "//body/div[@id='root']/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"

    def status(self):
        # Overdue
        self.click(self.overdue_button, "XPATH")
        self.log.info("Clicked on Overdue")
        time.sleep(2)
        self.click(self.total_button, "XPATH")
        self.log.info("Clicked on Total")
        time.sleep(1)

        # New
        self.click(self.new_button, "XPATH")
        self.log.info("Clicked on new")
        time.sleep(2)
        self.click(self.total_button, "XPATH")
        self.log.info("Clicked on Total")
        time.sleep(1)

        # OnHold
        self.click(self.onHold_button, "XPATH")
        self.log.info("Clicked on onHold")
        time.sleep(2)
        self.click(self.total_button, "XPATH")
        self.log.info("Clicked on Total")
        time.sleep(1)

        # InProgress
        self.click(self.inprogress_button, "XPATH")
        self.log.info("Clicked on InProgress")
        time.sleep(2)
        self.click(self.total_button, "XPATH")
        self.log.info("Clicked on Total")
        time.sleep(1)

        # Completed
        self.click(self.Completed_button, "XPATH")
        self.log.info("Clicked on Overdue")
        time.sleep(2)
        self.click(self.total_button, "XPATH")
        self.log.info("Clicked on Total")
        time.sleep(3)







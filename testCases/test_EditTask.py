import unittest
import pytest
from parameterized import parameterized
from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from PageObjects.edit_task_myTask import edit_task

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class EditTask(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.et = edit_task(self.driver)

    @pytest.mark.regression
    @pytest.mark.order(6)
    def test_EditTask(self):
        self.lp.log_in_out_Task_Management("login")
        self.et.clickOndetails()
        self.et.details()
        # self.et.clickOnDocuments()
        self.et.clickOnHistory()
        self.et.close_EditTask()
        self.et.clickOnRelations()
        # self.et.add_Existing_Parent()
        # self.et.add_New_Child()
        # self.et.add_Existing_Child()
        # self.et.clickOnHistory()
        # self.et.close_EditTask()
import unittest
import pytest
from parameterized import parameterized
from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from PageObjects.edit_sub_Task import edit_subTask


@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class EditSubTask(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.est = edit_subTask(self.driver)

    @pytest.mark.regression
    @pytest.mark.order(8)
    def test_EditSubTask(self):
        num_iter = 1
        self.lp.log_in_out_Task_Management("login")
        for i in range(num_iter):
            self.est.editSubTask()
            self.est.details()
            # self.est.clickOnDocuments()
            self.est.clickOnRelations()
            self.est.add_Existing_Parent()
            self.est.clickOnHistory()
            self.est.close_EditTask()

import unittest
import pytest
from parameterized import parameterized
from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from PageObjects.edit_parent_task import Edit_parent_task


@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class EditParentTask(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.ept = Edit_parent_task(self.driver)


    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_editParentTask(self):
        self.lp.log_in_out_Task_Management("login")
        self.ept.clickOnRelations()

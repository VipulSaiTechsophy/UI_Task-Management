import unittest
import pytest
from parameterized import parameterized
from PageObjects.loginPage import loginPage
# from PageObjects.create_Task_my_tasks import createTask_mytask
from PageObjects.create_Task_Teamtasks import createTask_Teamtask

from Utilities.configReader import readConfig

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class CreateTask_teamtask(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        # self.cMT = createTask_mytask(self.driver)
        self.cTT = createTask_Teamtask(self.driver)

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.order(3)
    def test_CreateTaskTeamTask(self):

        self.lp.log_in_out_Task_Management("login")
        # self.cMT.my_Tasks()
        self.cTT.team_Tasks()
        # self.lp.log_in_out_Task_Management("logout")



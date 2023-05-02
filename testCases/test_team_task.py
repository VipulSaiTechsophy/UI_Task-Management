import unittest
import pytest
from PageObjects.loginPage import loginPage
from PageObjects.team_tasks import TeamTasks



@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class Teamtask(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.tt = TeamTasks(self.driver)

    @pytest.mark.regression
    @pytest.mark.order(10)
    def test_teamTask(self):
        self.lp.log_in_out_Task_Management("login")
        self.tt.clickOnTeamTasks()
        self.tt.owned()
        self.tt.responsible()

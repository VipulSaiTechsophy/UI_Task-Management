import unittest
import pytest
from PageObjects.loginPage import loginPage
from PageObjects.status_mytasks import StatusMyTasks

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class TaskStatus(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.sm = StatusMyTasks(self.driver)

    @pytest.mark.regression
    @pytest.mark.order(9)
    def test_statusMytasks(self):
        self.lp.log_in_out_Task_Management("login")
        self.sm.status()
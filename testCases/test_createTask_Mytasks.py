import unittest
import pytest
from parameterized import parameterized
from PageObjects.loginPage import loginPage
from PageObjects.create_Task_my_tasks import createTask_mytask

from Utilities.configReader import readConfig

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class createTaskTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.ct = createTask_mytask(self.driver)

    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_CreateTask(self):

        self.lp.log_in_out_Task_Management("login")
        self.ct.my_Tasks()
        # self.ct.buttons()
        # self.lp.log_in_out_Task_Management("logout")



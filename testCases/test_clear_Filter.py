import unittest
import pytest
from parameterized import parameterized

from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from PageObjects.clear_Filter import clearfilter_myTask

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class ClearFilter(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.c = clearfilter_myTask(self.driver)
    @pytest.mark.regression
    @pytest.mark.order(5)
    def test_clear(self):
        self.lp.log_in_out_Task_Management("login")
        self.c.clear_Filter()
        # self.lp.log_in_out_Task_Management("logout")




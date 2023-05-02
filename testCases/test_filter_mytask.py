import unittest
import pytest
from parameterized import parameterized

from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from PageObjects.Filter_mytasks import filter_myTask

@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class Filter_MyTask(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lp = loginPage(self.driver)
        self.f = filter_myTask(self.driver)
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_filter(self):
        self.lp.log_in_out_Task_Management("login")
        self.f.filters()

    # def test_clear(self):
    #     self.lp.log_in_out_Task_Management("login")
    #     self.f.clear_Filter()
    #     self.lp.log_in_out_Task_Management("logout")

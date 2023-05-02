import unittest
import pytest
from parameterized import parameterized
from Utilities.configReader import readConfig
from PageObjects.loginPage import loginPage
from testCases.conftest import beforeClass


@pytest.mark.usefixtures("beforeClass", "beforeMethode")
class testLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def log_test(self):
        self.lp = loginPage(self.driver)
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.order(1)
    def test_loginPage(self):
        self.lp.log_in_out_Task_Management("login")

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(testLogin('test_loginPage'))
#     return suite
#
# if __name__ == '__main__':
#     unittest.TextTestRunner(verbosity=2).run(suite)

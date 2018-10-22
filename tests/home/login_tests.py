from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

class LoginTests(unittest.TestCase):

    def setUp(self):
        baseURL = "https://letskodeit.teachable.com/"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver )
        self.ts = TestStatus(self.driver)

    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        #assert result1 == True
        self.ts.mark(result1, "Title validation")
        result2 = self.lp.verifyLoginSuccessful()
        #assert result2 == True
        self.ts.markFinal("test_validLogin", result2, "Login Successfulness")

    #
    # def test_invalidLogin(self):
    #     self.lp.login(password = "abcabcabcabc")
    #     result = self.lp.verifyLoginFailed()
    #     self.assertTrue(result, "No se ha encontrado: 'Invalid email or password.'")

    def tearDown(self):
        self.driver.quit()


#py.test -s -v -p no:warnings --tb=short tests\home\login_tests.py

#--tb=short -p no:warning --html=report.html

#Terminal settings
#cmd.exe "/K" C:\Users\HOME\Anaconda3\Scripts\activate.bat py37

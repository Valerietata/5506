import time
from hytest import *
from selenium import webdriver
from lib.webui import *
from selenium.webdriver.support.ui import Select
class UI_0101:
    name = 'caseUI_0101'
    def setup(self):
        open_url()
    def teardown(self):
        wd = GSTORE['wd']
        logout()
        wd.quit()
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, 'testlogin')
        test_login('1234','1234')
        pagetext = GSTORE['pagetext']
        CHECK_POINT("login success")
class UI_0102:
    name = 'caseUI_0102'
    def setup(self):
        test_login('1234','1234')
    def teardown(self):
        wd = GSTORE['wd']
        logout()
        wd.quit()
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, 'test sign up')
        sign_up('123','123','123')

        CHECK_POINT("sign in success!")

class UI_0103:
    name = 'caseUI_0103'
    def setup(self):
        test_login()
    def teardown(self):
        wd = GSTORE['wd']
        logout()
        wd.quit()
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, 'test completed game')
        test_completed_game()
        CHECK_POINT("success")

class UI_0104:
    name = 'caseUI_0104'
    def setup(self):
        test_login()
    def teardown(self):
        wd = GSTORE['wd']
        logout()
        wd.quit()
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1, 'test completed game')
        incompleted_game()
        CHECK_POINT("success")


# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore


import unittest
from tests.testdata.settings import url, url_with_credentials
from tests.pages.request_page import HomePage
from time import sleep

class BaseTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(url_with_credentials())
        self.driver.get(url())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver(self.driver))

    def test_initial_request(self):
        HomePage(self.driver).submit_request()


if __name__ == '__main__':
    unittest.main()

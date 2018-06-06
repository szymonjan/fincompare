# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore

import unittest
from tests.testdata.settings import url, url_with_credentials
from tests.pages.request_page import HomePage, CompanySearchPage, ContactFormPage, RequestResultsPage

class BaseTests(WTFBaseTest):

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(url_with_credentials())
        self.driver.get(url())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver(self.driver))

    def test_valid_request(self):
        HomePage(self.driver).submit_request()
        company_search_page = CompanySearchPage(self.driver)
        self.assertIn("An welches Unternehmen", company_search_page.get_form_title())

        company_search_page.search_company("Fincompare")
        CompanySearchPage(self.driver).select_company()

        contact_form_page = ContactFormPage(self.driver)
        self.assertIn("geben Sie die Kontaktdaten", contact_form_page.get_form_title())

        ContactFormPage(self.driver).submit_contact_data()

        request_result_page = RequestResultsPage(self.driver)
        self.assertIn("passende Anbieter", request_result_page.get_table_title())

        request_result_page.select_random_offer()



if __name__ == '__main__':
    unittest.main()

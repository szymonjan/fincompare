# -*- coding: utf-8 -*-

from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER
from wtframework.wtf.utils.test_utils import do_and_ignore

import os
import unittest
from tests.testdata.settings import url, url_with_credentials
from tests.pages.request_page import HomePage, CompanySearchPage, ContactFormPage, RequestResultsPage, \
    DocumentsPage
from time import sleep

class BaseTests(WTFBaseTest):

    COMPANY_SEARCH_TITLE = "An welches Unternehmen"
    CONTACT_FORM_TITLE = "geben Sie die Kontaktdaten"
    RESULTS_PAGE_TITLE = "passende Anbieter"
    DOCUMENTS_PAGE_TITLE = "Ihre Anfrage"

    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.driver.get(url_with_credentials())

    def tearDown(self):
        do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver(self.driver))

    def test_valid_request(self):
        # Sumbit a valid request for random values
        HomePage(self.driver).submit_request()

        # Search and select company
        company_search_page = CompanySearchPage(self.driver)
        self.assertIn(self.COMPANY_SEARCH_TITLE, company_search_page.get_form_title())
        company_search_page.search_company("Fincompare")
        CompanySearchPage(self.driver).select_company()

        # Enter a valid contact data
        contact_form_page = ContactFormPage(self.driver)
        self.assertIn(self.CONTACT_FORM_TITLE, contact_form_page.get_form_title())
        ContactFormPage(self.driver).submit_contact_data()

        # Select random page
        request_result_page = RequestResultsPage(self.driver)
        self.assertIn(self.RESULTS_PAGE_TITLE, request_result_page.get_table_title())
        request_result_page.select_random_offer()

        # Upload documents
        self.assertIn(self.DOCUMENTS_PAGE_TITLE, DocumentsPage(self.driver).get_page_title())
        file_path = os.getcwd() + os.sep + os.path.join("assets", "document.pdf")
        DocumentsPage(self.driver).upload_documents(file_path)


if __name__ == '__main__':
    unittest.main()

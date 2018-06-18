# -*- coding: utf-8 -*-
# This file contains all of the pages used in tests. Every page should consist of loctors (e.g. Xpath)
# and methods used to interact with an webpage elements.

from tests.pages.base_page import BasePage

class HomePage(BasePage):

    """ This page will be used for making an initial request"""

    CATEGORY_DROPDOWN = "//input[@id='assetCategory']"
    CATEGORIES = "//ul[contains(@class, 'selectOptionsCategory')]//li"
    TYPE_DROPDOWN = "//input[@id='assetType']"
    TYPES = "//div[contains(@class, 'style__select')]//li"
    DESCRIPTION_FIELD = "//input[@id='description']"
    PRICE_FIELD = "//input[@id='purchasePrice']"
    CONTRACT_PERIOD_DROPDOWN = "//input[@id='term']"
    CONTRACT_PERIODS = "//div[contains(@class, 'contractPeriod')]//li"
    SUBMIT_BUTTON = "//button[@type='submit']"

    def __init__(self, driver):
        super().__init__(driver)

        self.description_field = self.find_clickable_element(self.DESCRIPTION_FIELD)
        self.price_field = self.find_clickable_element(self.PRICE_FIELD)
        self.submit_button = self.find_clickable_element(self.SUBMIT_BUTTON)

    def submit_request(self):
        """Submit a valid initial request on the homepage"""
        # Select random main category, subcategory and contract period
        self.select_random_dropdown_element(self.CATEGORY_DROPDOWN, self.CATEGORIES)
        self.select_random_dropdown_element(self.CONTRACT_PERIOD_DROPDOWN, self.CONTRACT_PERIODS)
        self.select_random_dropdown_element(self.TYPE_DROPDOWN, self.TYPES)

        # Fill description and price fields
        description = "Test description - {0}", format(self.get_random_string())
        self.description_field.send_keys(description)
        self.price_field.send_keys(self.get_random_number())

        # Finally submit the form
        self.submit_button.click()

class CompanySearchPage(BasePage):

    """This is company search page. It is used to find registered companies and select one of them"""

    FORM_TITLE = "//h2[contains(@class, 'forms__title')]"
    SEARCH_FIELD = "//input[@id='company-search-input']"
    SEARCH_BUTTON = "//button[@type='submit']"
    SEARCH_RESULTS = "//div[contains(@class, 'style__resultsList')]/div"

    def __init__(self, driver):
        super().__init__(driver)

        self.form_title = self.find_visible_element(self.FORM_TITLE)
        self.search_field = self.find_clickable_element(self.SEARCH_FIELD)
        self.search_button = self.find_clickable_element(self.SEARCH_BUTTON)

    def get_form_title(self):
        return self.form_title.text

    def search_company(self, company_name):
        self.search_field.send_keys(company_name)
        self.search_button.click()

    def select_company(self):
        self.select_random_element_from_list(self.SEARCH_RESULTS)


class ContactFormPage(BasePage):

    """This is contact form page. Here user have to pass his contact data in order to proceed with the request"""

    FORM_TITLE = "//h2[contains(@class, 'CompanyContactForm')]"
    GENDER_DROPDOWN = "//input[@id='company-search-gender']"
    GENDERS = "//ul[contains(@class, '_options-list')]/li"
    FIRST_NAME = "//input[@id='company-search-firstName']"
    LAST_NAME = "//input[@id='company-search-lastName']"
    EMAIL = "//input[@id='company-search-email']"
    PRIVACY_POLICY = "//div[@class='c-checkbox__wrapper']"
    SUBMIT_BUTTON = "//button[@type='submit']"

    def __init__(self, driver):
        super().__init__(driver)

        self.form_title = self.find_visible_element(self.FORM_TITLE)
        self.first_name = self.find_clickable_element(self.FIRST_NAME)
        self.last_name = self.find_clickable_element(self.LAST_NAME)
        self.email = self.find_clickable_element(self.EMAIL)
        self.privacy_policy = self.find_visible_element(self.PRIVACY_POLICY)
        self.submit_button = self.find_visible_element(self.SUBMIT_BUTTON)

    def get_form_title(self):
        return self.form_title.text

    def submit_contact_data(self):
        self.select_random_dropdown_element(self.GENDER_DROPDOWN, self.GENDERS)
        self.first_name.send_keys("Test")
        self.last_name.send_keys("User")
        self.email.send_keys("{0}@exmaple.com".format(self.get_random_string()))
        self.privacy_policy.click()
        self.submit_button.click()


class RequestResultsPage(BasePage):

    """This is request results page. Here user can view results of the request, update request
    values and select one of the offers - this opens documents page"""

    TABLE_TITLE = "//p[contains(@class, 'tableTitle')]"
    OFFERS = "//button[.='Vertrag anfordern']"

    def __init__(self, driver):
        super().__init__(driver)

        self.table_title = self.find_visible_element(self.TABLE_TITLE)

    def get_table_title(self):
        return self.table_title.text

    def select_random_offer(self):
        self.select_random_element_from_list(self.OFFERS)

    def upload_documet(self):
        self.webdriver.execute_script("handleUploadDocument()")

class DocumentsPage(BasePage):

    """On documents page user can see summary of the selected offer, list of documents,
     and if he didn't confirm his email notifiaction massage about that"""

    PAGE_TITLE = "//h2[contains(text(),'Ihre Anfrage')]"
    NOTIFICATION = "//div[contains(@class, 'Notification')]"
    DOCUMENTS_LIST = "//button[contains(@class, 'uploadButton')]"

    def __init__(self, driver):
        super().__init__(driver)

        self.page_title = self.find_visible_element(self.PAGE_TITLE)
        self.documents_list = self.find_list_of_elements(self.DOCUMENTS_LIST)

    def get_page_title(self):
        return self.page_title.text

    def upload_documents(self, file):
        for self.document in self.documents_list:
            self.document.drop_files(file)


if __name__=='__main__':
    pass
# -*- coding: utf-8 -*-
# This file contains all of the pages used in tests. Every page should consist of loctors (e.g. Xpath)
# and methods used to interact with an webpage elements.

from tests.pages.base_page import BasePage
from time import sleep

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

        self.category_dropdown = self.find_clickable_element(self.CATEGORY_DROPDOWN)
        self.categories = self.find_list_of_elements(self.CATEGORIES)
        self.type_dropdown = self.find_clickable_element(self.TYPE_DROPDOWN)
        self.types = self.find_list_of_elements(self.TYPES)
        self.description_field = self.find_clickable_element(self.DESCRIPTION_FIELD)
        self.price_field = self.find_clickable_element(self.PRICE_FIELD)
        self.contract_period_dropdown = self.find_clickable_element(self.CONTRACT_PERIOD_DROPDOWN)
        self.contract_periods = self.find_list_of_elements(self.CONTRACT_PERIODS)
        self.submit_button = self.find_clickable_element(self.SUBMIT_BUTTON)

    def submit_request(self):
        """Submit a valid initial request on the homepage"""
        #Select random main category, subcategory and contract period
        self.select_random_dropdown_element(self.category_dropdown, self.categories)
        self.select_random_dropdown_element(self.type_dropdown, self.types)
        self.select_random_dropdown_element(self.contract_period_dropdown, self.contract_periods)

        #Fill description and price fields
        description = "Test description - {0}", format(self.get_random_string())
        self.description_field.send_keys(description)
        self.price_field.send_keys("10000")
        sleep(3)

        #Finally submit the form
        self.submit_button.click()










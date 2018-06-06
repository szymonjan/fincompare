import time
import datetime
import random
import string

from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from wtframework.wtf.web.page import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(PageObject):
    """ This is a Base Page class that combines custom methods for building Page Objects. Every Page Object class
    inherits from Base Page
    """

    def __init__(self, webdriver, *args, **kwargs):
        super(BasePage, self).__init__(webdriver, *args, **kwargs)

    def find_visible_element(self, xpath):
        """Use this method to locate elements that are not visible instantly"""
        try:
            return WebDriverWait(self.webdriver, WTF_TIMEOUT_MANAGER.SHORT).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            msg = "No element located by XPATH - '{0}'".format(xpath)
            raise TimeoutException(msg)

    def find_clickable_element(self, xpath):
        """Use this method to locate elements that are not clickable instantly"""
        try:
            return WebDriverWait(self.webdriver, WTF_TIMEOUT_MANAGER.SHORT).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            msg = "No element located by XPATH - '{0}'".format(xpath)
            raise TimeoutException(msg)

    def find_list_of_elements(self, xpath):
        """ Use this method to get list of elements """
        try:
            return WebDriverWait(self.webdriver, WTF_TIMEOUT_MANAGER.SHORT).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath)))
        except TimeoutException:
            msg = "No elements located by XPATH - '{0}'".format(xpath)
            raise TimeoutException(msg)

    def select_hidden_element(self, visible_xpath, hidden_xpath):
        """Use this methods to select hidden elements """
        action = ActionChains(self.webdriver)
        # First hooover over an element
        action.move_to_element(self.find_visible_element(visible_xpath))
        # Then click on it
        action.click(self.find_visible_element(hidden_xpath))
        action.perform()

    def select_random_dropdown_element(self, dropdown_xpath, elements_xpath):
        """Use this methods to select random items from dropdown"""
        action = ActionChains(self.webdriver)
        action.click(self.find_clickable_element(dropdown_xpath))
        action.pause(WTF_TIMEOUT_MANAGER.BRIEF)
        action.click(self.get_random_element_from_list(self.find_list_of_elements(elements_xpath)))
        action.perform()

    def select_random_element_from_list(self, xpath):
        """Use this method to find a list of elements and select one at random"""
        element = self.get_random_element_from_list(self.find_list_of_elements(xpath))
        element.click()

    def get_random_element_from_list(self, list_of_elements):
        """FInd a list of elements and then click on one of them"""
        return random.choice(list_of_elements)

    def get_element_from_list(self, xpath, n):
        """ This method returns text from element from a list"""
        list = self.find_list_of_elements(xpath)
        return list[n].text

    def get_list_of_names(self, xpath):
        """ This method returns a list of strings for a list of elements. """
        names_list = []
        elements_list = self.find_list_of_elements(xpath)
        for element in elements_list:
            names_list.append(element.text)

        return names_list

    def confirm_alert(self):
        Alert(self.webdriver).accept()

    @staticmethod
    def get_current_date():
        """ Returns current date in format 'DD.MM'"""
        return datetime.date.today().strftime("%d.%m")

    @staticmethod
    def get_random_string():
        """Returns a random string with 6 letters"""
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for s in range(6))

    @staticmethod
    def get_random_number():
        """Returns a random 5-digit number"""
        return random.randint(10000, 50000)

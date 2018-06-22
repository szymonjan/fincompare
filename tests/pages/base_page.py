# -*- coding: utf-8 -*-

import datetime
import random
import string
import os.path

from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from wtframework.wtf.web.page import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


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
        """Choose one random element from a list of elements"""
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

    # Method from: https://gist.github.com/florentbr/349b1ab024ca9f3de56e6bf8af2ac69e
    def drop_files(self, files, offsetX=0, offsetY=0):
        """Use this method to upload files. Pass the file URL and the predefined JS script will
        drop this file to the WebElement that is used for receiving files (upload field or button) """
        JS_DROP_FILES = "var c=arguments,b=c[0],k=c[1];c=c[2];for(var d=b.ownerDocument||document,l=0;;){var e=b.getBoundingClientRect(),g=e.left+(k||e.width/2),h=e.top+(c||e.height/2),f=d.elementFromPoint(g,h);if(f&&b.contains(f))break;if(1<++l)throw b=Error('Element not interactable'),b.code=15,b;b.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var a=d.createElement('INPUT');a.setAttribute('type','file');a.setAttribute('multiple','');a.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');a.onchange=function(b){a.parentElement.removeChild(a);b.stopPropagation();var c={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:a.files,setData:function(){},getData:function(){},clearData:function(){},setDragImage:function(){}};window.DataTransferItemList&&(c.items=Object.setPrototypeOf(Array.prototype.map.call(a.files,function(a){return{constructor:DataTransferItem,kind:'file',type:a.type,getAsFile:function(){return a},getAsString:function(b){var c=new FileReader;c.onload=function(a){b(a.target.result)};c.readAsText(a)}}}),{constructor:DataTransferItemList,add:function(){},clear:function(){},remove:function(){}}));['dragenter','dragover','drop'].forEach(function(a){var b=d.createEvent('DragEvent');b.initMouseEvent(a,!0,!0,d.defaultView,0,0,0,g,h,!1,!1,!1,!1,0,null);Object.setPrototypeOf(b,null);b.dataTransfer=c;Object.setPrototypeOf(b,DragEvent.prototype);f.dispatchEvent(b)})};d.documentElement.appendChild(a);a.getBoundingClientRect();return a;"
        driver = self.parent
        isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
        paths = []

        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, list) else [files]):
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file if isLocal else self._upload(file))

        value = '\n'.join(paths)
        elm_input = driver.execute_script(JS_DROP_FILES, self, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

    WebElement.drop_files = drop_files


if __name__ == '__main__':
    pass

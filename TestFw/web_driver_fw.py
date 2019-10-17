"""
This module contains all the methods in selenium
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class WebDriverFw(webdriver.Firefox, webdriver.Chrome, webdriver.Ie, webdriver.Safari, Keys):
    """
        This class inherent the selenium webdriver.
        Purpose:
            -abstraction to the method of choosing the correct driver for  different browser_type
            -common methods to validate web content
            -common methods to interact the website
    """

    def __init__(self, browser_type):
        browser_type_lc = browser_type.lower()

        # this Proof Of Concept only support chrome for now
        if browser_type_lc == 'chrome':
            webdriver.Chrome.__init__(self)
            self.maximize_window()
            self.implicitly_wait(10)

        # todo:
        elif browser_type_lc == 'ie':
            webdriver.Ie.__init__(self)

        # todo:
        elif browser_type_lc == 'firefox':
            webdriver.Firefox.__init__(self)

        # todo:
        elif browser_type_lc == 'safari':
            webdriver.Safari.__init__(self)

        else:
            assert False, "argument should be one of: chrome, ie, firefox, safari"

    def validate_title(self, pattern, case_sensitive=True):
        """
        Validate the title of the open website
        :param pattern: Strings in the tittle to validate
        :param case_sensitive: True/False One can make it case_sensitive (default) or not sensitive
        :return: None
        """

        if not case_sensitive:
            pattern = pattern.lower()
            web_title = self.title.lower()
        else:
            web_title = self.title

        try:
            assert pattern in web_title, str(pattern) + " In Web title not found"
        except AssertionError as other_err:
            print("FAIL " + str(other_err))
        else:
            print("PASS patter found: " + str(pattern))

        print("\tTitle: " + str(self.title))

    def click_button_by_class_name(self, button_name):
        """
        This closes popup window
        :param button_name:
        :return:
        """
        sleep(5)
        widget = self.find_element_by_class_name(button_name)
        widget.click()


    def get_all_search_result(self, element_name, pattern):
        """
        Enter a two letter search criteria, and return the search result count
        :param element_name: html element
        :param pattern: pattern to enter into the search field
        :return: count
        """
        widget = self.find_element_by_name(element_name)
        widget.send_keys(pattern)
        sleep(3)
        element = self.find_element_by_xpath("//ul[@class='dropdown-menu']")
        option = element.find_elements_by_xpath("//li[@role='option']")
        widget.send_keys(Keys.CONTROL + 'a')
        widget.send_keys(Keys.DELETE)
        return len(option)

    def open_website(self, url):
        """
        open the website
        :param url:
        :return:
        """
        self.get(url)
        self.wait_for_site_render('homepage-headline')

    def wait_for_site_render(self, class_name, wait=5):
        """
        wait for site to complete rendering based on class_name
        :param class_name:
        :param wait:
        :return:
        """
        url = self.current_url
        try:
            WebDriverWait(self, wait).until(ec.presence_of_element_located(
                (By.CLASS_NAME, class_name)))
            print('PASS ' + url + ' open')
        except TimeoutException:
            print('FAIL ' + url + ' took too long')
            exit()

__author__ = 'Dmitry Kozhinov'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback

class GoogleRuPage(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30


    def find_element(self, *loc):
        assert self.browser.find_element(*loc)
        return self.browser.find_element(*loc)


    def visit(self, url):
        self.browser.get(url)


    # Позволяет определить поведение экземпляра пользовательского типа при попытке получения значения атрибута
    # Метод должен возвращать значение (возможно вычисляемое) для атрибута, либо генерировать исключение
    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                return self.find_element(*self.locator_dictionary[what])

        except AttributeError:
            GoogleRuPage.__getattribute__(self, what)

    locator_dictionary = {
        "search_string_field": (By.XPATH, '//input[@name="q"]'),
        "search_submit_button": (By.XPATH, '//input[@name="btnK"]'),
        "founding_cbr_site_link": (By.XPATH, '//a[@href="https://www.cbr.ru/"]')
    }

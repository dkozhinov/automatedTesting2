from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback

class CbrRuPage(object):

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
            CbrRuPage.__getattribute__(self, what)

    locator_dictionary = {
        "internet_reception_link": (By.XPATH, '//a[contains(.,"Интернет-приемная")]'),
        "write_gratitude_link": (By.XPATH, '//h2[contains(.,"Написать благодарность")]'),
        "messagebody_textarea": (By.XPATH, '//textarea[contains(@name,"MessageBody")]'),
        "agreement_checkbox": (By.XPATH, '//input[@name="Agreement"]'),
        "three_strips_button": (By.XPATH, '//span[contains(@class,"burger")]'),
        "three_strips_button_section_about": (By.LINK_TEXT, 'О сайте'),
        "three_strips_button_section_about_warning": (By.LINK_TEXT, 'Предупреждение'),
        "three_strips_button_section_about_warning_content": (By.ID, 'content'),
        "changed_language_en": (By.XPATH, '//a[contains(.,"EN")]')
    }

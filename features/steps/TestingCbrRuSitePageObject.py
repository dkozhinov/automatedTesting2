__author__ = 'Dmitry Kozhinov'

from behave import *
from features.lib.utility import *
from features.pages.GooglePage import *
from features.pages.CbrPage import *


# Для запомнинания текста предупреждения
__save_warning_text__ = ""

# Файл скриншота
__screenshot_filename__ = 'screenshots\\screenshot.png'


@given('website www.google.ru')
def step(context):
    page = GoogleRuPage(context)
    page.visit("http://www.google.ru")


@when("push search button with text '{text}'")
def step(context, text):
    page = GoogleRuPage(context)
    page.search_string_field.send_keys(text)
    page.search_submit_button.submit()


@then("displayed page www.google.ru and opened cbr.ru site link")
def step(context, link):
    page = GoogleRuPage(context)
    page.visit_without_new_tab(context, page.founding_cbr_site_link)


@then("on cbr.ru opened link Internet-reception")
def step(context):
    page = CbrRuPage(context)
    page.internet_reception_link.click()


@then("opened link Write gratitude")
def step(context):
    page = CbrRuPage(context)
    page.write_gratitude_link.click()


@then("write in textarea MessageBody '{text}'")
def step(context,text):
    page = CbrRuPage(context)
    page.messagebody_textarea.send_keys(text)


@then("select the checkbox Agreement")
def step(context):
    page = CbrRuPage(context)
    page.agreement_checkbox.click()

@then("make screenshot and send email")
def step(context):
    deletefile(__screenshot_filename__)
    context.browser.save_screenshot(__screenshot_filename__)
    sendemail(__screenshot_filename__)


@then("press the button Three strips")
def step(context):
    page = CbrRuPage(context)
    page.three_strips_button.click()


@then("clicked on the section About")
def step(context):
    page = CbrRuPage(context)
    page.three_strips_button_section_about.click()


@then("clicked link Warning")
def step(context):
    page = CbrRuPage(context)
    page.three_strips_button_section_about_warning.click()


@then("save warning text")
def step(context):
    page = CbrRuPage(context)
    __save_warning_text__ = page.three_strips_button_section_about_warning_content.text
    print("save_warning_text=", __save_warning_text__)


@then("changed page language to en")
def step(context):
    page = CbrRuPage(context)
    page.changed_language_en.click()


@then("check warning text is different from the memorized text previously")
def step(context):
    page = CbrRuPage(context)
    assert __save_warning_text__ != page.three_strips_button_section_about_warning_content.text, \
        "Aborting test: warning text is equal from the memorized text previously"


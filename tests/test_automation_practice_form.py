import random

from selene.support.shared import browser
from selene import be, have
import pytest
import time

@pytest.fixture()
def browser_preconfig():
    browser.config.browser_name="chrome"
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width=1920
    browser.config.window_height=1080
    browser.config.save_screenshot_on_failure
    yield

def test_submit_info(browser_preconfig):
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Practice Form'))
    browser.element('#firstName').type('Ilyas')  #name
    browser.element('#lastName').type('Mustafin')  #lastname
    browser.element('#userEmail').type('someEmail@mail.ru')  #email

    browser.element('#userNumber').type(random.randint(1111111111,9999999999))  #phone
    browser.element('#subjectsInput').type('so').press_enter().type('ch').press_enter()  #subjects : Social Studies, Chemistry

    browser.element('#currentAddress').type('fvhghsdkvhl')

    time.sleep(2)
import random
from faker import Faker
fake = Faker('ru_RU')
import os
filename = '/testdata/kitty.jpeg'
from selene.support.shared import browser
from selene import be, have
import pytest
import time

@pytest.fixture()
def browser_preconfig():
    browser.config.browser_name="chrome"
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.window_width=1920
    #browser.config.window_height=1080
    yield
    browser.config.quit_driver()

def test_submit_info(browser_preconfig):
    browser.open('/automation-practice-form').driver.fullscreen_window()
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Practice Form'))
    # Name
    browser.element('#firstName').type(fake.first_name())
    browser.element('#lastName').type(fake.last_name())
    # Email
    browser.element('#userEmail').type(fake.ascii_company_email())
    # Gender
    browser.element('#gender-radio-1').double_click()
    # Mobile
    browser.element('#userNumber').type(random.randint(1111111111,9999999999))
    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1987')
    browser.element('[aria-label="Choose Sunday, June 7th, 1987"]').click()
    # Subjects : Social Studies, Chemistry
    browser.element('#subjectsInput').type('so').press_enter().type('ch').press_enter()
    # Hobbies
    browser.element("label[for='hobbies-checkbox-1']").click()
    browser.element("label[for='hobbies-checkbox-2']").click()
    browser.element("label[for='hobbies-checkbox-3']").click()
    # Picture
    browser.element('#uploadPicture').send_keys(os.path.dirname(os.getcwd())+filename)
    # Current Address
    browser.element('#currentAddress').type(fake.address())
    # State and city
    browser.element('#react-select-3-input').type('ut').press_enter()
    browser.element('#react-select-4-input').type('a').press_enter()
    browser.element('#submit').click()

    #Check
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should((have.text('Male')))

    time.sleep(10)
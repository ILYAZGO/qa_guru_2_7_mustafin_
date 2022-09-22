from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown

main_header = browser.element('.main-header')
submition_table_title = browser.element('#example-modal-sizes-title-lg')
submition_table = browser.element('.table-responsive')
submit_button = browser.element('#submit')


def fill_out_name(firstname, lastname):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)


def fill_out_email(email):
    browser.element('#userEmail').type(email)


def fill_out_mobile(number):
    browser.element('#userNumber').type(number)


def fill_out_subject_with_addition(subject1, subject2):
    browser.element('#subjectsInput').type(subject1).press_enter().type(subject2).press_enter()


def fill_out_current_address(address):
    browser.element('#currentAddress').type(address)


def select_state(state):
    element = browser.element('#state')
    dropdown.select(element, state)


def select_city(city):
    element = browser.element('#city')
    dropdown.select(element, city)


def select_state_and_city(state, city):
    browser.element('#react-select-3-input').type(state).press_enter()
    browser.element('#react-select-4-input').type(city).press_enter()

from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


def input(day: str, month: str, year: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL+'a').type(day+month+year).press_enter()


# browser.element('#dateOfBirthInput').clear().click()
# browser.element('.react-datepicker__month-select').type('June')
# browser.element('.react-datepicker__year-select').type('1987')
# browser.element('[aria-label="Choose Sunday, June 7th, 1987"]').click()

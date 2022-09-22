from selene.support.shared import browser

main_header = browser.element('.main-header')
add_new = browser.element('#addNewRecordButton')
submit_button = browser.element('#submit')
table = browser.element('.rt-table')
delete_button = browser.all('[title="Delete"]')


def fill_out_name(firstname, lastname):
    browser.element('#firstName').clear().type(firstname)
    browser.element('#lastName').clear().type(lastname)


def fill_out_email(email):
    browser.element('#userEmail').clear().type(email)


def fill_out_age(age):
    browser.element('#age').clear().type(age)


def fill_out_salary(salary):
    browser.element('#salary').clear().type(salary)


def fill_out_department(department):
    browser.element('#department').type(department)


def delete_record(number):
    browser.element('#delete-record-' + str(number)).click()

from demoqa_tests.utils.params import *
from demoqa_tests.model.select_page import *
from demoqa_tests.model.pages.web_tables import *
from selene.support.shared import browser
from selene import be, have


def test_add_new_record(browser_preconfig):
    # GIVEN
    given_opened('/webtables')
    browser.should(have.title('ToolsQA'))
    main_header.should(be.visible)

    # WHEN
    add_new.click()
    fill_out_name(first_name, last_name)
    fill_out_email(email)
    fill_out_age(age)
    fill_out_salary(ten_digits)
    fill_out_department(department)
    submit_button.click()

    # THEN
    table.should(have.text(first_name))
    table.should(have.text(last_name))
    table.should(have.text(email))
    table.should(have.text(age))
    table.should(have.text(ten_digits))
    table.should(have.text(department))


def test_edit_record_2(browser_preconfig):
    # WHEN
    browser.element('#edit-record-2').click()
    fill_out_name('IVAN', 'IVANOV')
    fill_out_email('ivanov@mail.com')
    fill_out_age(age)
    fill_out_salary(ten_digits)
    fill_out_department(department)
    browser.element('#submit').click()
    # THEN
    table.should(have.text('IVAN'))
    table.should(have.text('IVANOV'))
    table.should(have.text('ivanov@mail.com'))
    table.should(have.text(age))
    table.should(have.text(ten_digits))
    table.should(have.text(department))


def test_rows_after_delete(browser_preconfig):
    # WHEN
    delete_record(3)
    # THEN
    delete_button.should(have.size(3))

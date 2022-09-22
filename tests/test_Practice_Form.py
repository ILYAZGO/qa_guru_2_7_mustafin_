from demoqa_tests.utils.params import *
from demoqa_tests.model.select_page import *
from demoqa_tests.model.pages.practice_form import *
from demoqa_tests.model.controls import checkbox, radio_button, upload, calendar
from selene.support.shared import browser
from selene import be, have


def test_registration_form(browser_preconfig):
    # GIVEN
    given_opened('/automation-practice-form')
    # WHEN
    browser.should(have.title('ToolsQA'))
    main_header.should(be.visible)
    fill_out_name(first_name, last_name)
    fill_out_email(email)
    radio_button.pick_button(1)
    fill_out_mobile(ten_digits)
    calendar.input(day, month, year)
    fill_out_subject_with_addition(subject1, subject2)
    checkbox.select_necessary_checkboxes(3)
    upload.file(filename)
    fill_out_current_address(address)
    # select_state(state)
    # select_city(city)
    select_state_and_city(state, city)
    submit_button.click()
    # THEN
    submition_table_title.should(be.visible)
    submition_table.should(have.text(first_name + ' ' + last_name))
    submition_table.should(have.text(email))
    submition_table.should(have.text('Male'))
    submition_table.should(have.text(ten_digits))
    submition_table.should(have.text('07 June,1987'))
    submition_table.should(have.text('Social Studies, Chemistry'))
    submition_table.should(have.text('Sports, Reading, Music'))
    submition_table.should(have.text('kitty.jpeg'))
    submition_table.should(have.text(address))
    submition_table.should(have.text('Uttar Pradesh Agra'))

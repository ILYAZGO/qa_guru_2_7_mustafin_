from .params import *
from demoqa_tests.model.select_page import *
from demoqa_tests.model.pages.registration_form import *
from demoqa_tests.model.controls import checkbox
from selene.support.shared import browser
from selene import be, have

def test_registration_form(browser_preconfig):
    given_opened('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(be.visible).should(have.text('Practice Form'))

    fill_out_name(first_name,last_name)
    fill_out_email(email)
    # Gender
    browser.element('#gender-radio-1').double_click()
    fill_out_mobile(ten_digits)
    # Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1987')
    browser.element('[aria-label="Choose Sunday, June 7th, 1987"]').click()
    # Subjects : Social Studies, Chemistry
    browser.element('#subjectsInput').type('so').press_enter().type('ch').press_enter()
    # Hobbies
    checkbox.select_necessary_checkboxes(3)
    # Picture
    #print(os.path.dirname(os.getcwd())+filename)
    browser.element('#uploadPicture').send_keys(path)
    # Current Address
    browser.element('#currentAddress').type(address)
    # State and city
    browser.element('#react-select-3-input').type('ut').press_enter()
    browser.element('#react-select-4-input').type('a').press_enter()
    browser.element('#submit').click()

    #Check
    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(first_name+' '+last_name))
    browser.element('.table-responsive').should(have.text(email))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text(ten_digits))
    browser.element('.table-responsive').should(have.text('07 June,1987'))
    browser.element('.table-responsive').should(have.text('Social Studies, Chemistry'))
    browser.element('.table-responsive').should(have.text('Sports, Reading, Music'))
    browser.element('.table-responsive').should(have.text('kitty.jpeg'))
    browser.element('.table-responsive').should(have.text(address))
    browser.element('.table-responsive').should(have.text('Uttar Pradesh Agra'))

def test_table_change(browser_preconfig):
    given_opened('/webtables')
    browser.element('.main-header').should(have.text('Web Tables'))

    #Step1
    browser.element('#addNewRecordButton').click()
    browser.element('#registration-form-modal').should(be.visible).should(have.text('Registration Form'))
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('#age').type(age)
    browser.element('#salary').type(ten_digits)
    browser.element('#department').type(department)
    browser.element('#submit').click()
    #Step1 check
    browser.element('.rt-table').should(have.text(first_name))
    browser.element('.rt-table').should(have.text(last_name))
    browser.element('.rt-table').should(have.text(email))
    browser.element('.rt-table').should(have.text(age))
    browser.element('.rt-table').should(have.text(ten_digits))
    browser.element('.rt-table').should(have.text(department))

    #Step2
    browser.element('#edit-record-2').click()
    actual_first_name = browser.element('#firstName').get_attribute('value')
    browser.element('#firstName').type(add_letter)
    actual_last_name = browser.element('#lastName').get_attribute('value')
    browser.element('#lastName').type(add_letter)
    actual_email = browser.element('#userEmail').get_attribute('value')
    browser.element('#userEmail').type(add_letter)
    browser.element('#age').clear().type(age)
    browser.element('#salary').clear().type(ten_digits)
    actual_department = browser.element('#department').get_attribute('value')
    browser.element('#department').type(add_letter)
    browser.element('#submit').click()

    #Step2 check
    browser.element('.rt-table').should(have.text(actual_first_name+add_letter))
    browser.element('.rt-table').should(have.text(actual_last_name+add_letter))
    browser.element('.rt-table').should(have.text(actual_email+add_letter))
    browser.element('.rt-table').should(have.text(age))
    browser.element('.rt-table').should(have.text(ten_digits))
    browser.element('.rt-table').should(have.text(actual_department+add_letter))


    #Step3
    browser.element('#delete-record-3').click()

    #Step3 check
    browser.all('[title="Delete"]').should(have.size(3))
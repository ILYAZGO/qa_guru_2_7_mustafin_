import os
from .params import first_name,last_name,email,mobile,path,address
from selene.support.shared import browser
from selene import be, have


def test_submit_info(browser_preconfig):
    browser.open('/automation-practice-form').driver.fullscreen_window()
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Practice Form'))
    # Name
    print(first_name)
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    # Email
    browser.element('#userEmail').type(email)
    # Gender
    browser.element('#gender-radio-1').double_click()
    # Mobile
    browser.element('#userNumber').type(mobile)
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
    #print(os.path.dirname(os.getcwd())+filename)
    browser.element('#uploadPicture').send_keys(path)
    # Current Address
    browser.element('#currentAddress').type(address)
    # State and city
    browser.element('#react-select-3-input').type('ut').press_enter()
    browser.element('#react-select-4-input').type('a').press_enter()
    browser.element('#submit').click()

    #Check
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(first_name))
    browser.element('.table-responsive').should(have.text(last_name))
    browser.element('.table-responsive').should(have.text(email))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text(str(mobile)))
    browser.element('.table-responsive').should(have.text('07 June,1987'))
    browser.element('.table-responsive').should(have.text('Social Studies, Chemistry'))
    browser.element('.table-responsive').should(have.text('Sports, Reading, Music'))
    browser.element('.table-responsive').should(have.text('kitty.jpeg'))
    browser.element('.table-responsive').should(have.text(address))
    browser.element('.table-responsive').should(have.text('Uttar Pradesh Agra'))
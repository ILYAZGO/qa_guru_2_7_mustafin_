from selene.support.shared import browser
from selene import be, have
from tests.params import *

def fill_out_name(firstname,lastname):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)

def fill_out_email(email):
    browser.element('#userEmail').type(email)

def fill_out_mobile(number):
    browser.element('#userNumber').type(number)

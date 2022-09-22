from selene.support.shared import browser


def pick_button(button_number: int):
    browser.element(f'[for=gender-radio-{button_number}]').click()
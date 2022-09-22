from selene.support.shared import browser


def file(path):
    browser.element('#uploadPicture').send_keys(path)

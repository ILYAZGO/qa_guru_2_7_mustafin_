from selene.support.shared import browser


def given_opened(url):
    browser.open(url).driver.fullscreen_window()

from selene.support.shared import browser


def select_necessary_checkboxes(summa: int):
    i = 1
    while i <= summa:
        browser.element(f"label[for='hobbies-checkbox-{i}']").click()
        i += 1

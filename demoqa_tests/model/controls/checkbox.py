from selene.support.shared import browser


def select_necessary_checkboxes(sum:int):
    i=1
    while i <= sum:
        browser.element(f"label[for='hobbies-checkbox-{i}']").click()
        i += 1
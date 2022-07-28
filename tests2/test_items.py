from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_find_add_card_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
        present_elem = True
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"


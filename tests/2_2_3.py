from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:

    link = "http://suninjuly.github.io/selects1.html" #можно пробывать с сайтом ../selects2.html
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1 = num1.text

    num2 = browser.find_element(By.ID, 'num2')
    num2 = num2.text

    z = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
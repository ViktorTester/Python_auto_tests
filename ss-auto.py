from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://www.ss.com/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "/html/body/div[1]/div/span[4]/div[1]/a")
    button.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "a_menu")
    button.click()
    time.sleep(1)

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='1']")
    option1.click()
    time.sleep(1)

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='14080']")
    option2.click()
    time.sleep(1)

    select = Select(browser.find_element(By.CLASS_NAME, "new_ad_select"))
    select.select_by_value("319")
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "b.new_ad_select")
    button.click()
    time.sleep(1)

    input1 = browser.find_element(By.ID, "login_txt")
    input1.send_keys("28836986")
    time.sleep(1)

    input2 = browser.find_element(By.ID, "pass_txt")
    input2.send_keys("undeadrulz")
    time.sleep(1)

    option3 = browser.find_element(By.ID, "savepass")
    option3.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn.l153")
    button.click()
    time.sleep(1)

    option4 = browser.find_element(By.ID, "rules")
    option4.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "b200.btn100")
    button.click()
    time.sleep(1)

    select = Select(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[3]/td/div/div/select"))
    select.select_by_value("114422")
    time.sleep(1)

    select = Select(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[6]/td[1]/div/div/select"))
    select.select_by_value("7428")
    time.sleep(1)

    option5 = browser.find_element(By.ID, "o_1747")
    option5.click()
    time.sleep(1)

    option5 = browser.find_element(By.ID, "o_1748")
    option5.click()
    time.sleep(1)

    option5 = browser.find_element(By.ID, "o_1749")
    option5.click()
    time.sleep(1)

    select = Select(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[8]/td[1]/div/div/select"))
    select.select_by_value("24260")
    time.sleep(1)

    select = Select(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[9]/td[1]/div/div/select"))
    select.select_by_value("16974")
    time.sleep(1)

    input3 = browser.find_element(By.ID, "opt[354]")
    input3.send_keys("с 10 до 18")
    time.sleep(1)

    input4 = browser.find_element(By.ID, "opt[1281]")
    input4.send_keys("Улица Бривибас")
    time.sleep(1)

    input4 = browser.find_element(By.ID, "mtxt_field")
    input4.send_keys("Нужен работник. Срочно.")
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "b.w200.btn100")
    button.click()
    time.sleep(1)

    button = browser.find_element(By.ID, "alert_ok")
    button.click()
    time.sleep(1)

    select = Select(browser.find_element(By.ID, "region_town"))
    select.select_by_value("16975")
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "b.w200.btn100")
    button.click()
    time.sleep(1)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



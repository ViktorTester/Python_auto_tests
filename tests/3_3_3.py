import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestAbs(unittest.TestCase):

    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("viktor345@inbox.lv")
        input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("12345678")
        input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
        input5.send_keys("london")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        congratulations = browser.find_element(By.XPATH, "/html/body/div/h1")
        congratulations = congratulations.text
        self.assertEqual("Congratulations! You have successfully registered!", congratulations)
        browser.quit()



    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("viktor345@inbox.lv")
        input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("12345678")
        input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
        input5.send_keys("london")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        congratulations = browser.find_element(By.XPATH, "/html/body/div/h1")
        congratulations = congratulations.text
        self.assertEqual("Congratulations! You have successfully registered!", congratulations)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

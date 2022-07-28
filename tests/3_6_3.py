import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895/step/1",
                                   "236896/step/1",
                                   "236897/step/1",
                                   "236898/step/1",
                                   "236899/step/1",
                                   "236903/step/1",
                                   "236904/step/1",
                                   "236905/step/1"])

def test_various_links(browser, links):
    link = f"https://stepik.org/lesson/{links}"
    browser.get(link)
    answer = str(math.log(int(time.time() + 6.6)))
    time.sleep(5)
    input1 = browser.find_element(By.CSS_SELECTOR, '.attempt-wrapper .textarea')
    input1.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()
    time.sleep(3)

    incorrect_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    incorrect = incorrect_text.text
    assert "Correct!" == incorrect, "Should be right answer"

if __name__ == "__main__":
    pytest.main()
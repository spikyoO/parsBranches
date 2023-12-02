import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    browser.find_element(By.ID, "answer").send_keys(calc(browser.find_element(By.ID, "input_value").text))
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()

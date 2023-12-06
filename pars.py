from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://devcasino-scr1-var1.test.egamings.com/'

def get_data_with_selenium():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.maximize_window()
        time.sleep(5)
        with open("devcasino_scr1_var1.html", "w", encoding="utf-8") as file:
            file.write(browser.page_source)
    finally:
        browser.close()
        browser.quit()

def main():
    get_data_with_selenium()

if __name__ == '__main__':
    main()
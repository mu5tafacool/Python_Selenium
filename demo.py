import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def main():
    driver = setUp()
    geturl(driver)
    webelement_username(driver)


def setUp():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver


def geturl(driver):
    driver.get("https://www.google.com/")


# weeks problem page
def webelement_username(driver):
    try:
        elemweeks = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "")))
        elemweeks.click()
        elemweeks.send_keys("text")
        time.sleep(3)

    except TimeoutException:
        print("object not found in " + driver.current_url)


if __name__ == "__main__":
    main()

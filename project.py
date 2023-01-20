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

    youtube_intro_play(driver)
    youtube_pause(driver)
    webelement_weeks(driver)

    webElement0(driver)
    problem_set(driver)
    problem_click(driver)
    list_problem_write(driver)

    webElement1(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement2(driver)
    problem_set(driver)
    list_problem_write(driver)

    time.sleep(4)
    driver.quit()


def setUp():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver


def geturl(driver):
    driver.get("https://cs50.harvard.edu/python/2022/")


# weeks problem page
def webelement_weeks(driver):
    driver.get("https://cs50.harvard.edu/python/2022/")
    try:
        elemweeks = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[text()='weeks']")))
        elemweeks.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)


def webElement0(driver):

    try:
        elemfunk = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Functions, Variables']")))
        elemfunk.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement1(driver):
    time.sleep(1)
    try:
        elemcond = driver.find_element(
            By.LINK_TEXT, "Conditionals")
        time.sleep(3)
        driver.execute_script("arguments[0].click();", elemcond)
    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement2(driver):
    time.sleep(1)
    try:
        elemloop = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Loops")))
        elemloop.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def problem_set(driver):
    try:
        elem = driver.find_element(By.XPATH, "//a[contains(.,'Problem Set')]")
        time.sleep(3)
        driver.execute_script("arguments[0].click();", elem)
    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


# problem click assert name of problem
def problem_click(driver):
    list_week = driver.find_elements(
        By.XPATH, "//main//ul[@class='fa-ul']//li//a")
    web_elem_list = []
    for element in list_week:
        web_elem_list.append(element.text)

    page = 1

    while True:
        try:
            if len(web_elem_list) >= page:
                # click problem index
                problem_element = driver.find_element(
                    By.XPATH, f"//main//ul[@class='fa-ul']//li[{page}]//a")
                problem_element.click()
                time.sleep(1)
                # page name title split
                title = driver.title.rstrip().split(" -")
                # problem name
                text = driver.find_element(By.XPATH, "//main/h1/a")

                # assert to page from title
                assert (text.text) in (f"{title[0]}")

                page += 1
                time.sleep(1)
                driver.back()
                time.sleep(1)
            else:
                break
        except:
            continue


def list_problem_write(driver):
    lists = driver.find_elements(
        By.XPATH, "//main//ul[@class='fa-ul']//li")
    i = 1
    with open("lists_of_problem_set.txt", "a") as file:
        title = driver.title.rstrip().split(" -")
        file.write(f"\n{title[0]}\n")
        for element in lists:
            print(int(i), element.text)  # print

            file.write(f"{int(i)}. {element.text}\n")

            i += 1


def youtube_intro_play(driver):
    elemsummry = driver.find_element(
        By.XPATH, "//summary").click()

    element = driver.find_element(
        By.XPATH, "//iframe[@id='iFrameResizer0']").click()

    # fullscreen video
    ActionChains(driver).send_keys('f').perform()
    time.sleep(15)


def youtube_pause(driver):

    ActionChains(driver).send_keys(Keys.ESCAPE).perform()


if __name__ == "__main__":
    main()

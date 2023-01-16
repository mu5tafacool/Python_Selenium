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

    webElement3(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement4(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement5(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement6(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement7(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement8(driver)
    problem_set(driver)
    list_problem_write(driver)

    webElement9(driver)
    list_problem_write(driver)

    time.sleep(4)
    driver.quit()


def setUp():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    # driver.wait = WebDriverWait(driver, 5)
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


# write to list of week problem titles
def webelement_week_list(driver):

    lists = driver.find_elements(By.XPATH, "//main/ol/li")
    i = 0
    for element in lists:
        # print("week", int(i), element.text)
        with open("week_list.txt", "a") as file:
            file.write(f"Week{int(i)}, {element.text}\n")

        i += 1


def webElement0(driver):

    try:
        elemfunk = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[text()='Functions, Variables']")))
        elemfunk.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement1(driver):
    # driver.get("https://cs50.harvard.edu/python/2022/")
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


def webElement3(driver):
    time.sleep(1)
    try:
        elemexc = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Exceptions")))
        elemexc.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement4(driver):
    time.sleep(1)
    try:
        elemlib = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Libraries")))
        elemlib.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement5(driver):
    time.sleep(1)
    try:
        elemunit = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Unit Tests")))
        elemunit.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement6(driver):
    time.sleep(1)
    try:
        elemfile = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "File I/O")))
        elemfile.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement7(driver):
    time.sleep(1)
    try:
        elemregular = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Regular Expressions")))
        elemregular.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement8(driver):
    time.sleep(1)
    try:
        elemoop = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Object-Oriented Programming")))
        elemoop.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)
    return driver.title


def webElement9(driver):
    time.sleep(1)
    try:
        elemel = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Et Cetera")))
        elemel.click()

    except TimeoutException:
        print("object not found in " + driver.current_url)

    try:
        elemfinal = driver.find_element(By.LINK_TEXT, "Final Project")
        time.sleep(3)
        driver.execute_script("arguments[0].click();", elemfinal)
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


def list_submit_problem(driver):
    # driver.get("https://cs50.harvard.edu/python/2022/")
    lists = driver.find_elements(By.XPATH, "//main//li[3]//li")
    i = 1
    for element in lists:
        print(int(i), element.text)

        i += 1


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

# print to list of week problem


def webelement_week_read():
    with open("lists_problem_set.txt", "r") as file:  # "r" read
        for line in file:
            row = line.rstrip().split(". ")
            if len(row) > 1:
                print(f"{row[1]}")  # problem name list


def youtube_play(driver):
    ytb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@class='ytp-large-play-button-bg']"))
    )
    ytb[0].click()


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

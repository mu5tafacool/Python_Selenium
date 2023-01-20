import pytest
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
# from project import *
from project import webElement0, webElement1, webElement2, problem_set, problem_click


# terminal>$ python -m  pytest test_project.py

chrome_driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))
chrome_driver.maximize_window()


def test_url():
    chrome_driver.get('https://cs50.harvard.edu/python/2022/')


def test_week0():
    assert webElement0(chrome_driver) == chrome_driver.title
    assert webElement0(
        chrome_driver) == "Week 0 Functions - CS50's Introduction to Programming with Python"


def test_problem_set_page():
    assert problem_set(chrome_driver) == chrome_driver.title


def test_problems_of_week():
    problem_click(chrome_driver)


def test_week1():
    assert webElement1(chrome_driver) == chrome_driver.title
    assert webElement1(
        chrome_driver) == "Week 1 Conditionals - CS50's Introduction to Programming with Python"


def test_week2():
    assert webElement2(chrome_driver) == chrome_driver.title
    assert webElement2(
        chrome_driver) == "Week 2 Loops - CS50's Introduction to Programming with Python"

import pytest
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from project import *


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


def test_week3():
    assert webElement3(chrome_driver) == chrome_driver.title
    assert webElement3(
        chrome_driver) == "Week 3 Exceptions - CS50's Introduction to Programming with Python"


def test_week4():
    assert webElement4(chrome_driver) == chrome_driver.title
    assert webElement4(
        chrome_driver) == "Week 4 Libraries - CS50's Introduction to Programming with Python"


def test_week5():
    assert webElement5(chrome_driver) == chrome_driver.title
    assert webElement5(
        chrome_driver) == "Week 5 Unit Tests - CS50's Introduction to Programming with Python"


def test_week6():
    assert webElement6(chrome_driver) == chrome_driver.title
    assert webElement6(
        chrome_driver) == "Week 6 File I/O - CS50's Introduction to Programming with Python"


def test_week7():
    assert webElement7(chrome_driver) == chrome_driver.title
    assert webElement7(
        chrome_driver) == "Week 7 Regular Expressions - CS50's Introduction to Programming with Python"


def test_week8():
    assert webElement8(chrome_driver) == chrome_driver.title
    assert webElement8(
        chrome_driver) == "Week 8 Object-Oriented Programming - CS50's Introduction to Programming with Python"


def test_week9():
    assert webElement9(chrome_driver) == chrome_driver.title
    assert webElement9(
        chrome_driver) == "Final Project - CS50's Introduction to Programming with Python"

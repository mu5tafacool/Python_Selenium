<a name="readme-top"></a>

<h1 align="center">Automation CS50P</h1>
<h2 align="center">Final Project</h2>

#### Video Demo: <https://youtu.be/2FYpvbXCQIw>

#### Description:

**Decision of the CS50P course, final project idea by Harvard:**
Automation tool that I use in Java programming language, at the end of the research. I decided to use [Selenium](https://pypi.org/project/selenium/) package. I found a title called **Automation CS50P**. There was also a need for other packages to help me do this project. After Run, It automatically adds the browser driver to the project with the [webdriver-manager](https://pypi.org/project/webdriver-manager/) package. [pytest-selenium](https://pypi.org/project/pytest-selenium/) is a plugin for pytest and it allows to test the selenium based project.
This project is to automation the course website using [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/).

### What's Automation test?

> In summary, any software or application has expected criteria. It is the process of testing them using an automation test tool. The goal is to compare the actual result with the expected result and find defects or bugs.
>
> - To build bug-free applications.
> - To satisfy end user and client.

# CS50’s Introduction to Programming with Python in Automation Testing

- ## This Acceptable Criteria
  ### Purpose of the test:
  > - Accessing the member course site.
  > - Watching a course introduction video.
  > - See the weekly course materials.
  > - Accessing and seeing each week's problem sets.

## To begin

---

- You can install request modules with their methods:

```
    pip install -r requirements.txt
```

- Run automation program with:

```
    python project.py
```

- Run your tests by executing:

```
    python -m  pytest test_project.py
```

## Project Steps

### `project.py`

### Run on beginning

> - Installing a browser to work
> - The second run method maximizes the browser window by webdriver method

### After Run

> - The browser goes to the [course site](https://cs50.harvard.edu/python/2022/)
> - Opens and closes the [introduction video](https://youtu.be/OvKCESUCWII) of the course in full screen
> - Opening the elements panel to [inspect](https://en.wikipedia.org/wiki/Web_development_tools) on browser, then creating locators by using the [`find_element` method](https://www.selenium.dev/documentation/webdriver/elements/finders/)
> - The time has been set to wait for the web pages to be opened by until method of [`WebDriverWait class`](https://github.com/SeleniumHQ/selenium/blob/trunk/py/selenium/webdriver/support/wait.py)
> - Click on the course [weeks material page](https://cs50.harvard.edu/python/2022/weeks/)
> - Click on the [problem set page](https://cs50.harvard.edu/python/2022/psets/0/) for the Week 0
> - With for loops, `find_elements` of week problem set
> - Every problem page of the first week is checked by Improving with User Input > `while True:`
> - Write the problem sets list of each weekly lesson in a `txt file` with for loops
> - This file is printed by `print` function
> - These procedures are done to write in the order of weeks
> - Control so a member can access all materials
> - All of the functions on the main function are running in the correct order
> - In particular, I took special care to create dynamic for looking at problem sets and weekly courses.

### Automation is done in approximately a few minutes, but manual control takes more time. There is a possibility of manual user error.

<p align="right"><u><a href="#readme-top">back to top</a></u></p>

## Test

Used to check whether all the functions in the code are working as expected. The pytest-selenium plugin provides functionality with browser work for tests.

### `test_project.py`

These are the tests implemented:

```ruby
def test_url():
```

- Showing [Welcome page](https://cs50.harvard.edu/python/2022/)

```ruby
def test_week0():
```

- User should be able to click on Week 0 Functions page then check

```ruby
def test_problem_set_page():
```

- User should be able to click on Problem Set page then check

```ruby
def test_problems_of_week():
```

- Check each problems on:
  <details><summary>Week 0</summary>
  <p>

  #### Improving with User Input > `while True:` with dynamic function

  - [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/)
  - [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/)
  - [Making Faces](https://cs50.harvard.edu/python/2022/psets/0/faces/)
  - [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/)
  - [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/)

  </p>
  </details>

```ruby
def test_week1():
```

- User should be able to click on Week 1 Conditionals page then check

```ruby
def test_week2():
```

- User should be able to click on Week 2 Loops page then check

```ruby
def test_week3():
```

- User should be able to click on Week 3 Exceptions page then check

```ruby
def test_week4():
```

- User should be able to click on Week 4 Libraries page then check

```ruby
def test_week5():
```

- User should be able to click on Week 5 Unit Tests page then check

```ruby
def test_week6():
```

- User should be able to click on Week 6 File I/O page then check

```ruby
def test_week7():
```

- User should be able to click on Week 7 Regular Expressions page then check

```ruby
def test_week8():
```

- User should be able to click onWeek 8 Object-Oriented Programming page then check

```ruby
def test_week9():
```

- User should be able to click on Final Project page then check

---

<!-- all weeks problem sets lists -->

## A summary of the problem sets

Currently working through CS50P, [Intro to programming with python](https://cs50.harvard.edu/python/2022/).

Completed each weeks problem set on here:

<details><summary>Weeks</summary>
 <p>

#### WEEK 0 : [Functions, Variables](https://cs50.harvard.edu/python/2022/weeks/0/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/0/) | Completed |
| ------------------------------------------------------------ | --------- |
| Indoor Voice                                                 | indoor    |
| Playback Speed                                               | play      |
| Making Face                                                  | faces     |
| Einstein                                                     | einstein  |
| Tip Calculator                                               | tip       |

---

#### WEEK 1 : [Conditionals](https://cs50.harvard.edu/python/2022/weeks/1/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/1/) | Completed   |
| ------------------------------------------------------------ | ----------- |
| Deep Thought                                                 | deep        |
| Home Federal Savings Bank                                    | bank        |
| File Extensions                                              | extension   |
| Math Interpreter                                             | interpreter |
| Meal Time                                                    | meal        |

---

#### WEEK 2 : [Loops](https://cs50.harvard.edu/python/2022/weeks/2/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/2/) | Completed |
| ------------------------------------------------------------ | --------- |
| Camel Case                                                   | camel     |
| Coke Machine                                                 | coke      |
| Just setting up my twttr                                     | twttr     |
| Vanity Plates                                                | plates    |
| Nutrition Facts                                              | nutrition |

---

#### WEEK 3 : [Exceptions](https://cs50.harvard.edu/python/2022/weeks/3/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/3/) | Completed |
| ------------------------------------------------------------ | --------- |
| Fuel Gauge                                                   | [fuel     |
| Felipe's Taqueria                                            | taqueria  |
|                                                              |
| Grocery List                                                 | grocery   |
| Outdated                                                     | outdated  |

---

#### WEEK 4 : [Libraries](https://cs50.harvard.edu/python/2022/weeks/4/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/4/) | Completed |
| ------------------------------------------------------------ | --------- |
| Emojize                                                      | emojize   |
| Frank, Ian and Glen’s Letters                                | adieu     |
| Adieu, Adieu                                                 | adieu     |
| Guessing Game                                                | game      |
| Little Professor                                             | professor |
| Bitcoin Price Index                                          | bitcoin   |

---

#### WEEK 5 : [Unit Tests](https://cs50.harvard.edu/python/2022/weeks/5/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/5/) | Completed   |
| ------------------------------------------------------------ | ----------- |
| Testing my twittr                                            | test_twttr  |
| Back to the Bank                                             | test_bank   |
| Re-requesting a Vanity Plate                                 | test_plates |
| Refueling                                                    | test_fuel   |

---

#### WEEK 6 : [File I/O](https://cs50.harvard.edu/python/2022/weeks/6/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/6/) | Completed |
| ------------------------------------------------------------ | --------- |
| Lines of Code                                                | lines     |
| Pizza Py                                                     | pizza     |
| Scourgify                                                    | scourgify |
| CS50 P-Shirt                                                 | shirt     |

---

#### WEEK 7 : [Regular Expressions](https://cs50.harvard.edu/python/2022/weeks/7/)

| [Problem Set](https://cs50.harvard.edu/python/2022/psets/7/) | Completed |
| ------------------------------------------------------------ | --------- |
| NUMB3RS                                                      | numb3rs   |
| Watch on YouTube                                             | [watch    |
| Working 9 to 5                                               | working   |
| Regular, um, Expressions                                     | um        |
| Response Validation                                          | response  |

---

#### WEEK 8 : [Object Oriented Programming](https://cs50.harvard.edu/python/2022/weeks/8/)

| [Problem Set ](https://cs50.harvard.edu/python/2022/psets/8/) | Completed    |
| ------------------------------------------------------------- | ------------ |
| Seasons of Love                                               | seasons      |
| Cookie Jar                                                    | jar          |
| CS50 Shirtificate                                             | shirtificate |

---

#### WEEK 9 : [Et Cetera](https://cs50.harvard.edu/python/2022/weeks/9/)

| [Final Project](https://cs50.harvard.edu/python/2022/project/) | Completed |
| -------------------------------------------------------------- | --------- |
| Final Project                                                  | project   |

</p>
</details>

---

## Contact

Mustafa Kul: [mustafakulkulf1@gmail.com](mailto:mustafakulf1@gmail.com)

LinkedIn : [linkedin.com/in/mkulf1](https://www.linkedin.com/in/mkulf1)

GitHub : [mu5tafacool](https://github.com/mu5tafacool)

<p align="right"><u><a href="#readme-top">back to top</a></u></p>

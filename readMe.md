# Automation Cs50p

## Final Project

#### Video Demo: <URL HERE>

Currently working through CS50P, [Intro to programming with python](https://cs50.harvard.edu/python/2022/). I'll be tracking my problem sets and progress here.

Eventually this repo will probably adjust to hold both CS50P and CS50Web. More to come!

### WEEK 0 : [Functions, Variables](https://github.com/me50/mu5tafacool/tree/main/week0)

| Problem Set    | Date Completed |
| -------------- | -------------- |
| Indoor Voice   | 5/12/22        |
| Playback Speed | 5/12/22        |
| Making Face    | 5/12/22        |
| Einstein       | 5/12/22        |
| Tip Calculator | 5/12/22        |

---

### WEEK 1 : [Conditionals](https://github.com/me50/mu5tafacool/tree/main/week1)

| Problem Set               | Date Completed |
| ------------------------- | -------------- |
| Deep Thought              | 5/12/22        |
| Home Federal Savings Bank | 5/12/22        |
| File Extensions           | 5/12/22        |
| Math Interpreter          | 5/12/22        |
| Meal Time                 | 5/12/22        |

---

### WEEK 2 : [Loops](https://github.com/me50/mu5tafacool/tree/main/week2)

| Problem Set              | Date Completed        |
| ------------------------ | --------------------- |
| Camel Case               | 5/7/22                |
| Coke Machine             | 5/7/22                |
| Just setting up my twttr | 5/7/22                |
| Vanity Plates            | 5/9/22, updated 5/30! |
| Nutrition Facts          | 5/10/22               |

---

### WEEK 3 : [Exceptions](https://github.com/me50/mu5tafacool/tree/main/week3)

| Problem Set       | Date Completed |
| ----------------- | -------------- |
| Fuel Gauge        | 5/14/22        |
| Felipe's Taqueria | 5/15/22        |
| Grocery List      | 5/15/22        |
| Outdated          | 5/21/22        |

---

### WEEK 4 : [Libraries](https://github.com/me50/mu5tafacool/tree/main/week4)

| Problem Set                   | Date Completed |
| ----------------------------- | -------------- |
| Emojize                       | 5/22/22        |
| Frank, Ian and Glen’s Letters | 5/23/22        |
| Adieu, Adieu                  | 5/24/22        |
| Guessing Game                 | 5/25/22        |
| Little Professor              | 5/28/22        |
| Bitcoin Price Index           | 5/28/22        |

---

### WEEK 5 : [Unit Tests](https://github.com/me50/mu5tafacool/tree/main/week5)

| Problem Set                  | Date Completed |
| ---------------------------- | -------------- |
| Testing my twittr            | 5/29/22        |
| Back to the Bank             | 5/29/22        |
| Re-requesting a Vanity Plate | 5/30/22        |
| Refueling                    | 5/30/22        |

---

### WEEK 6 : [File I/O](https://github.com/me50/mu5tafacool/tree/main/week6)

| Problem Set   | Date Completed |
| ------------- | -------------- |
| Lines of Code | 6/2/22         |
| Pizza Py      | 6/3/22         |
| Scourgify     | 6/4/22         |
| CS50 P-Shirt  | 6/5/22         |

---

### WEEK 7 : [Regular Expressions](https://github.com/me50/mu5tafacool/tree/main/week7)

| Problem Set              | Date Completed |
| ------------------------ | -------------- |
| NUMB3RS                  | 6/10/22        |
| Watch on YouTube         | 6/10/22        |
| Working 9 to 5           | 6/11/22        |
| Regular, um, Expressions | 6/11/22        |
| Response Validation      | 6/11/22        |

---

### WEEK 8 : [Object Oriented Programming](https://github.com/me50/mu5tafacool/tree/main/week8)

| Problem Set       | Date Completed |
| ----------------- | -------------- |
| Seasons of Love   | 7/26/22        |
| Cookie Jar        | 11/14/22       |
| CS50 Shirtificate | 11/16/22       |

---

[FINAL PROJECT](https://github.com/me50/mu5tafacool/tree/main/project)

##################################### ##########

# CS50’s Introduction to Programming with Python in Automation Testing

#### Description:

    Final project done as ?????????????????a part of the
    CS50P course by Harvard
      THE REASON WHY I CREATE THIS PROGRAM
       Sure everyone need to improve u programing skill ,And i like ascii art this unique and then i decide to build this program
       and i'm started to research. And i found some library to help me make this project that is pyfiglet and i try it a lot but it doesn't work
       after that i go to stackoverflow and find why it doesn't work and i fix the problem . NOW i so proud of myself and i write the story in my github
       to the way of my life.

This project is to automation the course website using [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/).

#

- To begin, you can install request modules with their methods:

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

- ## This Acceptable Criteria
  > ### Purpose of the test:
  >
  > - Accessing the member course site.
  > - Watching a course introduction video.
  > - See the weekly course materials.
  > - Accessing and seeing each week's problem sets.

### Automation of CS50’s Introduction to Programming with Python

---

#### `project.py`

> Run on beginning

    - Installing a browser to work
    - The second run method maximizes the browser window by webdriver method

first get

> - The browser goes to the [course site](https://cs50.harvard.edu/python/2022/)
> - Opens and closes the introduction video of the course in full screen
> - Opening the elements panel to [inspect](https://en.wikipedia.org/wiki/Web_development_tools) on browser, then creating locators by using the [find_element method](https://www.selenium.dev/documentation/webdriver/elements/finders/)
> - The time has been set to wait for the web pages to be opened by until method of [WebDriverWait class](https://github.com/SeleniumHQ/selenium/blob/trunk/py/selenium/webdriver/support/wait.py)
> - Click on the course [weeks material page](https://cs50.harvard.edu/python/2022/weeks/)
> - Click on the [problem set page](https://cs50.harvard.edu/python/2022/psets/0/) for the first week (week 0)
> - With for loops, findelements of week problem set
> - Every problem page of the first week is checked by Improving with User Input (while True:)
> - Write the problem set list of each weekly lesson in a [txt file](https://github.com/me50/mu5tafacool/blob/main/project/lists_of_problem_set.txt) with for loops
> - This file is printed by print function
> - These procedures are done to write in the order of weeks
> - Control so a member can access all materials
> - All of the functions on the main function are running in the correct order
> - In particular, I took special care to create dynamic for looking at problem sets and weekly courses.

### Automation is done in approximately a few minutes, but manual control takes more time. There is a possibility of manual user error.

### Unit tests

---

_Used to check whether all the functions in the code are working as expected. The pytest-selenium plugin provides functionality with browser work for tests._

### [test_project.py](https://github.com/me50/mu5tafacool/blob/main/project/test_project.py)

- These are the tests implemented

### test_url():

    - Showing [Welcome page](https://cs50.harvard.edu/python/2022/)

> test_week0():

    - User should be able to click on Week 0 Functions page then check

> test_problem_set_page():

    - used to check if the specified position is free to insert marker

> test_problems_of_week():

- Check each problems on:
  <details><summary>Week 0</summary>
  <p>

  #### Improving with User Input (while True:) with dynamic function

  - [Indoor Voice](https://cs50.harvard.edu/python/2022/psets/0/indoor/)
  - [Playback Speed](https://cs50.harvard.edu/python/2022/psets/0/playback/)
  - [Making Faces](https://cs50.harvard.edu/python/2022/psets/0/faces/)
  - [Einstein](https://cs50.harvard.edu/python/2022/psets/0/einstein/)
  - [Tip Calculator](https://cs50.harvard.edu/python/2022/psets/0/tip/)

  </p>
  </details>

> def test_week1():

    - User should be able to click on Week 0 Functions page then check

> def test_week2():

    - User should be able to click on Week 2 Loops page then check

> def test_week3():

    - User should be able to click on Week 3 Exceptions page then check

> def test_week4():

    - User should be able to click on Week 4 Libraries page then check

> def test_week5():

    - User should be able to click on Week 5 Unit Tests page then check

> def test_week6():

    - User should be able to click on Week 6 File I/O page then check

```ruby
def test_week7():
```

    - User should be able to click on Week 7 Regular Expressions page then check

> def test_week8():

    - User should be able to click onWeek 8 Object-Oriented Programming page then check

> def test_week9():

    - User should be able to click on Final Project page then check

## Contact

|              | ??????????                                                 |
| ------------ | ---------------------------------------------------------- |
| Mustafa Kul: | [mustafakulkulf1@gmail.com](mailto:mustafakulf1@gmail.com) |
| -            | -                                                          |

Mustafa Kul: [mustafakulkulf1@gmail.com](mailto:mustafakulf1@gmail.com)

LinkedIn : [linkedin.com/in/mkulf1](https://www.linkedin.com/in/mkulf1)

GitHub : [mu5tafacool](https://github.com/mu5tafacool)

<p align="right"><a href="#readme-top">back to top</a></p>

##################################### ##########

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/mku" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="mku" height="30" width="40" /></a>
</p>
<h3 align="left">Languages and Tools:</h3>
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>

##################################### ##########

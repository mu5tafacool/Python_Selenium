```

code linkedIn.py
```

## alternative above

    pip install -r requirements.txt

requirements.txt

    <!-- selenium>=2.5 -->
    -U Selenium
    webdriver-manager
    pytest-selenium

## version, test run, submit

    python project.py
    python -m  pytest test_project.py

## import

    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time


    # Browser'ı başlatmak vb işlemler için gerekli kütüphane
    from selenium import webdriver
    # Sayfadaki elementlere ulaşmak için gerekli kütüphane
    from selenium.webdriver.common.by import By
    # Sayfanın yüklenmesini bekleyen kütüphane
    from selenium.webdriver.support.wait import WebDriverWait
    # Belli bir koşulun oluşmasını bekleyen kütüphane
    from selenium.webdriver.support import expected_conditions as EC

## Driver

The main idea is to simplify management of binary drivers for different browsers.

### Chrome

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())  ????? neden yuklendigini

### Chromium ?????

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromiumService
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.utils import ChromeType

    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

##

    driver = webdriver.Chrome()
    url = "https://www.linkedin.com/"
    driver.get(url)

    logIn  = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
    logIn.click()

## web element

find_element(By.ID, ‘id’)
find_element(By.NAME, ‘name’)
find_element(By.XPATH, ‘xpath’)

## assert

```
driver.get("http://www.python.org")
```

The next line is an assertion to confirm that title has the word “Python” in it:

```
assert "Python" in driver.title
```

# Second setup

```
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/chromedriver")
#initialize web driver
with webdriver.Chrome(service=service) as driver:
    #navigate to the url
    driver.get('http://127.0.0.1:5500/localwebsite/index.html')
    #find element by xpath
    myDiv = driver.find_element(By.XPATH, '/html/body/div[1]')
    print(myDiv)
    print(myDiv.text)
```

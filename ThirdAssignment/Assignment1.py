import time
from importlib.util import source_hash
from itertools import product

import  pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common import keys


def test_login_angularWebsite():
    base_url = ' https://angular-university.io/ '
    driver = webdriver.Chrome()
    driver.get(base_url)

    driver.find_element(by='xpath', value='//span[text()="My Courses"]').click()
    time.sleep(5)

    driver.find_element(by='xpath',value='//div[text()="Angular For Beginners"]').click()


    checkboxes = driver.find_elements(by='xpath', value='//i[@class="md-icon icon-border"]')
    time.sleep(5)
    for check in checkboxes:
        if check.get(0) :
            check.click()
            print(check.get(0))
            break

    actual_result = driver.find_element(by='xpath', value='//div[@class="message-text"]')
    print(actual_result.text)
    expected_result =" Information "

    time.sleep(5)

    assert  actual_result.text==expected_result


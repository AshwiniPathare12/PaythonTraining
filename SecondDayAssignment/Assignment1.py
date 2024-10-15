import time
from telnetlib import EC
from tkinter.tix import Select

import  pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_login_myntra():
    base_url = 'https://www.amazon.in '
    driver = webdriver.Chrome()
    driver.get(base_url)

    select_category = driver.find_element(by='xpath',value='//div[@id="nav-search-dropdown-card"]')
    time.sleep(5)
    select_category.click()

    dropdown=driver.find_element(by='xpath', value='//select[@id="searchDropdownBox"]')
    time.sleep(5)
    dropdown.click()
    electronic= driver.find_element(by='xpath',value='//option[text()="Electronics"]')
    electronic.click()
    time.sleep(5)

    search_product= driver.find_element(by='xpath', value='//input[@id="twotabsearchtextbox"]')
    search_product.send_keys("bluetooth headphones")
    time.sleep(5)
    search_product.send_keys(Keys.ENTER)

    sort_by_new= driver.find_element(by='xpath', value='//span[@class="a-dropdown-prompt"]')
    sort_by_new.click()

    click_on_new_arrival= driver.find_element(by='xpath',value='//a[text()="Newest Arrivals"]')
    click_on_new_arrival.click()
    time.sleep(5)

    actual_result= driver.find_element(by='xpath',value='//span[contains(text(),"Friday 18 October")]')
    expected_result="Friday 18 October"

    assert actual_result.text == expected_result
    time.sleep(5)
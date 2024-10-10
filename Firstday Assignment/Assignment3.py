import time
from importlib.util import source_hash
from itertools import product

import  pytest
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common import keys


def test_login_myntra():
    base_url = 'https://www.myntra.com/'
    driver = webdriver.Chrome()
    driver.get(base_url)

    search_product= driver.find_element(by='xpath', value='//input[@placeholder="Search for products, brands and more"]')

    search_product.send_keys("Bluetooth headphones")
    search_product.send_keys(Keys.ENTER)
    time.sleep(5)

    select_dropdown= driver.find_element(by='xpath',value='//div[@class="sort-sortBy"]')
    select_dropdown.click()

    select_dropdown_new= driver.find_element(by='xpath', value='//ul[@class="sort-list"]//li[2]')
    select_dropdown_new.click()
    time.sleep(5)

    select_jbl= driver.find_element(by='xpath', value='//ul[@class="brand-list"]/li[2]')
    select_jbl.click()
    time.sleep(5)

    actual_result = driver.find_element(by='xpath', value='//div[@class="product-productMetaInfo"]/h3')
    print(actual_result.text)
    expected_result= "JBL"
    assert actual_result==expected_result
    time.sleep(5)

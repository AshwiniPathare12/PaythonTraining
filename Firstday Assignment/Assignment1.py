import time

from tkinter.tix import Select

import pytest
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def test_login_ebay():

    base_url = 'https://www.ebay.com/'
    driver = webdriver.Chrome()
    driver.get(base_url)

    search_option=driver.find_element(by='xpath', value="//input[@class='gh-tb ui-autocomplete-input']")
    search_option.send_keys("Selenium")

    click_search=driver.find_element(by='id',value='gh-btn')
    click_search.click()

    clik_on_buy= driver.find_element(by='xpath', value='//ul//li[@class="fake-tabs__item btn"][2]')
    clik_on_buy.click()

    click_on_dropdown=driver.find_element(by='xpath', value="//div[@class='srp-controls__sort srp-controls__control']")
    click_on_dropdown.click()

    click_on_new=driver.find_element(by='xpath',value='//div[@class="srp-controls__sort srp-controls__control"]//ul//li[3]')
    click_on_new.click()


import csv
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_data(file_name):
    data_file = open(file_name,'r')
    reader = csv.reader(data_file)

    next(reader) # to skip the header
    data = []
    for rowdata in reader:
        data.append(rowdata)

    return data



@pytest.mark.parametrize("username,password",get_data('LoginCredentials.CSV'))
def test_login(username,password):
    base_url = 'https://www.saucedemo.com/'
    driver = webdriver.Chrome()
    driver.get(base_url)

    driver.find_element(by='id',value='user-name').send_keys(username)

    driver.find_element(by='id',value='password').send_keys(password)

    driver.find_element(by='id',value='login-button').click()
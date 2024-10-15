from selenium import webdriver


def test_Ust_Website():
    base_url = 'https://www.ust.com/en/careers'
    driver = webdriver.Edge()
    driver.get(base_url)


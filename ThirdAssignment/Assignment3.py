import time

from selenium import webdriver


def test_genkin_website() :
    base_url = 'https://www.jenkins.io/doc/'
    driver = webdriver.Firefox()
    driver.get(base_url)

    open_document=driver.find_element(by='xpath',value='//a[@href="/doc/"]')
    open_document.click()

    driver.execute_script("window.scrollTo(0, 1000);")

    driver.find_element(by='xpath',value='//a[@href="#feedback"]').click()

    click_raido_button_yes= driver.find_element(by='xpath',value='//input[@value="Yes"]')
    click_raido_button_yes.click()

    fill_feedback= driver.find_element(by='id',value='ssTestValue').get_attribute("value")
    print(fill_feedback)


    # submit_button= driver.find_element(by='xpath',value='//button[text()="Submit"]')
    # submit_button.click()
    #
    # actual_result= driver.find_element(by='xpath',value='//h3[@id="thank-you-for-your-feedback"]')
    # print(actual_result)
    # expected_result= "Thank you for your feedback! "
    #
    # time.sleep(5)
    #
    # assert  actual_result.text == expected_result
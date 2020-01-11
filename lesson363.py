import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["895", "896","897","898","899","903","904","905"])
def test_number(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector("textarea").send_keys('%s'% answer)
    browser.find_element_by_css_selector('button.submit-submission').click()
    browser.implicitly_wait(10)
    
    assert browser.find_element_by_css_selector('pre.smart-hints__hint').text=='Correct!', "failed"
    

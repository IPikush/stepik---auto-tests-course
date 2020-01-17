from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    input1 = browser.find_element_by_css_selector('''input[name='firstname']''')
    input1.send_keys('Иван')
    input2 = browser.find_element_by_css_selector('''input[name='lastname']''')
    input2.send_keys('Иванов')
    input3 = browser.find_element_by_css_selector('''input[name='email']''')
    input3.send_keys('i.ivanov@ts.ua')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    element=browser.find_element_by_css_selector('''input[type='file']''')
    element.send_keys(file_path)
    
    
    
    
    
    
    button = browser.find_element_by_css_selector("button.btn")
    
    button.click()



    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

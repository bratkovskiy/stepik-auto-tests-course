from selenium import webdriver
import os
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    first_name = browser.find_element_by_css_selector("[name=\"firstname\"]")
    first_name.send_keys("Илья")

    last_name = browser.find_element_by_css_selector("[name=\"lastname\"]")
    last_name.send_keys("Братковский")

    email = browser.find_element_by_css_selector("[name=\"email\"]")
    email.send_keys("ilis@ghj.ru")



    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_class_name("btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


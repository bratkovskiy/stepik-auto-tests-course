from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    answer = browser.find_element_by_id("treasure")
    key = answer.get_attribute("valuex")
    print(key)
    y = calc(key)

    answer2 = browser.find_element_by_id("answer")
    answer2.send_keys(y)

    robot = browser.find_element_by_id("robotCheckbox")
    robot.click()

    rule = browser.find_element_by_id("robotsRule")
    rule.click()

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    imrobot = browser.find_element_by_id("robotCheckbox")
    imrobot.click()



    robots_rule = browser.find_element_by_css_selector("[for=\"robotsRule\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
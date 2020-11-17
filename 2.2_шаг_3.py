from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = int(num1) + int(num2)
    str_sum = str(sum)
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str_sum)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
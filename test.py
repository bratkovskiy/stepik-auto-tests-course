from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    browser.get("https://kazan.110km.ru/")

    description =  browser.find_element_by_name("description")
    descr_text = description.get_attribute("content")
    print("Tag Description was found! Text of tag Description: ",descr_text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
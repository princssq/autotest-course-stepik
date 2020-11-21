from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(log(abs(12*(sin(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #button =
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    x1 = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x1)

    button = browser.find_element(By.ID, "solve")
    button.click()



    #input1 = browser.find_element_by_tag_name("input")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element_by_name("last_name")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element_by_class_name("city")
    #input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

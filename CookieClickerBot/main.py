from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = 60*5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
timeout_start = time.time()


def go_shopping():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    store.reverse()
    store.pop(0)
    for item in store:
        if item.get_attribute("class") != "grayed":
            item.click()
            break


click_counter = 20
iteration = 0
while time.time() < timeout_start + timeout:
    for _ in range(click_counter):
        cookie.click()
    go_shopping()
    if iteration == 7:
        click_counter = 105
    if iteration == 15:
        click_counter = 400
    if iteration == 16:
        click_counter = 250
    if iteration == 21:
        click_counter = 600
    if iteration == 22:
        click_counter = 400
    if iteration == 24:
        click_counter = 200
    iteration += 1

cookies_per_sec = driver.find_element(By.ID, "cps")
score = cookies_per_sec.text.split(":")[1].strip()

print(score)
driver.quit()

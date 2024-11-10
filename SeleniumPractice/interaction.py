from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

data = ["First name", "Last Name", "email@mail.com"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.maximize_window()

# number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# number.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python", Keys.ENTER)

inputs = driver.find_elements(By.CSS_SELECTOR, ".form-signin input")
for i in range(len(inputs)):
    inputs[i].send_keys(data[i], Keys.ENTER)

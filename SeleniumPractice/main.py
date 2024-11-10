from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollars = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is ${price_dollars.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(link.get_attribute("href"))

# bug_link = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
events = {
    i: {
        "time": event_times[i].get_attribute("datetime").split("T")[0],
        "name": event_names[i].text
    }
    for i in range(len(event_times))}

print(events)

# driver.close()  # Close the tab
driver.quit()  # Close the entire browser

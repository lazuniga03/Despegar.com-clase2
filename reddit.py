import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://reddit.com/")

login_button = driver.find_element(by=By.CSS_SELECTOR, value="#login-button")
login_button.click()

time.sleep(5)

username_input = driver.find_element(by=By.XPATH, value='//*[@id="loginUsername"]')
password_input = driver.find_element(by=By.CSS_SELECTOR, value="#loginPassword")

username_input.send_keys('swing772')
password_input.send_keys('ciberseguridad.28')

driver.close()
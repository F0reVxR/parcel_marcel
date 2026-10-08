import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://2captcha.com/ru/demo/recaptcha-v2")

iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='recaptcha/api2/anchor']")))
time.sleep(10)
checkbox = wait.until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
checkbox.click()
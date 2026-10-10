import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_text_of_img(path: str) -> str:

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    driver.get('https://www.prepostseo.com/ru/image-to-text')

    input_pic = os.path.abspath(f'{path}')

    input_zone = driver.find_element(By.ID, 'uploadFile')
    input_zone.send_keys(input_pic)

    upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Извлечь текст']")))
    upload_button.click()

    input_text = wait.until(EC.visibility_of_element_located((By.ID, 'result__text0'))).text

    return input_text
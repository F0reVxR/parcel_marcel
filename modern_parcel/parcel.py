import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pic_enh import enhance_pic
from get_text import get_text_of_img

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.get('https://issaold.beltelecom.by/main.html')

image = driver.find_element(By.XPATH, '//*[@id="capcher"]')
image.screenshot('modern_parcel/pics/secpic_raw.png')
time.sleep(10)

enhance_pic(path='modern_parcel/pics/secpic_raw.png', save_directory='modern_parcel/pics/enhpic.png' ) 

input_text = get_text_of_img(path='modern_parcel/pics/enhpic.png')

text_input_zone = driver.find_element(By.ID, 'cap_field')
text_input_zone.send_keys(input_text)
time.sleep(10)

os.remove('modern_parcel/pics/secpic_raw.png')
os.remove('modern_parcel/pics/enhpic.png')
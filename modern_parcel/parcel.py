import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pic_enh import enhance_pic
from get_text import get_text_of_img

class Parse():

    def __init__(self, link_to_solve, link_img_convert_to_text):

        self._link_to_solve = link_to_solve
        self._link_img_converter = link_img_convert_to_text
    
    def solve_captcha(href: str) -> None:

        driver = webdriver.Chrome()

        driver.get(f'{href}')

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
        driver.quit()

    #solve_captcha('https://issaold.beltelecom.by/main.html')

    def visit_w_UsAge(href: str) -> None:

        options = Options()
        options.add_argument('--user-agent=Semen/4.0 (Windows NT 7.0; Win32; x32) AppleWebkit/1 (KHTML, like Gecko) Shrone/192.168.9.0 Plateau/12.10')
        options.add_argument(f'--proxy-server=https://nullsproxy.com/')

        driver = webdriver.Chrome(options=options)
        driver.get(f'{href}')
        time.sleep(200)
        driver.quit()
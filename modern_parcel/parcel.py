import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pic_enh import enhance_pic
from get_text import get_text_of_img

class Parse_Chrome():

    def __init__(self, link_to_solve, link_img_convert_to_text):

        self._link_to_solve = link_to_solve
        self._link_img_converter = link_img_convert_to_text
        self._driver = webdriver.Chrome()

    def get_screenshot(self, RISTD) -> None:
    
        self._driver.get(f'{self._link_to_solve}')

        image = self._driver.find_element(By.XPATH, '//*[@id="capcher"]')
        image.screenshot(f'{RISTD}')
        print(f'raw image saved to {RISTD}')
        time.sleep(10)
    
    def enhance_img(self, RISTD, EISTD) -> str:

        enhance_pic(path=f'{RISTD}', save_directory=f'{EISTD}' ) 
        input_text = get_text_of_img(path=f'{EISTD}')
        print(f'enhanced image saved to {EISTD}')

        return input_text

    def User_Agent_Mask(href: str) -> Options:

        options = Options()
        options.add_argument('--user-agent=Semen/4.0 (Windows NT 7.0; Win32; x32) AppleWebkit/1 (KHTML, like Gecko) Shrone/192.168.9.0 Plateau/12.10')
        options.add_argument(f'--proxy-server=https://nullsproxy.com/')
        return options

    def input_keys(self, input_text) -> None:

        text_input_zone = self._driver.find_element(By.ID, 'cap_field')

        text_input_zone.send_keys(input_text)
        time.sleep(10)

    def __del__(self) -> None:

        os.remove('modern_parcel/pics/enhpic.png')
        os.remove('modern_parcel/pics/secpic_raw.png')
        self._driver.quit()

#solve_captcha('https://issaold.beltelecom.by/main.html')
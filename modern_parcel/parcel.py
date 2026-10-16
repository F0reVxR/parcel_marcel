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
        self.__driver = webdriver.Chrome()

    class Img():

        def __init__(self, raw_img_store_directory, enh_img_store_directory):

            self._RISTD = raw_img_store_directory #'modern_parcel/pics/secpic_raw.png'
            self._EISTD = enh_img_store_directory #'modern_parcel/pics/enhpic.png'

        def get_screenshot(self) -> None:

            self.__driver.get(f'{self._link_to_solve}')

            image = self.__driver.find_element(By.XPATH, '//*[@id="capcher"]')
            image.screenshot(f'{self._RISTD}')
            print(f'raw image saved to {self._RISTD}')
            time.sleep(10)

        def enhance_img(self) -> str:

            enhance_pic(path=f'{self._RISTD}', save_directory=f'{self._EISTD}' ) 
            input_text = get_text_of_img(path=f'{self._EISTD}')
            print(f'enhanced image saved to {self._EISTD}')

            return input_text

    class Mask():
            
            def User_Agent_Mask(href: str) -> Options:
    
                options = Options()
                options.add_argument('--user-agent=Semen/4.0 (Windows NT 7.0; Win32; x32) AppleWebkit/1 (KHTML, like Gecko) Shrone/192.168.9.0 Plateau/12.10')
    
                return options
        
            def Proxy_Mask(href: str) -> Options:
        
                options = Options()
                options.add_argument(f'--proxy-server=https://nullsproxy.com/')
        
                return options
            
    def input_keys(self) -> None:

        text_input_zone = self.__driver.find_element(By.ID, 'cap_field')
        text_input_zone.send_keys(self.enhance_img())
        time.sleep(10)

    def __del__(self) -> None:

        os.remove(f'{self._RISTD}')
        os.remove(f'{self._EISTD}')
        self.__driver.quit()

#solve_captcha('https://issaold.beltelecom.by/main.html')
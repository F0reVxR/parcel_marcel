from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FParser:

    def __init__(self, link):

        self.link = link
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
        self.links_list = []

    def get_all_links(self):

        elements = self.driver.find_elements(By.TAG_NAME, value='a')
        for element in elements:
            self.links_list.append(element.get_attribute('href'))

    def click_next_page(self):
        time.sleep(3)
        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//main/div/div[1]/div[3]/div[3]/nav/ul/li[7]/a'))
        )

        clickable_element.click()

    def accept_cookies(self):

        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "popup-cookie__confirm"))
        )
        
        clickable_element.click()

    
    def __del__(self):

        print('finished')
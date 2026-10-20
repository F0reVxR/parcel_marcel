from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FParser:

    def __init__(self, link):

        self.link = link
        self.driver = webdriver.Firefox()
        self.links_list = []

        self.driver.get(self.link)

    def get_all_links(self):

        elements = self.driver.find_elements(By.CLASS_NAME, value='c-list__title')
        
        for element in elements:
            self.link_list.append(element.get_attribute('href'))

    def click_next_page(self):

        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(By.CLASS_NAME, "show-more")
        )

        clickable_element.click()
    
    def __del__():

        print('finished')
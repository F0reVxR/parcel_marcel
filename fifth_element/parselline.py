from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FParser:

    def __init__(self, link):

        self.link = link;
        self.driver = webdriver.Chrome();
        self.driver.get(self.link);
        self.links_list = [];
        self.info_list = [];

    def get_all_links(self):

        elements = self.driver.find_elements(By.TAG_NAME, value='c-list__center')
        for element in elements:
            self.link = element(By.TAG_NAME, 'a')
            self.links_list.append(element.get_attribute('href'))

    def click_next_page(self):
        time.sleep(3)
        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div[3]/div[3]/a"))
        )

        self.driver.execute_script("arguments[0].click();", clickable_element)

    def accept_cookies(self):

        clickable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "popup-cookie__confirm"))
        )
        
        clickable_element.click()

    def get_info(self):

        for link in self.links_list[:7]:
            self.driver.get(link + "#characteristics")
            time.sleep(6)
            # wait = WebDriverWait(self.driver, 10)
            # wait.until(EC.any_of((By.CLASS_NAME, "prod-tab-specifications__table")))
            tabble_list = self.driver.find_elements(By.CLASS_NAME, 'prod-tab-specifications__table')
            for table in tabble_list:
                self.info_list.append(table.text)
            time.sleep(3)

    def __del__(self):

        print('finished')
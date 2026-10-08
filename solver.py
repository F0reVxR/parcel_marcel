from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    image_path = Path("capcha_temp/capcha.png").resolve()

    driver.get("https://www.prepostseo.com/ru/image-to-text")

    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

    file_input.send_keys(str(image_path))

    # Ждём, пока файл появится в интерфейсе
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img")))

    extract_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(normalize-space(), 'Извлечь текст')]")))

    extract_button.click()

    print("Изображение отправлено на распознавание.")

finally:
    input("Нажмите Enter для закрытия браузера...")
    driver.quit()

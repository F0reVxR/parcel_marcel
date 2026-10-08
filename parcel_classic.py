from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    # Сначала создаём скриншот
    driver.get("https://www.google.com/recaptcha/api2/demo")

    screenshot_path = Path("capcha_temp/recaptcha.png").resolve()
    screenshot_path.parent.mkdir(exist_ok=True)

    driver.save_screenshot(str(screenshot_path))

    # Открываем сайт, на котором есть загрузка файлов
    driver.get("https://the-internet.herokuapp.com/upload")

    # Находим input type="file"
    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

    # Передаём полный путь к изображению
    file_input.send_keys(str(screenshot_path))

    # Нажимаем кнопку загрузки
    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    upload_button.click()

    # Проверяем результат
    uploaded_file = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))
    print("Загружен файл:", uploaded_file.text)
finally:
    driver.quit()
# https://www.prepostseo.com/ru/image-to-text